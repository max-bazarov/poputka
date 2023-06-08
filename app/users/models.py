from datetime import datetime

from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(length=254), nullable=False)
    name = Column(String(length=254), nullable=False)
    surname = Column(String(length=254))
    phone_number = Column(String)
    car_id = Column(ForeignKey('car.id'))
    age = Column(Integer, nullable=False)
    likes = Column(Integer, default=0)
    dislikes = Column(Integer, default=0)

    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_admin: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
