"""Carga y validación de configuración externa."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv
import yaml


@dataclass
class RuntimeConfig:
    """Configuración consolidada cargada desde YAML y CSV."""

    system_path: Path
    meters_catalog_path: Path
    meter_historization_path: Path
    meteo_catalog_path: Path
    polling_seconds_default: int
    reconnect_seconds: int
    projects: list[str]


def _read_yaml(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo YAML: {path}")
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _read_csv(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo CSV: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def load_runtime_config(base_dir: str | Path = "config") -> RuntimeConfig:
    """
    Carga la configuración principal del sistema.

    La filosofía del proyecto es que la ampliación estándar del sistema
    se realice mediante configuración, sin reprogramar código.
    """
    base_dir = Path(base_dir)
    system_path = base_dir / "system.yaml"

    data = _read_yaml(system_path)
    projects_block = data.get("projects", {})

    meters_catalog_path = Path(projects_block.get("meters_file", "config/catalogs/meters.csv"))
    meter_historization_path = Path(
        projects_block.get("meter_historization_file", "config/catalogs/meter_historization.csv")
    )
    meteo_catalog_path = Path(
        projects_block.get("meteo_stations_file", "config/catalogs/meteo_stations.csv")
    )

    meters = _read_csv(meters_catalog_path)
    meteo = _read_csv(meteo_catalog_path)

    projects = sorted(
        {
            row.get("psfv_project", "").strip()
            for row in [*meters, *meteo]
            if row.get("psfv_project", "").strip()
        }
    )

    acquisition = data.get("acquisition", {})
    return RuntimeConfig(
        system_path=system_path,
        meters_catalog_path=meters_catalog_path,
        meter_historization_path=meter_historization_path,
        meteo_catalog_path=meteo_catalog_path,
        polling_seconds_default=int(acquisition.get("polling_seconds_default", 5)),
        reconnect_seconds=int(acquisition.get("reconnect_seconds", 30)),
        projects=projects,
    )
