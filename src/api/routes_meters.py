"""Rutas de contadores."""

from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("")
def list_meters() -> dict:
    return {
        "items": [
            {"meter_name": "CONTADOR_CT_01", "project": "PSFV_LLERENA"},
            {"meter_name": "CONTADOR_CT_02", "project": "PSFV_LLERENA"},
        ]
    }


@router.get("/{meter_name}/realtime")
def meter_realtime(meter_name: str) -> dict:
    return {
        "meter_name": meter_name,
        "signals": {
            "POWER_ACTIVE_TOTAL": 1248.0,
            "POWER_FACTOR_TOTAL": 0.98,
        },
    }
