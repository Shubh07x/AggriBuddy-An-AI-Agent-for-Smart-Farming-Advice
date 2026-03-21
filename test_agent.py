"""
AggriBuddy - Unit Tests
Run with: pytest tests/test_agent.py -v
"""

import pytest
from unittest.mock import MagicMock, patch


# ── RAGPipeline Tests ────────────────────────────────────────────────

class TestRAGPipeline:

    @patch("rag_pipeline.HuggingFaceEmbeddings")
    @patch("rag_pipeline.Chroma")
    def test_retrieve_returns_string(self, mock_chroma, mock_embed):
        """retrieve() should always return a string."""
        from rag_pipeline import RAGPipeline

        mock_doc = MagicMock()
        mock_doc.page_content = "Soybean grows well in Kharif season."
        mock_doc.metadata = {"source": "crop_guide.pdf"}

        mock_chroma.return_value.similarity_search.return_value = [mock_doc]

        rag = RAGPipeline.__new__(RAGPipeline)
        rag.embeddings = mock_embed
        rag.vectorstore = mock_chroma.return_value

        result = rag.retrieve("Which crop in August?")
        assert isinstance(result, str)
        assert len(result) > 0

    @patch("rag_pipeline.HuggingFaceEmbeddings")
    @patch("rag_pipeline.Chroma")
    def test_retrieve_no_docs_returns_fallback(self, mock_chroma, mock_embed):
        """retrieve() with empty vectorstore should return fallback text."""
        from rag_pipeline import RAGPipeline

        mock_chroma.return_value.similarity_search.return_value = []

        rag = RAGPipeline.__new__(RAGPipeline)
        rag.embeddings = mock_embed
        rag.vectorstore = mock_chroma.return_value

        result = rag.retrieve("random query")
        assert "No specific context" in result


# ── AggriBuddy Agent Tests ───────────────────────────────────────────

class TestAggriBuddy:

    @patch("agent.RAGPipeline")
    @patch("agent.ModelInference")
    @patch("agent.Credentials")
    def test_ask_returns_string(self, mock_creds, mock_model, mock_rag):
        """ask() should return a non-empty string answer."""
        from agent import AggriBuddy

        mock_rag.return_value.retrieve.return_value = "Soybean is ideal in August."
        mock_model.return_value.generate_text.return_value = "You should grow soybean in August."

        agent = AggriBuddy()
        result = agent.ask("Which crop in August in Kolhapur?")

        assert isinstance(result, str)
        assert len(result) > 0

    @patch("agent.RAGPipeline")
    @patch("agent.ModelInference")
    @patch("agent.Credentials")
    def test_ask_empty_query(self, mock_creds, mock_model, mock_rag):
        """ask() with empty query should return a helpful message."""
        from agent import AggriBuddy

        agent = AggriBuddy()
        result = agent.ask("")

        assert isinstance(result, str)
        assert len(result) > 0

    @patch("agent.RAGPipeline")
    @patch("agent.ModelInference")
    @patch("agent.Credentials")
    def test_ask_calls_rag(self, mock_creds, mock_model, mock_rag):
        """ask() should call RAG retrieve before calling the LLM."""
        from agent import AggriBuddy

        mock_rag.return_value.retrieve.return_value = "some context"
        mock_model.return_value.generate_text.return_value = "some answer"

        agent = AggriBuddy()
        agent.ask("What pesticide for aphids?")

        mock_rag.return_value.retrieve.assert_called_once()

    @patch("agent.RAGPipeline")
    @patch("agent.ModelInference")
    @patch("agent.Credentials")
    def test_ask_off_topic(self, mock_creds, mock_model, mock_rag):
        """ask() with off-topic query should still return a string (model handles redirect)."""
        from agent import AggriBuddy

        mock_rag.return_value.retrieve.return_value = "No context found."
        mock_model.return_value.generate_text.return_value = (
            "I can only help with farming-related questions."
        )

        agent = AggriBuddy()
        result = agent.ask("Who won IPL 2024?")

        assert isinstance(result, str)
        assert len(result) > 0
