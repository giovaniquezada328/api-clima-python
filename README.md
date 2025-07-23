# 🌤️ Clima App

Aplicación que muestra el clima actual por ciudad, usando Angular (Frontend) y Python FastAPI en AWS Lambda (Backend).

## Funcionalidades
- Buscar clima por ciudad (OpenWeatherMap)
- Mostrar temperatura, humedad, viento, condición
- Historial de ciudades buscadas
- Almacenamiento en AWS DynamoDB

## Tecnologías
- Angular 19 Standalone
- Python FastAPI
- AWS Lambda, API Gateway, S3, DynamoDB

## Deploy
- Frontend: S3
- Backend: Lambda con API Gateway
- DB: DynamoDB

## Cómo correr localmente

### Frontend
```bash
ng serve
