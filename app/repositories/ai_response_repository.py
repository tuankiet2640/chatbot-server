from sqlalchemy.orm import Session
from app.models.ai_response import AIResponse
from app.schemas.ai_response import AIResponseCreate

class AIResponseRepository:
    def create_ai_response(self, db: Session, ai_response: AIResponseCreate):
        db_ai_response = AIResponse(**ai_response.dict())
        db.add(db_ai_response)
        db.commit()
        db.refresh(db_ai_response)
        return db_ai_response

    def get_ai_response(self, db: Session, response_id: int):
        return db.query(AIResponse).filter(AIResponse.id == response_id).first()
