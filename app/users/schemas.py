from uuid import UUID, uuid4

from typing import Optional

from datetime import datetime

from pydantic import BaseModel, EmailStr


class Profile(BaseModel):
    id: UUID = uuid4()
    email: EmailStr
    name: str
    surname: str
    phone_number: Optional[str] = None
    car_id: Optional[int] = None
    age: Optional[int] = None
    likes: Optional[int]
    dislikes: Optional[int]
    registered_at: datetime
    is_admin: bool
    is_active: bool
    is_verified: bool

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    id: UUID = uuid4()
    name: str
    surname: str
    age: Optional[int] = None
    likes: int
    dislikes: int
    registered_at: datetime

    class Config:
        orm_mode = True
