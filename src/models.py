"""Modelos de dominio simplificados de la aplicación."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Meter:
    link_address: str
    measurement_point: str
    ip_address: str
    tcp_port: int
    meter_name: str
    physical_location: str
    psfv_project: str
    enabled: bool = True


@dataclass
class MeteoStation:
    ip_address: str
    tcp_port: int
    station_name: str
    physical_location: str
    psfv_project: str
    enabled: bool = True


@dataclass
class SignalReading:
    asset_name: str
    signal_name: str
    value: float
    timestamp_utc: datetime
    quality: str = "GOOD"
    source_protocol: Optional[str] = None


@dataclass
class AlarmEvent:
    asset_name: str
    severity: str
    message: str
    timestamp_utc: datetime
    code: Optional[str] = None
