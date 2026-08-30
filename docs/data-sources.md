# Official Data Catalogue

This catalogue records the Saudi public datasets used to calibrate SurplusZero AI. It distinguishes annual strategic statistics from operational telemetry. These sources describe the Kingdom's electricity system and flexibility opportunity; none of the reviewed public files alone provides the synchronized 5–15 minute generation, demand, tie-line, constraint, and curtailment data required to calculate a live national surplus.

## National Open Data API

Metadata:

```bash
curl -X GET \
  'https://open.data.gov.sa/data/api/datasets?version=-1&dataset=DATASET_ID' \
  -H 'Accept: application/json'
```

Resources:

```bash
curl -X GET \
  'https://open.data.gov.sa/data/api/datasets/resources?version=-1&dataset=DATASET_ID' \
  -H 'Accept: application/json'
```

## Ministry of Energy datasets

| Dataset | ID | Period/frequency | Verified resource fields | Use |
|---|---|---|---|---|
| Consumer numbers and energy sales | `03b3fed0-d8c5-47e3-bf83-dfa59bc39897` | 2023–2024, yearly | Consumer count; energy sold | Customer baseline, sales intensity, participation scenarios |
| Total electricity users | `eae27e00-386a-4212-9cd6-3087fb42c5e3` | 2017–2024, yearly | Year; user count | Connected-customer growth |
| Electricity consumption by category | `5e4851e8-7af1-4bfb-904f-c03dda024acb` | 2023–2024, yearly | Category; energy sold | Sector opportunity and flexibility sizing |
| Average/percentage customer consumption | `f12628ed-d4cb-49d1-8618-4957dc848c97` | 2023, yearly | Year; consumption | Cross-check average consumption; terminology requires file validation |
| Peak Load | `004003e8-343c-4eee-90bc-71370570dcdd` | 2017–2024, yearly | Year; peak load; unit in 2024 resource | Calibrate maximum national demand; cross-checked 2024 grid peak: 74.8 GW |

Landing pages follow:

```text
https://open.data.gov.sa/ar/datasets/view/{DATASET_ID}
```

### Data-quality note

Some catalogue titles and resource descriptions are inconsistent. For example, historical peak-load resources are labelled as total electricity consumption in some filenames, while their declared columns are year and peak load. SurplusZero validates file contents, units, and definitions before ingestion and preserves the original source metadata.

## GASTAT

### Renewable Energy Statistics 2024

Source: https://www.stats.gov.sa/documents/d/guest/renewable-energy-statistics-2024-en-1-pdf

Verified headline baseline at end-2024:

- Operating renewable capacity: 6,551 MW
- Solar: 6,151 MW
- Wind: 400 MW
- Ten commissioned projects: nine solar and one wind

Use: renewable project capacity, technology, commissioning, and LCOE baseline.

### Regional seasonal household consumption

API:

```text
https://api.stats.gov.sa/v1/stats/DPV_HES_EHE_IT_HES0303
```

Verified fields:

- `REGION_ENGL`
- `YEAR_TIME`
- `CONSUMP_OPERATION_PERIOD_ENGL`
- `OBSVALUE_OBSV`

Use: regional and seasonal demand calibration.

Additional relevant GASTAT APIs:

- Household solar use: `DPV_HES_EHE_IT_HES0501`
- Energy-saving devices by region: `DPV_HES_EHE_IT_HES0602`

## SERA

- Open data: https://www.sera.gov.sa/en/knowledge-center/data-management-office/data-management-office-categories/open-data
- Licensed capacity by region: https://sera.gov.sa/en/knowledge-center/data-and-statistics/data-and-statistics-categories/data-and-information/licensed-capacity-by-region-and-year
- Consumption tariffs: https://sera.gov.sa/en/consumer/electric-tariff/electric-tariff-categories/consumption-tariff

Use: regional capacity constraints and customer economic calculations.

## Missing operational data

The reviewed open datasets do not provide:

- 5-, 15-, or 60-minute system demand
- Plant-level actual renewable generation
- Curtailment instructions or events
- Day-ahead grid demand and renewable forecasts
- Regional network congestion
- Live import/export capability
- Battery state of charge
- Registered flexible-load availability

The prototype therefore uses official data for calibration, actual weather for time-varying renewable estimates, and measured pilot telemetry for flexibility verification. Production deployment would replace scenario grid signals with authorized operational feeds.
