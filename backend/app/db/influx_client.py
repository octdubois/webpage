from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from app.core.config import settings
from datetime import datetime, timedelta
from typing import List, Dict, Any

class InfluxDB:
    def __init__(self):
        self.client = InfluxDBClient(
            url=settings.INFLUXDB_URL,
            token=settings.INFLUXDB_TOKEN,
            org=settings.INFLUXDB_ORG
        )
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.query_api = self.client.query_api()
        self.bucket = settings.INFLUXDB_BUCKET

    def write_pot_data(self, data: Dict[str, Any]):
        point = Point("pot_data") \
            .tag("device_id", data["device_id"]) \
            .field("moisture", data["moisture"][0]) \
            .field("temperature", data["temp"][0]) \
            .time(datetime.fromtimestamp(data["ts"]))
        
        self.write_api.write(bucket=self.bucket, record=point)

    def write_irrigation_event(self, data: Dict[str, Any]):
        if "irrigation_event" in data:
            event = data["irrigation_event"]
            point = Point("irrigation_event") \
                .tag("device_id", data["device_id"]) \
                .tag("valve_id", str(event["valve_id"])) \
                .field("status", event["status"]) \
                .field("target_litres", event["target_litres"]) \
                .field("actual_litres", event["actual_litres"]) \
                .field("pwm", event["pwm"]) \
                .field("duration_sec", event["duration_sec"]) \
                .time(datetime.fromtimestamp(data["ts"]))
            
            self.write_api.write(bucket=self.bucket, record=point)

    def write_enviro_data(self, data: Dict[str, Any]):
        point = Point("enviro_data") \
            .tag("device_id", data["device_id"]) \
            .field("bme280_temp", data["bme280"]["temp"]) \
            .field("bme280_hum", data["bme280"]["hum"]) \
            .field("bme280_pres", data["bme280"]["pres"]) \
            .field("lux", data["lux_tsl2591"]) \
            .field("dht22_temp", data["dht22"]["temp"]) \
            .field("dht22_hum", data["dht22"]["hum"]) \
            .time(datetime.fromtimestamp(data["ts"]))
        
        self.write_api.write(bucket=self.bucket, record=point)

    def write_weather_data(self, data: Dict[str, Any]):
        point = Point("weather_data") \
            .field("temp", data["weather_out"]["temp"]) \
            .field("humidity", data["weather_out"]["humidity"]) \
            .field("pressure", data["weather_out"]["pressure"]) \
            .field("clouds", data["weather_out"]["clouds"]) \
            .field("rain_1h", data["weather_out"]["rain_1h"]) \
            .field("rain_3h", data["weather_out"]["rain_3h"]) \
            .field("wind_speed", data["weather_out"]["wind_speed"]) \
            .field("wind_deg", data["weather_out"]["wind_deg"]) \
            .time(datetime.fromtimestamp(data["ts"]))
        
        self.write_api.write(bucket=self.bucket, record=point)

    def get_pot_history(self, device_id: str, hours: int = 24) -> List[Dict[str, Any]]:
        start_time = datetime.now() - timedelta(hours=hours)
        query = f'''
            from(bucket: "{self.bucket}")
                |> range(start: {start_time.isoformat()})
                |> filter(fn: (r) => r["_measurement"] == "pot_data")
                |> filter(fn: (r) => r["device_id"] == "{device_id}")
                |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
        '''
        
        result = self.query_api.query(query)
        return [{
            "timestamp": record.get_time().isoformat(),
            "moisture": record.get_value(),
            "temperature": record.get_value()
        } for table in result for record in table.records]

    def close(self):
        self.client.close()

influx_db = InfluxDB() 
