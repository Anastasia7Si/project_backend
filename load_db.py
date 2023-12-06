from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from src.company.utils import load_csv
from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

async_local_session = sessionmaker(engine, class_=AsyncSession,
                                   expire_on_commit=False)


async def get_async_load_csv() -> AsyncGenerator[AsyncSession, None]:
    async with async_local_session() as db:
        await load_csv(db)
