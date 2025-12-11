from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.api.db.base import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    action = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
