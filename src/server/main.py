

from starlette.routing import Route
from starlette.responses import Response 
from starlette.requests import Request 
from starlette.status import HTTP_200_OK

#  importing config
from ..config.config import render



async def home(request: Request)-> Response:
    return render(template='home/index.html',context=request)


home_routes = [
    Route('/', endpoint=home, name='home.main')
]