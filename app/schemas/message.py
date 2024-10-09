from pydantic import BaseModel

class MessageCreate(BaseModel):
    message_content: str
    user_id: int

class Message(BaseModel):
    id: int
    message_content: str
    user_id: int

    class Config:
        orm_mode = True