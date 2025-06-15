from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class IrrigationEvent(BaseModel):
    status: str
    valve_id: int
    target_litres: float
    actual_litres: float
    pwm: int
    duration_sec: int

class PotData(BaseModel):
    device_id: str
    ts: int
    uptime_sec: int
    interval_sec: int
    moisture: List[int]
    temp: List[float]

class IrrigationData(PotData):
    irrigation_event: Optional[IrrigationEvent] = None

class BME280Data(BaseModel):
    temp: float
    hum: float
    pres: float

class DHT22Data(BaseModel):
    temp: float
    hum: float

class EnviroData(BaseModel):
    device_id: str
    ts: int
    uptime_sec: int
    bme280: BME280Data
    lux_tsl2591: float
    dht22: DHT22Data

class WeatherData(BaseModel):
    ts: int
    weather_out: dict

class PotResponse(BaseModel):
    id: str
    name: str
    moisture: float
    temperature: float
    humidity: float
    light: float
    co2: float
    plantType: str
    isWatering: bool
    lastWatered: str
    moistureHistory: List[dict]
    temperatureHistory: List[dict]
    settings: dict 
