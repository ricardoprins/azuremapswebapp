import os
from dotenv import load_dotenv
import json
from flask import Flask, render_template, request
import requests

load_dotenv()

MAP_KEY = os.getenv("MAP_KEY")
WAQI_API_URL = "https://api.waqi.info/map/bounds/?latlng={},{},{},{}&token={}"
WAQI_API_KEY = os.environ["WAQI_API_KEY"]


app = Flask(__name__)


@app.route("/")
def home():
    data = {"map_key": MAP_KEY}
    return render_template("home.html", data=data)


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


@app.route("/aqi", methods=["GET"])
def get_aqi():
    bounds = request.args["bounds"].split(",")
    data = load_aqi_data(bounds[0], bounds[1], bounds[2], bounds[3])
    return json.dumps(data)
