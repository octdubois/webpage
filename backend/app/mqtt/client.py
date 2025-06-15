import paho.mqtt.client as mqtt
from app.core.config import settings
import json
from typing import Dict, Any

class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client()
        if settings.MQTT_USERNAME and settings.MQTT_PASSWORD:
            self.client.username_pw_set(settings.MQTT_USERNAME, settings.MQTT_PASSWORD)
        
        self.client.connect(settings.MQTT_BROKER, settings.MQTT_PORT)
        self.client.loop_start()

    def publish_irrigation_command(self, valve_id: int, action: str, duration_sec: int):
        payload = {
            "valve_id": valve_id,
            "action": action,
            "duration_sec": duration_sec
        }
        self.client.publish("irrigation/command", json.dumps(payload))

    def close(self):
        self.client.loop_stop()
        self.client.disconnect()

mqtt_client = MQTTClient() 
