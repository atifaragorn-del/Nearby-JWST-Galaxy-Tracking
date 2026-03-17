from __future__ import annotations
from typing import Iterable, Optional

import pandas as pd
from astroquery.mast import Observations


def query_by_program(program_id: str) -> pd.DataFrame:
    """Return an observations table for a given JWST program ID."""
    obs = Observations.query_criteria(proposal_id=program_id, obs_collection=["JWST"])
    return obs.to_pandas()


def query_by_target(object_name: str, radius: str = "0.1 deg") -> pd.DataFrame:
    """Return observations around a target name."""
    obs = Observations.query_criteria(objectname=object_name, radius=radius, obs_collection=["JWST"])
    return obs.to_pandas()


def get_products(obs_table: pd.DataFrame, product_substrings: Optional[Iterable[str]] = None) -> pd.DataFrame:
    """Get product list for given observations, optionally filter by filename substrings."""
    table = Observations.get_product_list(obs_table)
    df = table.to_pandas()
    if product_substrings:
        mask = False
        for s in product_substrings:
            mask |= df["productFilename"].str.contains(s)
        df = df[mask]
    return df
