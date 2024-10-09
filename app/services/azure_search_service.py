from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables

class AzureSearchService:
    def __init__(self):
        self.search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
        self.search_key = os.getenv("AZURE_SEARCH_SERVICE_KEY")  # Update this line
        self.index_name = os.getenv("AZURE_SEARCH_SERVICE")  # Assuming this is your index name
        print(f"Search Key: {self.search_key}")  # Debugging line to check the key
        if not self.search_key:
            raise ValueError("AZURE_SEARCH_SERVICE_KEY environment variable is not set.")
        if not self.search_endpoint:
            raise ValueError("AZURE_SEARCH_ENDPOINT environment variable is not set.")
        if not self.index_name:
            raise ValueError("AZURE_SEARCH_SERVICE environment variable is not set.")

        self.credential = AzureKeyCredential(self.search_key)
        self.client = SearchClient(endpoint=self.search_endpoint,
                                   index_name=self.index_name,
                                   credential=self.credential)

    async def search_documents(self, query: str, top: int = 3):
        results = self.client.search(search_text=query, top=top)
        return [{"id": result["id"], "content": result["content"]} for result in results]

    async def semantic_search(self, query: str, top: int = 3):
        results = self.client.search(
            search_text=query,
            query_type="semantic",
            semantic_configuration_name="default",
            top=top
        )
        return [{"id": result["id"], "content": result["content"]} for result in results]

    async def vector_search(self, query_vector: list, top: int = 3):
        vector_query = VectorizedQuery(vector=query_vector, k_nearest_neighbors=top, fields="contentVector")
        results = self.client.search(
            search_text="",
            vector_queries=[vector_query],
            select=["id", "content"],
            top=top
        )
        return [{"id": result["id"], "content": result["content"]} for result in results]
