from sqlalchemy import Column, Integer, String, DateTime
import datetime
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String)
    user_id = Column(Integer)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Task( \
            \nid={self.id}, \
            \ncreated_at={self.created_at}, \
            \description={self.description}, \
            \nuser_id={self.user_id}, \
            \nupdated_at={self.updated_at}, \
            \n)"
