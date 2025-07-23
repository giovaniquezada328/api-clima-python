from fastapi import HTTPException
import requests

from models.weather import Weather
from .db import dynamodb
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from boto3.dynamodb.conditions import Key
import os


table = dynamodb.Table("weather_history")
API_KEY = os.environ.get("WEATHER_API_KEY", "8ed7388f2b0ef9633740d639c588a17a")

def create_weather(weather: dict):
    try:
        table.put_item(Item=weather)
        return weather
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)
    

def get_weather(city: str):
    try:
        res = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
        data = res.json()
        if res.status_code != 200:
            raise HTTPException(status_code=404, detail="Ciudad no encontrada")
        
        weather = Weather(city=city) 
        table.put_item(Item=weather.dict())
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_weathers():
    try:
        response = table.scan(
            Limit=10,
            AttributesToGet=["city", "id"]
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)