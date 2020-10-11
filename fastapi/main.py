from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from dotenv import load_dotenv

import requests
import os


load_dotenv()
app = FastAPI()
template = Jinja2Templates(directory='../templates')

MAP_KEY = os.getenv("MAP_KEY")
WAQI_API_URL = "https://api.waqi.info/map/bounds/?latlng={},{},{},{}&token={}"
WAQI_API_KEY = os.environ["WAQI_API_KEY"]


class Bounds(BaseModel):
    lat1: str
    lat2: str
    lon1: str
    lon2: str


@app.get('/')
async def home(request: Request, map_key: str = MAP_KEY):
    return template.TemplateResponse('home.html', {
        'request': request,
        'map_key': map_key
    })


@app.get("/aqi", response_model=Bounds)
async def get_aqi(request: Request, bounds: Bounds):
    return load_aqi_data(bounds.lat1, bounds.lat2, bounds.lon1, bounds.lon2)


def get_color(aqi):
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


def load_aqi_data(lon1, lat1, lon2, lat2):
    url = WAQI_API_URL.format(lat1, lon1, lat2, lon2, WAQI_API_KEY)
    aqi_data = requests.get(url)

    feature_collection = {"type": "FeatureCollection", "features": []}

    for value in aqi_data.json()["data"]:
        if value["aqi"] != "-":
            feature_collection["features"].append(
                {
                    "type": "Feature",
                    "properties": {"color": get_color(int(value["aqi"]))},
                    "geometry": {
                        "type": "Point",
                        "coordinates": [value["lon"], value["lat"]],
                    },
                }
            )

    return feature_collection
