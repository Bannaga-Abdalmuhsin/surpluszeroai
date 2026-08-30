# Running the Riyadh Data Pipeline

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e . pytest
surpluszero --config config/riyadh_demo.json --output output/riyadh_demo
pytest
```

The pipeline fetches Ministry of Energy metadata, GASTAT Riyadh seasonal consumption, and actual archived Riyadh weather. It writes 96 fifteen-minute rows to `intervals.csv`, asset instructions to `dispatch.csv`, and a provenance-aware `manifest.json`.

The demonstration intentionally configures one cooling asset to deliver only 75% of its initial commitment. The closed loop detects that shortfall and reallocates it. Only delivered response is included in the absorption KPI.

The configured pilot-zone PV capacity, average demand, and asset portfolio are explicitly **assumed** until replaced by meter and asset-registry data. A detected event is a potential demonstration-zone surplus, not evidence of historical national curtailment.
