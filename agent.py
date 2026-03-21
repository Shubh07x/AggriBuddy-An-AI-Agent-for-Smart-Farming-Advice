"""
AggriBuddy - AI Agent for Smart Farming Advice
Main agent entry point
Author: Shubham Dattatray Potdar
D. Y. Patil College of Engineering & Technology, Kolhapur
"""

import os
from dotenv import load_dotenv
from rag_pipeline import RAGPipeline
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()

# ── IBM Watsonx Config ──────────────────────────────────────────────
IBM_API_KEY     = os.getenv("IBM_API_KEY")
WATSONX_URL     = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
WATSONX_PROJECT = os.getenv("WATSONX_PROJECT_ID")

SYSTEM_PROMPT = """
You are AggriBuddy, an AI farming assistant for small and marginal farmers in India.
You ONLY answer questions related to:
- Crop selection, sowing and harvesting
- Pest and disease identification and control
- Mandi (market) prices and selling advice
- Soil health and fertilizer guidance
- Weather impact on farming
- Government farming schemes (PM-KISAN, PMFBY, etc.)

If the question is NOT related to farming or agriculture, politely say:
"I can only help with farming-related questions. Please ask me about crops, pests, soil, or market prices."

Always respond in the same language the farmer used (Hindi, Marathi, or English).
Keep answers simple, practical, and actionable.
"""


class AggriBuddy:
    def __init__(self):
        print("🌾 Initializing AggriBuddy...")
        self.rag = RAGPipeline()

        credentials = Credentials(
            url=WATSONX_URL,
            api_key=IBM_API_KEY
        )

        self.model = ModelInference(
            model_id="ibm/granite-13b-chat-v2",
            credentials=credentials,
            project_id=WATSONX_PROJECT,
            params={
                "max_new_tokens": 512,
                "temperature": 0.3,
                "repetition_penalty": 1.1
            }
        )
        print("✅ AggriBuddy is ready!")

    def ask(self, query: str) -> str:
        """
        Takes a farmer query, retrieves grounded context via RAG,
        sends to IBM Granite LLM, returns a trusted answer.
        """
        if not query or not query.strip():
            return "Please ask a farming-related question."

        # Step 1: Retrieve relevant context from Vector Index
        context = self.rag.retrieve(query)

        # Step 2: Build prompt
        prompt = f"""{SYSTEM_PROMPT}

Context from trusted agricultural sources:
{context}

Farmer's Question: {query}

Answer:"""

        # Step 3: Get answer from IBM Granite
        response = self.model.generate_text(prompt=prompt)
        return response.strip()

    def chat(self):
        """Interactive CLI chat loop for testing locally."""
        print("\n🌾 Welcome to AggriBuddy - Smart Farming Assistant")
        print("Ask your farming questions below. Type 'exit' to quit.\n")

        while True:
            query = input("You: ").strip()
            if query.lower() in ["exit", "quit", "bye"]:
                print("AggriBuddy: Jai Kisan! 🌾 Goodbye!")
                break
            if not query:
                continue

            print("AggriBuddy: Thinking...")
            answer = self.ask(query)
            print(f"AggriBuddy: {answer}\n")


if __name__ == "__main__":
    agent = AggriBuddy()
    agent.chat()
