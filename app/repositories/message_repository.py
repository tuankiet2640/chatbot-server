from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.message import Message

class MessageRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_message(self, message: Message):
        try:
            self.session.add(message)
            self.session.commit()
            return message
        except IntegrityError:
            self.session.rollback()
            raise ValueError("Message with this content already exists.")

    def get_message_by_id(self, message_id: int):
        return self.session.query(Message).filter_by(id=message_id).first()

    def get_all_messages(self):
        return self.session.query(Message).all()

    def update_message(self, message_id: int, new_content: str):
        message = self.get_message_by_id(message_id)
        if message:
            message.message_content = new_content
            self.session.commit()
            return message
        else:
            raise ValueError("Message not found.")

    def delete_message(self, message_id: int):
        message = self.get_message_by_id(message_id)
        if message:
            self.session.delete(message)
            self.session.commit()
        else:
            raise ValueError("Message not found.")
