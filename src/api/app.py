"""API conceptual de integración."""

from __future__ import annotations

from fastapi import FastAPI
from src.api.routes_health import router as health_router
from src.api.routes_meters import router as meters_router
from src.api.routes_alarms import router as alarms_router

app = FastAPI(
    title="Solar Plant Monitoring Platform",
    version="1.0.0",
    description="API de ejemplo para monitorización energética de plantas fotovoltaicas.",
)

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(meters_router, prefix="/meters", tags=["meters"])
app.include_router(alarms_router, prefix="/alarms", tags=["alarms"])
