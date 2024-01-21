
#  import sqlalchemy async packeges

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine

from ..config.config import SETTINGS
from .model import Base

#  making some batteries 


def async_engine(uri) -> AsyncEngine:
    #  creating a engine...
    engine: create_async_engine[AsyncEngine] = create_async_engine(uri)
    return engine



def async_session() -> async_sessionmaker[AsyncSession]: 
    #  creating a session...
    session: async_sessionmaker[AsyncSession] = async_sessionmaker(
        async_engine(SETTINGS.DB_URI), expire_on_commit=False
    ) 
    return session



async def create_all(engine: AsyncEngine):
    #  create a new database...
    engine = async_engine(SETTINGS.DB_URI)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



async def drop_all(engine: AsyncEngine):
    # delete the current database ...
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)