from fastapi import APIRouter, Depends
from app.services.openai_service import OpenAIService
from app.services.search_service import SearchService
from app.models.pydantic_models import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(
        request: ChatRequest,
        openai_service: OpenAIService = Depends(),
        search_service: SearchService = Depends()
):
    # Get relevant context from search service
    context = await search_service.search(request.message)

    # Generate response using OpenAI service
    response = await openai_service.generate_response(request.message, context)

    return ChatResponse(response=response)