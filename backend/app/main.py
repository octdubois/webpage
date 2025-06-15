from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import pots, irrigation, enviro, weather
from app.core.config import settings

app = FastAPI(title="Smart Irrigation API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(pots.router, prefix="/api", tags=["pots"])
app.include_router(irrigation.router, prefix="/api", tags=["irrigation"])
app.include_router(enviro.router, prefix="/api", tags=["environment"])
app.include_router(weather.router, prefix="/api", tags=["weather"])

@app.get("/")
async def root():
    return {"message": "Smart Irrigation API"} 
