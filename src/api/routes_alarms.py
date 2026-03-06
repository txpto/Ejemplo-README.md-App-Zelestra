"""Rutas de alarmas."""

from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("")
def list_alarms() -> dict:
    return {
        "items": [
            {
                "asset_name": "CONTADOR_CT_17",
                "severity": "WARNING",
                "message": "Equipo en recuperación de datos",
            }
        ]
    }
