from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID, Column, DateTime, ForeignKey, String

from app.database import Base


class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    uuid = Column(UUID, primary_key=True, default=uuid4)
    user_id = Column(ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    refresh_token = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime,
        onupdate=datetime.utcnow,
    )
