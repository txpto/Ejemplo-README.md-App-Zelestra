"""Servicio conceptual de recuperación de huecos históricos."""

from __future__ import annotations


class BackfillService:
    """
    Gestiona la recuperación de datos faltantes.

    Filosofía de funcionamiento:
    - detecta huecos
    - solicita históricos al contador tras reconexión
    - rellena primero los huecos más antiguos
    """

    def detect_gaps(self, asset_name: str) -> list[dict]:
        print(f"[BACKFILL] Analizando huecos para {asset_name}")
        return []

    def backfill_left_to_right(self, asset_name: str) -> None:
        print(f"[BACKFILL] Recuperación por la izquierda para {asset_name}")
