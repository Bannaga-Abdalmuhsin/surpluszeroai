# Running the Riyadh Data Pipeline

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e . pytest
surpluszero --config config/riyadh_demo.json --output output/riyadh_demo
pytest
```

The pipeline fetches Ministry of Energy metadata, GASTAT Riyadh seasonal consumption, and actual archived Riyadh weather. It writes 96 fifteen-minute rows to `intervals.csv` and a provenance-aware `manifest.json`.

The configured pilot-zone PV capacity, average demand, and asset portfolio are explicitly **assumed** until replaced by meter and asset-registry data. A detected event is a potential demonstration-zone surplus, not evidence of historical national curtailment.
