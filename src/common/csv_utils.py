"""Utilidades comunes para lectura de catálogos CSV."""

from __future__ import annotations

from pathlib import Path
import csv


def read_csv_catalog(path: str | Path) -> list[dict]:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Catálogo no encontrado: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))
