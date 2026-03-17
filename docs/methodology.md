# Methodology

This document describes the scientific and technical design of the JWST Data Tracker.

- Data source: MAST JWST archive queried via astroquery.mast.Observations.
- Scope: metadata-only catalog of public JWST observations for selected programs or targets.
- Pipeline: query -> normalize metadata -> update local catalog -> optional product download -> plotting.

The goal is to provide a reproducible, scripted workflow that can be extended for specific science cases.
