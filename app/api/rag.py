from fastapi import APIRouter, Depends
from app.services.rag_service import RAGService
from pydantic import BaseModel

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query: str
    response: str
    sources: list

@router.post("/query", response_model=QueryResponse)
async def query_policy(request: QueryRequest, rag_service: RAGService = Depends(RAGService)):
    result = await rag_service.query(request.query)
    return result