from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
from app.api.db.base import Base

class Ballot(Base):
    __tablename__ = "ballots"

    id = Column(Integer, primary_key=True)
    poll_id = Column(Integer, ForeignKey("polls.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    choice = Column(Boolean, nullable=False)  # Yes / No
    created_at = Column(DateTime(timezone=True), server_default=func.now())
