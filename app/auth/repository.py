from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError
from app.auth.schemas import RefreshTokenCreateSchema, UserRegisterSchema
from app.auth.security import hash_password
from app.db import Base, async_session_maker
from app.repository.base import SQLAlchemyRepository
from app.auth.models import RefreshToken
from app.users.models import User
from app.logger import logger


class AuthRepository(SQLAlchemyRepository):
    model: Base = User

    async def create(self, user_data: UserRegisterSchema):
        try:
            async with async_session_maker() as session:
                auth_data = user_data.model_dump()
                auth_data["password"] = hash_password(user_data.password)
                query = (
                    insert(self.model)
                    .values(**auth_data)
                    .returning(self.model.id, self.model.name, self.model.email)
                )
                result = await session.execute(query)
                await session.commit()
                return result.mappings().first()

        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database Exc: Cannot register user"
            elif isinstance(e, Exception):
                msg = "Unknown Exc: Cannot register user"
            extra = {**user_data.model_dump()}
            extra["first_name"] = extra.pop("name")
            logger.error(msg, extra=extra, exc_info=True)


class JWTRepository(SQLAlchemyRepository):
    model: Base = RefreshToken

    async def create(self, refresh_token_data: RefreshTokenCreateSchema):
        try:
            async with async_session_maker() as session:
                query = (
                    insert(self.model)
                    .values(**refresh_token_data.model_dump())
                    .returning(self.model)
                )
                result = await session.execute(query)
                await session.commit()
                return result.mappings().first()

        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database Exc: Cannot register user"
            elif isinstance(e, Exception):
                msg = "Unknown Exc: Cannot register user"
            extra = {**refresh_token_data.model_dump()}
            logger.error(msg, extra=extra, exc_info=True)
