from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount('/assets', StaticFiles(directory='templates/assets'), name='assets')
templates = Jinja2Templates(directory='templates')


def get_color(aqi: float):
    """Creates color coding according to the Air Quality Index
    Args:
        aqi : Air Quality Index
    Returns:
        str: Hexadecimal color code
    """
    if aqi <= 50:
        return "#009966"
    if aqi <= 100:
        return "#ffde33"
    if aqi <= 150:
        return "#ff9933"
    if aqi <= 200:
        return "#cc0033"
    if aqi <= 300:
        return "#660099"
    return "#7e0023"


@app.get('/')
def home(request: Request):
    return templates.TemplateResponse('home.html', {
        'request': request
    })
