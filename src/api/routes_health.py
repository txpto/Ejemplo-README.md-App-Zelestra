"""Rutas de salud del sistema."""

from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("")
def health() -> dict:
    return {"status": "ok", "service": "solar-monitoring-platform"}
