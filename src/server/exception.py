
from starlette.requests import Request
from starlette.exceptions import HTTPException
from src.config.config import render as render_template




async def not_found(request: Request, exc: HTTPException):
    # Handle 404 http excptions 
    return render_template( context=request, template='/exceptions/404.html', status_code=exc.status_code)

async def server_error(request: Request, exc: HTTPException):
    # Handle 500 http excptions
    return render_template( contrxt=request, template='/exceptions/500.html', status_code=exc.status_code)



exception_handlers = {
    404: not_found,
    500: server_error
}