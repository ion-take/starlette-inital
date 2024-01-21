# importing a production server
import uvicorn 

#  importing the app we created
from src import create_app


app = create_app()


if __name__ == '__main__':
    uvicorn.run(app)
