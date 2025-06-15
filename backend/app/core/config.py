from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "Smart Irrigation API"
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # InfluxDB
    INFLUXDB_URL: str = os.getenv("INFLUXDB_URL", "http://localhost:8086")
    INFLUXDB_TOKEN: str = os.getenv("INFLUXDB_TOKEN", "your-token-here")
    INFLUXDB_ORG: str = os.getenv("INFLUXDB_ORG", "your-org")
    INFLUXDB_BUCKET: str = os.getenv("INFLUXDB_BUCKET", "irrigation")
    
    # MQTT
    MQTT_BROKER: str = os.getenv("MQTT_BROKER", "localhost")
    MQTT_PORT: int = int(os.getenv("MQTT_PORT", "1883"))
    MQTT_USERNAME: Optional[str] = os.getenv("MQTT_USERNAME")
    MQTT_PASSWORD: Optional[str] = os.getenv("MQTT_PASSWORD")
    
    # OpenWeather
    OPENWEATHER_API_KEY: str = os.getenv("OPENWEATHER_API_KEY", "your-api-key")
    OPENWEATHER_LAT: float = float(os.getenv("OPENWEATHER_LAT", "51.5074"))
    OPENWEATHER_LON: float = float(os.getenv("OPENWEATHER_LON", "-0.1278"))

settings = Settings() 
