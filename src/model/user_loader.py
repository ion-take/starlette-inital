
# import starlette components

from stalette.requests import Request 


#  load your users here ...

async def user_loader(request:Request, _id: int):
    """
    Example:
        query = select(User).options( your options here ).limit(1)
        result = await session.execute(query)
        user = result.scalar()

        return user
    """
     raise NotImplementedError()    # remove this line