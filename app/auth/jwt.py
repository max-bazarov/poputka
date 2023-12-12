# import secrets
# from datetime import datetime, timedelta
# from typing import Any
# from uuid import UUID

# from jose import jwt

# from app.auth.config import config
# from app.auth.service import RefreshTokenService
# from app.config import settings


# def _create_refresh_token_value():
#     return secrets.token_urlsafe(32)


# async def create_refresh_token(*, user_id: int) -> str:
#     old_refresh_token = await RefreshTokenService.get_object_or_none(user_id=user_id)
#     if old_refresh_token:
#         await RefreshTokenService.delete(uuid=old_refresh_token.uuid)

#     refresh_token_value = _create_refresh_token_value()

#     await RefreshTokenService.create(
#         refresh_token=refresh_token_value,
#         expires_at=(datetime.utcnow() + timedelta(seconds=config.REFRESH_TOKEN_EXP)),
#         user_id=user_id,
#     )

#     return refresh_token_value


# async def update_refresh_token(*, old_refresh_token: UUID) -> str:
#     refresh_token_value = _create_refresh_token_value()

#     await RefreshTokenService.update(
#         uuid=old_refresh_token.uuid,
#         refresh_token=refresh_token_value,
#         expires_at=(datetime.utcnow() + timedelta(seconds=config.REFRESH_TOKEN_EXP)),
#     )

#     return refresh_token_value


# def create_access_token(user_id: int) -> str:
#     expires_delta = timedelta(seconds=config.ACCESS_TOKEN_EXP)
#     jwt_data = {
#         "iss": settings.SITE_DOMAIN,
#         "sub": str(user_id),
#         "iat": datetime.utcnow(),
#         "exp": datetime.utcnow() + expires_delta,
#     }

#     return jwt.encode(jwt_data, config.JWT_SECRET, config.JWT_ALG)


# def get_token_settings(
#     token_value: str,
#     token_key: str,
#     token_exp: int,
#     expired: bool = False,
# ) -> dict[str, Any]:
#     base_cookie = {
#         "key": token_key,
#         "httponly": True,
#         "samesite": "strict",
#         "secure": config.SECURE_COOKIES,
#         "domain": settings.SITE_DOMAIN,
#     }
#     if expired:
#         return base_cookie

#     return {
#         **base_cookie,
#         "value": token_value,
#         "max_age": token_exp,
#     }
