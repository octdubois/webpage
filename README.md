# Smart Irrigation Deployment

This repository contains the backend API extracted from `irrigation-dashboard.zip`
and a Node-RED flow for communicating with ESP devices.

Use `docker-compose` to run the backend, Node-RED, MQTT and InfluxDB services.

## Getting Started

1. **Unzip the full project** (if you need the React frontend):
   ```bash
   unzip irrigation-dashboard.zip -d irrigation-dashboard
   ```
   The backend used by Docker Compose is already available in the `backend/` directory.

2. **Create a `.env` file** under `backend/` following the variables documented in
   `backend/README.md`.

3. **Start everything**:
   ```bash
   docker-compose up --build
   ```
   - Backend API: <http://localhost:8000>
   - Node-RED editor: <http://localhost:1880>

The Node-RED flow (`node-red/flows.json`) subscribes to MQTT topics for sensor
updates and forwards them to the backend API. It also exposes an HTTP endpoint
`/irrigate/:id` to publish irrigation commands to the MQTT broker.
