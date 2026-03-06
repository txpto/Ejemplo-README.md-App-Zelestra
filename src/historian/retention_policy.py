"""Políticas de retención de datos históricos."""

from __future__ import annotations


class RetentionPolicy:
    """Define reglas de retención y archivado de datos."""

    def __init__(self, retention_days: int) -> None:
        self.retention_days = retention_days

    def describe(self) -> str:
        return f"Retención configurada: {self.retention_days} días"
