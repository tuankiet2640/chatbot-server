from pydantic import BaseModel

class AIResponseCreate(BaseModel):
    message_id: int
    response_content: str

class AIResponse(BaseModel):
    id: int
    message_id: int
    response_content: str

    class Config:
        orm_mode = True
