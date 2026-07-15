from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_URL = "postgresql+asyncpg://zulmach:change_this_password@postgres:5432/zulmach"


engine = create_async_engine(
    DATABASE_URL,
    echo=True
)


async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class Base(DeclarativeBase):
    pass
