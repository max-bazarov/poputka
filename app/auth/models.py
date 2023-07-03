from datetime import datetime

from sqlalchemy import UUID, Column, ForeignKey, String, DateTime

from app.database import Base


class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    uuid = Column(UUID, primary_key=True)
    user_id = Column(ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    refresh_token = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )
