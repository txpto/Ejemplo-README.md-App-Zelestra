"""Servicio de historización."""

from __future__ import annotations

from src.models import SignalReading


class HistorianService:
    """
    Servicio responsable de almacenar lecturas históricas.

    En la aplicación real insertaría datos en una base SQL y aplicaría
    reglas de historización definidas por CSV.
    """

    def __init__(self, config) -> None:
        self.config = config
        self._buffer: list[SignalReading] = []

    def buffer_reading(self, reading: SignalReading) -> None:
        self._buffer.append(reading)

    def flush(self) -> None:
        print(f"[HISTORIAN] Inserción simulada de {len(self._buffer)} lecturas.")
        self._buffer.clear()
