import openai
import os

class AzureOpenAIService:
    def __init__(self):
        openai.api_type = "azure"
        openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
        openai.api_version = "2023-05-15"
        openai.api_key = os.getenv("AZURE_OPENAI_KEY")
        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

    async def generate_response(self, prompt: str, max_tokens: int = 150):
        response = openai.Completion.create(
            engine=self.deployment_name,
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()

    async def generate_embedding(self, text: str):
        response = openai.Embedding.create(
            input=text,
            engine=self.deployment_name
        )
        return response['data'][0]['embedding']
