from typing import Optional

from pydantic import BaseModel, EmailStr, Field, validator

from app.auth.validators import validate_email, validate_password


class UserBaseReadSchema(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class UserAuthRegisterSchema(BaseModel):
    name: str
    surname: Optional[str] = None
    email: EmailStr
    password: str = Field(min_length=8, max_length=24)

    @validator('password')
    def validate_password(cls, password: str) -> str:
        validate_password(password)

        return password

    @validator('email')
    def validate_email(cls, email: str) -> str:
        validate_email(email)

        return email

    class Config:
        schema_extra = {
            'example': {
                'name': 'Ivan',
                'surname': 'Ivanov',
                'email': 'ivanov@gmail.com',
                'password': 'Password1234!',
            }
        }


class UserAuthLoginSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            'example': {
                'email': 'ivanov@gmail.com',
                'password': 'Password1234!',
            }
        }


class UserAccessTokenResponseSchema(BaseModel):
    access_token: str
    refresh_token: str

    class Config:
        orm_mode = True
