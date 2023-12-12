import secrets
from datetime import datetime, timedelta

from typing import Any
from uuid import UUID
from app.auth.exceptions import InvalidCredentialsException
from app.auth.repository import AuthRepository, JWTRepository
from app.auth.security import check_password
from app.email.schemas import UserRegisterEmailSchema
from app.email.service import EmailService

from fastapi import Response
from jose import jwt

from app.auth.config import auth_settings

from app.auth.schemas import (
    RefreshTokenCreateSchema,
    UserLoginSchema,
    UserRegisterSchema,
)

from app.config import app_settings

from app.repository.base import AbstractRepository


class JWTService:
    def __init__(self, jwt_repo: AbstractRepository):
        self.jwt_repo: JWTRepository = jwt_repo

    @staticmethod
    def _create_refresh_token_value():
        return secrets.token_urlsafe(32)

    async def create_refresh_token(self, *, user_id: int, response: Response) -> str:
        old_refresh_token = await self.jwt_repo.get_one_or_none(user_id=user_id)
        if old_refresh_token:
            await self.jwt_repo.delete(id=old_refresh_token.id)

        refresh_token_value = self._create_refresh_token_value()

        refresh_token = RefreshTokenCreateSchema(
            user_id=user_id,
            refresh_token=refresh_token_value,
            expires_at=(
                datetime.utcnow() + timedelta(seconds=auth_settings.REFRESH_TOKEN_EXP)
            ),
        )

        await self.jwt_repo.create(refresh_token)

        response.set_cookie(
            **self.get_token_settings(
                refresh_token_value,
                auth_settings.REFRESH_TOKEN_KEY,
                auth_settings.REFRESH_TOKEN_EXP,
            )
        )

        return refresh_token_value

    async def update_refresh_token(self, *, old_refresh_token: UUID) -> str:
        refresh_token_value = self._create_refresh_token_value()

        await self.jwt_repo.update(
            uuid=old_refresh_token.uuid,
            refresh_token=refresh_token_value,
            expires_at=(
                datetime.utcnow() + timedelta(seconds=auth_settings.REFRESH_TOKEN_EXP)
            ),
        )

        return refresh_token_value

    def create_access_token(self, *, user_id: int, response: Response) -> str:
        expires_delta = timedelta(seconds=auth_settings.ACCESS_TOKEN_EXP)
        jwt_data = {
            "iss": app_settings.SITE_DOMAIN,
            "sub": str(user_id),
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + expires_delta,
        }

        access_token_value = jwt.encode(
            jwt_data, auth_settings.JWT_SECRET, auth_settings.JWT_ALG
        )

        response.set_cookie(
            **self.get_token_settings(
                access_token_value,
                auth_settings.ACCESS_TOKEN_KEY,
                auth_settings.ACCESS_TOKEN_EXP,
            )
        )
        return access_token_value

    @staticmethod
    def get_token_settings(
        token_value: str,
        token_key: str,
        token_exp: int,
        expired: bool = False,
    ) -> dict[str, Any]:
        base_cookie = {
            "key": token_key,
            "httponly": True,
            "samesite": "strict",
            "secure": auth_settings.SECURE_COOKIES,
            "domain": app_settings.SITE_DOMAIN,
        }
        if expired:
            return base_cookie

        return {
            **base_cookie,
            "value": token_value,
            "max_age": token_exp,
        }


class AuthService:
    def __init__(
        self,
        auth_repo: AbstractRepository,
        jwt_service: JWTService,
        email_service: EmailService,
    ):
        self.auth_repo: AuthRepository = auth_repo
        self.jwt_service: JWTService = jwt_service
        self.email_service: EmailService = email_service

    async def register_user(self, user_data: UserRegisterSchema, response: Response):
        user = await self.auth_repo.create(user_data)
        refresh_token_value = await self.jwt_service.create_refresh_token(
            user_id=user.id, response=response
        )
        access_token_value = self.jwt_service.create_access_token(
            user_id=user.id, response=response
        )

        email_data = UserRegisterEmailSchema(
            user_email=user.email,
            user_name=user.name,
            user_id=user.id,
            user_access_token=access_token_value,
            subject="Подтверждение почты",
        )

        self.email_service.send_email(email_data)

        return access_token_value, refresh_token_value

    async def authenticate_user(self, user_data: UserLoginSchema):
        user = await self.auth_repo.get_one_or_none(email=user_data.email)
        if not user:
            raise InvalidCredentialsException()

        if not check_password(user_data.password, user.get("password")):
            raise InvalidCredentialsException()

        return user

    async def verify_user(self, token: str):
        """Verify user token via email message"""
        pass
