from fastapi import APIRouter
from fastapi import FastAPI, HTTPException, Request
import requests

import os

from models.weather import Weather
from database.weather import get_weather,create_weather,get_weathers

routes_weather = APIRouter()


# API_KEY = os.environ.get("WEATHER_API_KEY", "8ed7388f2b0ef9633740d639c588a17a")

@routes_weather.post("/history", response_model=Weather)
def create(weather: Weather):
    return create_weather(weather.dict())

@routes_weather.get("/weather")
def get_weather_city(city: str):
    return get_weather(city)
    # try:
    #     res = requests.get(
    #         f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
    #     data = res.json()
    #     if res.status_code != 200:
    #         raise HTTPException(status_code=404, detail="Ciudad no encontrada")
    #     return data
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))
    
@routes_weather.get("/history")
def get_weather_list():
    return get_weathers()