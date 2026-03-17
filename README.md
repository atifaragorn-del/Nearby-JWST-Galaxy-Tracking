# JWST Data Tracker

Automated pipeline to discover, catalog, and download JWST observations from MAST, with summary analysis notebooks and plots.

## Features
- Query JWST observations from MAST by program ID or target name.
- Maintain a local metadata catalog (CSV) of observations.
- Download selected data products.
- Generate basic summary plots (counts by instrument, filter, date).

## Quick start
```bash
pip install -e .

jwst-tracker update --program 2733
jwst-tracker make-plots
```

See `docs/methodology.md` for the scientific and technical details.
