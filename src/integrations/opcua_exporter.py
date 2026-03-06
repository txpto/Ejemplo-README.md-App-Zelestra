"""Exportador OPC UA conceptual."""

from __future__ import annotations


class OPCUAExporter:
    """
    Adaptador conceptual para publicar variables a un servidor OPC UA.

    Esta pieza se alinea con la necesidad de exponer datos a centros de control.
    """

    def publish(self, node_id: str, value) -> None:
        print(f"[OPCUA] Publicando {node_id} = {value}")
