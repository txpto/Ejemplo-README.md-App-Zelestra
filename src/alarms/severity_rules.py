"""Reglas de severidad de alarmas."""

from __future__ import annotations


def classify_communication_failure(duration_seconds: int) -> str:
    if duration_seconds >= 3600:
        return "CRITICAL"
    if duration_seconds >= 300:
        return "WARNING"
    return "INFO"
