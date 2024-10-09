from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True, index= True)
    message_content = Column(String, unique=True, index=True)
    user = relationship("User", back_populates="messages")
    ai_response = relationship("AIResponse", uselist=False, back_populates="message")
