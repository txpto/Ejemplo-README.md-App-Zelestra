"""Eventos de comunicación."""

from __future__ import annotations


def offline_message(asset_name: str) -> str:
    return f"Equipo sin comunicación: {asset_name}"


def recovering_message(asset_name: str) -> str:
    return f"Equipo en recuperación de datos: {asset_name}"
