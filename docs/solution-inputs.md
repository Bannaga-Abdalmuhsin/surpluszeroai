# Solution inputs

SurplusZero needs two distinct layers of data. Public open data makes the national case credible and calibrates the model. Operational data makes real dispatch possible.

## Minimum viable operational inputs

| Input | Resolution | Why it is needed | Prototype fallback |
|---|---:|---|---|
| Generation by source and grid zone | 5–15 min | Total injections and forecast error | Transparent scenario calibrated to official totals |
| Demand by grid zone | 5–15 min | Detect current/forecast imbalance | Modeled shape anchored to the actual 2024 grid peak of 74,800 MW |
| Interconnector and corridor flows/limits | 5–15 min | Determine whether excess can move | Assumed zonal transfer limits |
| Unit ramp and minimum stable output | Event/current | Bound safe redispatch | Representative plant constraints |
| Required operating reserves | 5–15 min | Preserve system security | Explicit reserve constraint |
| Storage state of charge and limits | 1–5 min | Know charge headroom | Simulated telemetry |
| Flexible asset offers and constraints | 1–15 min | Build dispatchable portfolio | Registered demo assets |
| Asset meter readings | 1 min preferred | Verify delivery and settle | Hardware meter or simulated meter |
| Weather and renewable forecasts | Hourly input, 5–15 min output | Predict variable production | Archived observed weather |
| Outages and network topology | Event/current | Prevent infeasible dispatch | Scenario contingencies |

## Official open-data role

Saudi Ministry of Energy, SERA, GASTAT, and the National Open Data Portal datasets can support installed capacity and generation mix, renewable capacity, peak-load calibration, annual/seasonal consumption, customer and sector segmentation, tariff assumptions, and geographic prioritization of flexible-load recruitment.

They cannot, on their own, prove a particular 15-minute national surplus event or avoided curtailment. Those claims require operator telemetry and meter evidence.

## Data contract

Every value should carry `timestamp`, `zone_id`, `unit`, `source`, `provenance`, `quality_flag`, and `received_at`. Forecasts also carry `forecast_created_at`, `horizon`, and uncertainty bounds. This prevents annual official statistics, forecasts, assumptions, and measurements from being mixed in one KPI.
