from sqlalchemy import insert

from app.auth.exceptions import InvalidCredentialsException
from app.auth.schemas import UserAuthLoginSchema, UserAuthRegisterSchema
from app.auth.security import check_password, hash_password
from app.core.service import BaseService
from app.database import async_session_maker
from app.users.models import User


class UserService(BaseService):
    model = User

    @classmethod
    async def create(cls, auth_data: UserAuthRegisterSchema):
        async with async_session_maker() as session:
            auth_data.password = hash_password(auth_data.password)
            query = (
                insert(cls.model)
                .values(**auth_data.dict())
                .returning(cls.model.id, cls.model.email, cls.model.name)
            )
            result = await session.execute(query)
            await session.commit()
            return result.mappings().first()

    @classmethod
    async def authenticate_user(cls, auth_data: UserAuthLoginSchema):
        user = await cls.get_object_or_none(email=auth_data.email)
        if not user:
            raise InvalidCredentialsException()

        if not check_password(auth_data.password, user.get('password')):
            raise InvalidCredentialsException()

        return user
