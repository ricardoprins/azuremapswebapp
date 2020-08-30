import os
import json
import requests
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount('/assets', StaticFiles(directory='templates/assets'), name='assets')
templates = Jinja2Templates(directory='templates')
# apikey = {"map_key": os.environ.get('MAP_KEY')}
apikey = {"map_key": "jphGVAbly1ZAmDCcsyX-q6K263wJWmThhBkue0xJYow"}


class MapKey(BaseModel):
    mapkey: dict


@app.get('/')
def home(request: Request, data: MapKey = apikey):
    return templates.TemplateResponse('home.html', {
        'request': request,
        'data': data
    })
