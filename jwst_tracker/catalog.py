from __future__ import annotations
from pathlib import Path

import pandas as pd

METADATA_DIR = Path(__file__).resolve().parent.parent / "data" / "metadata"
METADATA_DIR.mkdir(parents=True, exist_ok=True)
CATALOG_PATH = METADATA_DIR / "jwst_observations.csv"


def load_catalog() -> pd.DataFrame:
    if CATALOG_PATH.exists():
        return pd.read_csv(CATALOG_PATH)
    return pd.DataFrame()


def update_catalog(new_obs: pd.DataFrame) -> pd.DataFrame:
    """Merge new observations into the on-disk catalog, de-duplicating by obsid."""
    cat = load_catalog()
    if not cat.empty:
        combined = pd.concat([cat, new_obs], ignore_index=True)
        combined = combined.drop_duplicates(subset=["obsid"])
    else:
        combined = new_obs.drop_duplicates(subset=["obsid"])
    combined.to_csv(CATALOG_PATH, index=False)
    return combined
