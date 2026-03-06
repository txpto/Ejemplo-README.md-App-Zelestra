"""Adaptador conceptual para integración con ROC."""

from __future__ import annotations


class ROCAdapter:
    """
    Adaptador para enviar datos consolidados al centro de control.

    En una implementación real incorporaría:
    - validación de payloads
    - control de errores
    - reintentos
    - trazabilidad
    """

    def send_snapshot(self, payload: dict) -> None:
        print(f"[ROC] Envío de snapshot con {len(payload)} claves.")
