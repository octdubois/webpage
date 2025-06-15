from fastapi import APIRouter, HTTPException
from app.schemas.sensor_data import EnviroData
from app.db.influx_client import influx_db

router = APIRouter()

@router.post("/enviro/data")
async def receive_enviro_data(data: EnviroData):
    try:
        influx_db.write_enviro_data(data.dict())
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/enviro")
async def get_latest_enviro_data():
    # In a real application, this would fetch from InfluxDB
    # For now, return mock data
    return {
        "device_id": "enviro1",
        "bme280": {
            "temp": 24.7,
            "hum": 48.3,
            "pres": 1008.2
        },
        "lux_tsl2591": 15000.3,
        "dht22": {
            "temp": 25.0,
            "hum": 51.2
        }
    } 
