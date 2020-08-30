from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount('/assets', StaticFiles(directory='templates/assets'), name='assets')
templates = Jinja2Templates(directory='templates')


@app.get('/')
def home(request: Request):
    return templates.TemplateResponse('home.html', {
        'request': request
    })
