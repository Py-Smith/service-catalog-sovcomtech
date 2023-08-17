from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import settings as st

DATABASE_URL = f'postgresql+asyncpg://{st.db_user}:{st.db_password}@{st.db_host}:{st.db_port}/{st.db_name}'

# TODO убрать Echo, что бы не выводи сгенерированный SQL
engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()

async_session = sessionmaker(  # type: ignore
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


# Dependency
async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session
