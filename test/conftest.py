
from typing import AsyncIterator
from starlette.testclient import TestClient
from src import create_app

from src.model.connection import create_all, drop_all
from src.config.log import logger_manager 
from src.model.connection import async_engine

from dotenv import dotenv_values
import pytest
import httpx
import pytest_asyncio



@pytest_asyncio.fixture()
async def client() -> AsyncIterator[httpx.AsyncClient]:
   async with httpx.AsyncClient(app=create_app(), base_url="http://testserver") as client:
      
      log = logger_manager('testing')
      log.info('initializing db process')
      try:
         log.info('Creating database')
         await create_all(async_engine(DB_URI))
         log.info('Database created')

      except Exception as e:
         log.error(str(e))

      yield client

      try:
         log.info('Dorping database')
         await drop_all(async_engine(DB_URI))
         log.inf('dropping database')
         
      except Exception as e:
         log.error(str(e))



