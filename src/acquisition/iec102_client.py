"""Cliente IEC60870-5-102 simplificado."""

from __future__ import annotations


class IEC102Client:
    """
    Cliente conceptual para adquisición de datos desde contadores IEC102.

    En una implementación real, este módulo se encargaría de:
    - establecer conexión TCP con el contador
    - negociar el protocolo IEC102
    - solicitar valores instantáneos
    - consultar históricos para backfill
    """

    def __init__(self, ip_address: str, tcp_port: int, link_address: str) -> None:
        self.ip_address = ip_address
        self.tcp_port = tcp_port
        self.link_address = link_address

    def connect(self) -> None:
        print(
            f"[IEC102] Conectando a {self.ip_address}:{self.tcp_port} "
            f"(link_address={self.link_address})"
        )

    def read_instant_values(self) -> dict[str, float]:
        """
        Devuelve lecturas instantáneas de ejemplo.

        En el sistema real deberían leerse, entre otras:
        - energía importada/exportada
        - tensiones por fase
        - corrientes por fase
        - potencias y factor de potencia
        """
        return {
            "ACTIVE_IMPORTED_KWH": 125034.0,
            "VOLTAGE_PHASE_1": 230.1,
            "CURRENT_PHASE_1": 186.2,
            "POWER_ACTIVE_TOTAL": 1248.0,
            "POWER_FACTOR_TOTAL": 0.98,
        }
