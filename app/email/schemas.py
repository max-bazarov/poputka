from pydantic import BaseModel, EmailStr, field_validator

from app.email.validators import validate_email


class UserRegisterEmailSchema(BaseModel):
    user_email: EmailStr
    user_name: str
    user_id: int
    user_access_token: str
    subject: str

    @field_validator("user_email")
    def validate_email(cls, email: str) -> str:
        validate_email(email)

        return email
