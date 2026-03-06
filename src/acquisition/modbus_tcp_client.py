"""Cliente Modbus TCP simplificado para estaciones meteorológicas."""

from __future__ import annotations


class ModbusTCPClient:
    """
    Cliente conceptual para lectura de estaciones meteorológicas.

    Este módulo está pensado para crecer por configuración, no por recodificación.
    """

    def __init__(self, ip_address: str, tcp_port: int) -> None:
        self.ip_address = ip_address
        self.tcp_port = tcp_port

    def connect(self) -> None:
        print(f"[MODBUS] Conectando a {self.ip_address}:{self.tcp_port}")

    def read_registers(self) -> dict[str, float]:
        return {
            "AMBIENT_TEMPERATURE": 28.4,
            "IRRADIANCE": 874.0,
            "WIND_SPEED": 4.2,
        }
