from typing import AsyncGenerator

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import app_settings

DATABASE_PARAMS = {}

if app_settings.MODE == "TEST":
    DATABASE_PARAMS = {"poolclass": NullPool}


engine = create_async_engine(app_settings.database_url, **DATABASE_PARAMS)

async_session_maker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
