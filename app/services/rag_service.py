# app/services/rag_service.py
from app.services.azure_search_service import AzureSearchService
from app.services.azure_openai_service import AzureOpenAIService

class RAGService:
    def __init__(self):
        self.search_service = AzureSearchService()
        self.openai_service = AzureOpenAIService()

    async def query(self, user_query: str):
        # Step 1: Search for relevant documents
        search_results = await self.search_service.semantic_search(user_query)

        # Step 2: Prepare context from search results
        context = "\n".join([result["content"] for result in search_results])

        # Step 3: Generate response using OpenAI
        prompt = f"""Based on the following company policy information:

{context}

Please answer the following question:
{user_query}

If the answer is not explicitly stated in the policy, please respond with "I'm sorry, but I couldn't find a specific answer to that question in the company policy."
"""

        response = await self.openai_service.generate_response(prompt)

        return {
            "query": user_query,
            "response": response,
            "sources": search_results
        }