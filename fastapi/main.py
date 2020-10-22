from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import requests
import os


load_dotenv()
app = FastAPI()
template = Jinja2Templates(directory='../templates')

MAP_KEY = os.getenv("MAP_KEY")
WAQI_API_URL = "https://api.waqi.info/map/bounds/?latlng={},{},{},{}&token={}"
WAQI_API_KEY = os.environ["WAQI_API_KEY"]


@app.get('/')
async def home(request: Request, map_key: str = MAP_KEY):
    return template.TemplateResponse('home.html', {
        'request': request,
        'map_key': map_key
    })


@app.get("/aqi")
async def get_aqi(bounds: str):
    mapdata = bounds.split(",")
    return load_aqi_data(mapdata[0], mapdata[1], mapdata[2], mapdata[3])


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