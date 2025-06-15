from fastapi import APIRouter, HTTPException
from app.schemas.sensor_data import PotData, PotResponse
from app.db.influx_client import influx_db
from app.mqtt.client import mqtt_client
from typing import List

router = APIRouter()

@router.post("/pots/data")
async def receive_pot_data(data: PotData):
    try:
        influx_db.write_pot_data(data.dict())
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/pots", response_model=List[PotResponse])
async def get_all_pots():
    # In a real application, this would fetch from a database
    # For now, return mock data
    return [
        {
            "id": "1",
            "name": "Pot 1",
            "moisture": 45,
            "temperature": 24,
            "humidity": 65,
            "light": 850,
            "co2": 450,
            "plantType": "Tomato",
            "isWatering": False,
            "lastWatered": "2024-03-10T10:00:00",
            "moistureHistory": [],
            "temperatureHistory": [],
            "settings": {
                "targetMoisture": 60,
                "waterAmount": 500,
                "wateringInterval": 24,
                "maxWateringDuration": 30,
                "moistureThreshold": 40
            }
        }
    ]

@router.get("/pot/{pot_id}", response_model=PotResponse)
async def get_pot(pot_id: str):
    # In a real application, this would fetch from a database
    # For now, return mock data
    return {
        "id": pot_id,
        "name": f"Pot {pot_id}",
        "moisture": 45,
        "temperature": 24,
        "humidity": 65,
        "light": 850,
        "co2": 450,
        "plantType": "Tomato",
        "isWatering": False,
        "lastWatered": "2024-03-10T10:00:00",
        "moistureHistory": influx_db.get_pot_history(pot_id),
        "temperatureHistory": influx_db.get_pot_history(pot_id),
        "settings": {
            "targetMoisture": 60,
            "waterAmount": 500,
            "wateringInterval": 24,
            "maxWateringDuration": 30,
            "moistureThreshold": 40
        }
    }

@router.post("/pot/{pot_id}/water")
async def trigger_watering(pot_id: str, duration_sec: int = 60):
    try:
        mqtt_client.publish_irrigation_command(int(pot_id), "open", duration_sec)
        return {"status": "success", "message": f"Watering triggered for pot {pot_id}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
