from fastapi import APIRouter, HTTPException
from app.schemas.sensor_data import WeatherData
from app.db.influx_client import influx_db
import requests
from app.core.config import settings

router = APIRouter()

@router.post("/weather/data")
async def receive_weather_data(data: WeatherData):
    try:
        influx_db.write_weather_data(data.dict())
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/weather")
async def get_weather_data():
    try:
        # Fetch weather data from OpenWeather API
        url = f"https://api.openweathermap.org/data/2.5/weather"
        params = {
            "lat": settings.OPENWEATHER_LAT,
            "lon": settings.OPENWEATHER_LON,
            "appid": settings.OPENWEATHER_API_KEY,
            "units": "metric"
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "clouds": data["clouds"]["all"],
            "desc": data["weather"][0]["description"],
            "rain_1h": data.get("rain", {}).get("1h", 0),
            "rain_3h": data.get("rain", {}).get("3h", 0),
            "wind_speed": data["wind"]["speed"],
            "wind_deg": data["wind"]["deg"],
            "sunrise": data["sys"]["sunrise"],
            "sunset": data["sys"]["sunset"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
