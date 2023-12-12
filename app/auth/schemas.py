from datetime import date, datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, field_validator

from app.auth.validators import validate_password
from app.email.validators import validate_email


class UserBaseReadSchema(BaseModel):
    id: int
    email: EmailStr


class UserRegisterSchema(BaseModel):
    name: str
    surname: Optional[str] = None
    email: EmailStr
    password: str = Field(min_length=8, max_length=24)

    @field_validator("password")
    def validate_password(cls, password: str) -> str:
        validate_password(password)

        return password

    @field_validator("email")
    def validate_email(cls, email: str) -> str:
        validate_email(email)

        return email

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Ivan",
                "surname": "Ivanov",
                "email": "ivanov@gmail.com",
                "password": "Password1234!",
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "ivanov@gmail.com",
                "password": "Password1234!",
            }
        }


class AccessTokenResponseSchema(BaseModel):
    access_token: str
    refresh_token: str


class RefreshTokenSchema(BaseModel):
    uuid: UUID
    user_id: int
    refresh_token: str
    expires_at: date
    created_at: date
    updated_at: date


class RefreshTokenCreateSchema(BaseModel):
    user_id: int
    refresh_token: str
    expires_at: datetime
