from datetime import date, datetime

from sqlalchemy import DateTime, ForeignKey, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(length=254), nullable=False)
    name: Mapped[str] = mapped_column(String(length=254), nullable=False)
    surname: Mapped[str] = mapped_column(String(length=254), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(length=12), nullable=True)
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"), nullable=True)
    age: Mapped[int] = mapped_column(nullable=True)
    likes: Mapped[int] = mapped_column(default=0, nullable=False)
    dislikes: Mapped[int] = mapped_column(default=0, nullable=False)

    registered_at: Mapped[date] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    password: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)
