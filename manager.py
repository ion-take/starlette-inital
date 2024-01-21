#  importing the click manager handler
import asyncclick as click

#  importing databse connection components 
from src.model.connection import create_all, drop_all
from src.config.log import logger_manager
from src.config.config import SETTINGS

# creating a logger manager
logger = logger_manager('manage_app')


@click.group()
async def Tasks():pass    # main task object 


@click.command()
async def init_db():
    try:
        await create_all(SETTINGS.DB_URI)
        logger.info('database created')

    except Exception as e:
        logger.error(str(e))


@click.command()
async def drop_db():
    try:
        await database_all(SETTINGS.DB_URI)
        logger.info('database delete')

    except Exception as e:
        logger.error(str(e))


@click.command()
async def add_user():
    """    
        try:
            user =  User(name=name, age=age)
            session.add(user)
            session.commit()

        except Exception as e:
            logger.error(str(e))
            await sesstion.rolleback()
    """
    raise NotImplementedError()    # remove this line

Tasks.add_command(init_db)
Tasks.add_command(drop_db)

if __name__=='__main__':
    Tasks()