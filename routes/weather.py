from fastapi import APIRouter
from fastapi import FastAPI, HTTPException, Request
import requests

import os

from models.weather import Weather
from database.weather import get_weather,create_weather,get_weathers

routes_weather = APIRouter()

@routes_weather.post("/history", response_model=Weather)
def create(weather: Weather):
    return create_weather(weather.dict())

@routes_weather.get("/weather")
def get_weather_city(city: str):
    return get_weather(city)
    
@routes_weather.get("/history")
def get_weather_list():
    return get_weathers()