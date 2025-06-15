# Smart Irrigation Backend

This is the backend API for the Smart Irrigation Dashboard. It handles sensor data from ESP32 devices, manages irrigation control, and provides data to the React frontend.

## Features

- Real-time sensor data ingestion
- Time-series data storage with InfluxDB
- MQTT integration for irrigation control
- OpenWeather API integration
- RESTful API endpoints for the frontend

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your configuration:
```env
# API Settings
SECRET_KEY=your-secret-key-here

# InfluxDB
INFLUXDB_URL=http://localhost:8086
INFLUXDB_TOKEN=your-token-here
INFLUXDB_ORG=your-org
INFLUXDB_BUCKET=irrigation

# MQTT
MQTT_BROKER=localhost
MQTT_PORT=1883
MQTT_USERNAME=your-username
MQTT_PASSWORD=your-password

# OpenWeather
OPENWEATHER_API_KEY=your-api-key
OPENWEATHER_LAT=51.5074
OPENWEATHER_LON=-0.1278
```

4. Run the server:
```bash
python run.py
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### Pots
- `GET /api/pots`: List all pots
- `GET /api/pot/{id}`: Get pot details
- `POST /api/pot/{id}/water`: Trigger watering
- `POST /api/pots/data`: Receive pot sensor data

### Environment
- `GET /api/enviro`: Get latest environmental data
- `POST /api/enviro/data`: Receive environmental sensor data

### Weather
- `GET /api/weather`: Get weather data
- `POST /api/weather/data`: Receive weather data

## Development

The project uses:
- FastAPI for the web framework
- InfluxDB for time-series data
- MQTT for real-time communication
- OpenWeather API for weather data

## Testing

To test the API endpoints, you can use the interactive API documentation at `http://localhost:8000/docs`. 
