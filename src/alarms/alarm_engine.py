"""Motor básico de alarmas."""

from __future__ import annotations

from datetime import datetime, timezone

from src.models import AlarmEvent


class AlarmEngine:
    """
    Motor de alarmas simplificado.

    Debe detectar, entre otros:
    - pérdida de comunicación
    - recuperación en curso
    - estados degradados
    """

    def __init__(self, config) -> None:
        self.config = config

    def emit(self, asset_name: str, severity: str, message: str) -> AlarmEvent:
        event = AlarmEvent(
            asset_name=asset_name,
            severity=severity,
            message=message,
            timestamp_utc=datetime.now(timezone.utc),
        )
        print(f"[ALARM] {event.severity} | {event.asset_name} | {event.message}")
        return event
