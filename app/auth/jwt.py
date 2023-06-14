import secrets
import uuid
from datetime import datetime, timedelta
from typing import Any, Optional

from jose import jwt
from sqlalchemy import insert

from app.auth.config import config
from app.auth.models import RefreshToken
from app.config import settings
from app.database import async_session_maker


async def create_refresh_token(
    *, user_id: int, refresh_token: Optional[str] = None
) -> str:
    async with async_session_maker() as session:
        if not refresh_token:
            refresh_token = secrets.token_urlsafe(32)

        query = insert(RefreshToken).values(
            uuid=uuid.uuid4(),
            refresh_token=refresh_token,
            expires_at=(
                datetime.utcnow() + timedelta(seconds=config.REFRESH_TOKEN_EXP)
            ),
            user_id=user_id,
        )
        await session.execute(query)
        await session.commit()

        return refresh_token


async def create_access_token(*, user_id: int, is_user_admin: bool) -> str:
    expires_delta = timedelta(seconds=config.ACCESS_TOKEN_EXP)
    jwt_data = {
        'iss': settings.SITE_DOMAIN,
        'sub': str(user_id),
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + expires_delta,
        'is_admin': is_user_admin,
    }

    return jwt.encode(jwt_data, config.JWT_SECRET, config.JWT_ALG)


def get_access_token_settings(
    access_token: str,
    expired: bool = False,
) -> dict[str, Any]:
    base_cookie = {
        'key': config.ACCESS_TOKEN_KEY,
        'httponly': True,
        'samesite': 'none',
        'secure': config.SECURE_COOKIES,
        'domain': settings.SITE_DOMAIN,
    }
    if expired:
        return base_cookie

    return {
        **base_cookie,
        'value': access_token,
        'max_age': config.ACCESS_TOKEN_EXP,
    }
