from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String

from app.database import Base


class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    refresh_token = Column(String, nullable=False)
    expires_at = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = Column(TIMESTAMP, onupdate=datetime.utcnow, nullable=False)
