"""
AggriBuddy - RAG Pipeline
Handles document loading, embedding, vector indexing and retrieval
Author: Shubham Dattatray Potdar
"""

import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

DOCS_DIR    = os.getenv("DOCS_DIR", "./docs")
VECTOR_DIR  = os.getenv("VECTOR_DIR", "./vectorstore")
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K       = 4


class RAGPipeline:
    def __init__(self):
        print("📚 Loading RAG Pipeline...")
        self.embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
        self.vectorstore = self._load_or_build_vectorstore()
        print("✅ RAG Pipeline ready!")

    def _load_or_build_vectorstore(self):
        """Load existing vectorstore or build from docs folder."""
        if os.path.exists(VECTOR_DIR):
            print("📂 Loading existing vectorstore...")
            return Chroma(
                persist_directory=VECTOR_DIR,
                embedding_function=self.embeddings
            )

        print("🔨 Building vectorstore from documents...")
        return self._build_vectorstore()

    def _build_vectorstore(self):
        """Load PDFs, split into chunks, embed and store."""
        if not os.path.exists(DOCS_DIR):
            os.makedirs(DOCS_DIR)
            print(f"📁 Created docs folder at '{DOCS_DIR}'. Add your agricultural PDFs there.")
            # Return empty store if no docs yet
            return Chroma(
                persist_directory=VECTOR_DIR,
                embedding_function=self.embeddings
            )

        # Load all PDFs from docs folder
        loader = DirectoryLoader(DOCS_DIR, glob="**/*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()

        if not documents:
            print("⚠️  No PDFs found in docs/ folder. Add agricultural PDFs to enable RAG.")
            return Chroma(
                persist_directory=VECTOR_DIR,
                embedding_function=self.embeddings
            )

        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=100,
            separators=["\n\n", "\n", ".", " "]
        )
        chunks = splitter.split_documents(documents)
        print(f"📄 Loaded {len(documents)} documents → {len(chunks)} chunks")

        # Build and persist vectorstore
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=VECTOR_DIR
        )
        vectorstore.persist()
        print(f"💾 Vectorstore saved to '{VECTOR_DIR}'")
        return vectorstore

    def retrieve(self, query: str, k: int = TOP_K) -> str:
        """
        Retrieve top-k relevant chunks for a given query.
        Returns a single formatted string to inject into the LLM prompt.
        """
        docs = self.vectorstore.similarity_search(query, k=k)

        if not docs:
            return "No specific context found. Answer based on general agricultural knowledge."

        context_parts = []
        for i, doc in enumerate(docs, 1):
            source = doc.metadata.get("source", "Agricultural Document")
            context_parts.append(f"[Source {i}: {os.path.basename(source)}]\n{doc.page_content}")

        return "\n\n".join(context_parts)

    def add_documents(self, pdf_path: str):
        """Add a new PDF document to the existing vectorstore."""
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
        chunks = splitter.split_documents(documents)

        self.vectorstore.add_documents(chunks)
        self.vectorstore.persist()
        print(f"✅ Added {len(chunks)} chunks from {pdf_path}")
