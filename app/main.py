import json
import os

import requests
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
app.mount('/assets', StaticFiles(directory='templates/assets'), name='assets')
templates = Jinja2Templates(directory='templates')
apikey = {"map_key": os.environ.get('MAP_KEY')}


class MapKey(BaseModel):
    mapkey: dict


@app.get('/')
def home(request: Request, data: MapKey = apikey):
    return templates.TemplateResponse('home.html', {
        'request': request,
        'data': data
    })
