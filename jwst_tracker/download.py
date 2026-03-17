from __future__ import annotations
from pathlib import Path

from astroquery.mast import Observations

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def download_products(products_table) -> str:
    """Download products using astroquery; returns manifest path."""
    manifest = Observations.download_products(products_table, download_dir=str(DATA_DIR))
    return str(manifest)
