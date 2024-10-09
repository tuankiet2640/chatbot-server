import os
import dotenv
from azure.search.documents.indexes import SearchIndexClient
from azure.core.credentials import AzureKeyCredential
from openai import openai

dotenv.load_dotenv()

AZURE_SEARCH_SERVICE = os.getenv("AZURE_SEARCH_SERVICE")
AZURE_SEARCH_ENDPOINT = f"https://{AZURE_SEARCH_SERVICE}.search.windows.net"
AZURE_SEARCH_SERVICE_KEY = os.getenv("AZURE_SEARCH_SERVICE_KEY")

search_service_cred = AzureKeyCredential(AZURE_SEARCH_SERVICE_KEY)
index_client = SearchIndexClient(endpoint=AZURE_SEARCH_ENDPOINT, credential=search_service_cred)

def get_ai_response(message: str) -> str:
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=150
    )
    return response.choices.text.strip()
