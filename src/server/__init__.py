from starlette.routing import Mount

#  importing static object
from ..config.config import Static

#  importing routes
from .main import home_routes

#  Router defition
PUBLIC_ROUTER:list = []
PRIVATE_ROUTER:list= []

PUBLIC_ROUTER.extend(home_routes)


routes = [
    Mount('/static', app=Static, name='static'),
    Mount('/', routes=PUBLIC_ROUTER, name='public'),
]