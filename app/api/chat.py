from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.message import MessageCreate
from app.schemas.ai_response import AIResponseCreate
from app.repositories.message_repository import MessageRepository
from app.repositories.ai_response_repository import AIResponseRepository
from app.utils.azure_openai import get_ai_response
from app.db.database import get_db

router = APIRouter()

@router.post("/chat")
def chat(message: MessageCreate, db: Session = Depends(get_db)):
    message_repo = MessageRepository()
    ai_response_repo = AIResponseRepository()

    db_message = message_repo.create_message(db, message)
    ai_response_content = get_ai_response(db_message.message_content)
    ai_response = AIResponseCreate(message_id=db_message.id, response_content=ai_response_content)
    db_ai_response = ai_response_repo.create_ai_response(db, ai_response)

    return {"message": db_message, "ai_response": db_ai_response}
