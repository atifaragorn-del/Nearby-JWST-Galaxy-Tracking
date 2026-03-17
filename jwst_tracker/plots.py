from __future__ import annotations
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from .catalog import load_catalog

FIG_DIR = Path(__file__).resolve().parent.parent / "reports" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def plot_counts_by_instrument():
    df = load_catalog()
    if df.empty:
        print("Catalog is empty; run an update first.")
        return
    counts = df["instrument_name"].value_counts()
    fig, ax = plt.subplots(figsize=(6, 4))
    counts.plot(kind="bar", ax=ax)
    ax.set_xlabel("Instrument")
    ax.set_ylabel("Number of observations")
    ax.set_title("JWST observations by instrument")
    fig.tight_layout()
    out = FIG_DIR / "counts_by_instrument.png"
    fig.savefig(out)
    plt.close(fig)
    print(f"Saved {out}")
