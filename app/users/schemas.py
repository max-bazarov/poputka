from pydantic import BaseModel, EmailStr, validator, Field

from app.users.utils import validate_password


class UserBaseReadSchema(BaseModel):
    email: EmailStr
    username: str

    class Config:
        orm_mode = True


class UserAuthSchema(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)

    @validator('password')
    def validate_password(cls, password: str) -> str:
        validate_password(password)

        return password


class UserLoginAccessTokenResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
