"""Gestor del ciclo de adquisición."""

from __future__ import annotations

from datetime import datetime, timezone

from src.common.csv_utils import read_csv_catalog
from src.acquisition.iec102_client import IEC102Client
from src.acquisition.modbus_tcp_client import ModbusTCPClient
from src.models import SignalReading


class PollingManager:
    """
    Orquesta la adquisición desde múltiples equipos.

    La lista de equipos se obtiene de catálogos CSV, permitiendo crecimiento
    sin modificar código fuente.
    """

    def __init__(self, config, historian, alarm_engine) -> None:
        self.config = config
        self.historian = historian
        self.alarm_engine = alarm_engine

    def describe_startup(self) -> None:
        meters = read_csv_catalog(self.config.meters_catalog_path)
        meteo = read_csv_catalog(self.config.meteo_catalog_path)

        print(f"[POLLING] Contadores configurados: {len(meters)}")
        print(f"[POLLING] Estaciones meteorológicas configuradas: {len(meteo)}")
        print(f"[POLLING] Polling por defecto: {self.config.polling_seconds_default} s")

    def poll_once(self) -> None:
        """
        Realiza un ciclo de adquisición de ejemplo.

        Se deja como referencia estructural para el repositorio.
        """
        now = datetime.now(timezone.utc)
        for meter in read_csv_catalog(self.config.meters_catalog_path):
            if meter.get("enabled", "").lower() != "true":
                continue

            client = IEC102Client(
                ip_address=meter["ip_address"],
                tcp_port=int(meter["tcp_port"]),
                link_address=meter["link_address"],
            )
            client.connect()
            values = client.read_instant_values()

            for signal_name, value in values.items():
                reading = SignalReading(
                    asset_name=meter["meter_name"],
                    signal_name=signal_name,
                    value=float(value),
                    timestamp_utc=now,
                    quality="GOOD",
                    source_protocol="IEC102",
                )
                self.historian.buffer_reading(reading)

        for station in read_csv_catalog(self.config.meteo_catalog_path):
            if station.get("enabled", "").lower() != "true":
                continue

            client = ModbusTCPClient(
                ip_address=station["ip_address"],
                tcp_port=int(station["tcp_port"]),
            )
            client.connect()
            values = client.read_registers()

            for signal_name, value in values.items():
                reading = SignalReading(
                    asset_name=station["station_name"],
                    signal_name=signal_name,
                    value=float(value),
                    timestamp_utc=now,
                    quality="GOOD",
                    source_protocol="MODBUS_TCP",
                )
                self.historian.buffer_reading(reading)

        self.historian.flush()
