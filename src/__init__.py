#  importing starlette components

from starlette.applications import Starlette 

#  importing router 
from .server import routes
from .server.exception import exception_handlers


def create_app():
    """
    Create a starlette application an return it
    """

    # creating app instance
    app = Starlette(
        routes=routes,
        exception_handlers=exception_handlers,
        debug=True
    )   


    return app

