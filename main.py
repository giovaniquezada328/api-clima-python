from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from database.db import create_tables
from routes.weather import routes_weather
app = FastAPI()

# cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # 👈 O usa ["http://localhost:4200"] para mayor seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_weather)

create_tables()

handler = Mangum(app)

# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('WeatherHistory')

# API_KEY = os.environ.get("WEATHER_API_KEY", "8ed7388f2b0ef9633740d639c588a17a")

# @app.get("/weather")
# def get_weather(city: str):
#     try:
#         res = requests.get(
#             f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
#         data = res.json()
#         if res.status_code != 200:
#             raise HTTPException(status_code=404, detail="Ciudad no encontrada")
#         return data
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/history")
# def get_history():
#     response = table.scan()
#     cities = [item['city'] for item in response.get('Items', [])]
#     return cities[::-1]

# @app.post("/history")
# def post_history(request: Request):
#     body = request.json()
#     city = body.get("city")
#     if city:
#         table.put_item(Item={"city": city})
#         return {"message": "Guardado"}
#     raise HTTPException(status_code=400, detail="Ciudad requerida")
