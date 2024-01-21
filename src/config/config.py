
import os 
import os.path

from pathlib import Path
from secrets import token_hex


from starlette.config import Config
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.datastructures import Secret, CommaSeparatedStrings
from starlette.status import HTTP_200_OK


# setting the configurations variables 

class SETTINGS:
    """ APP config """
    config = Config('.env')

    DB_URI = config('DB_URI', cast=str)

    

def get_resouces_location(*name):
    """
    This func creates a comunication between the app and the static resources.
    
    args:
        obj (object) : object to generate a path for.
        name (str) : name of the end file directory.

    params:
        location_str (callable) : generate the path to a certain resouse.
    """
    parent_path = Path(os.path.dirname(__file__)).resolve().parents[0]

    location_str = os.path.join(parent_path, *name)
    return str(location_str)



# resources getter 
Template = Jinja2Templates(directory=get_resouces_location('templates'))
Static = StaticFiles(directory=get_resouces_location('static'))

# tamplate rendering 
def render(template=None, context=None, status_code=HTTP_200_OK):
    return Template.TemplateResponse( context, template, status_code=status_code)




