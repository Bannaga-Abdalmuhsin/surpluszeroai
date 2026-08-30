# SurplusZero AI

**Kingdom-wide predictive orchestration for near-zero avoidable electricity surplus and curtailment.**

[Open the live national simulator](https://bannaga-abdalmuhsin.github.io/surpluszeroai/)

SurplusZero AI is a grid-support decision and dispatch layer. It predicts where and when electricity supply may exceed demand and network capacity, then coordinates the least-cost feasible response: interregional transfer, safe generation redispatch, storage charging, and productive flexible demand. Curtailment is the last resort.

> Surplus is a grid condition—not “solar electricity assigned to a load.” Utility solar, wind, gas, and other generators inject into the interconnected system. SurplusZero controls eligible resources in the right electrical zone to correct the combined system imbalance.

## The problem

At any interval, a surplus can result from the combined generation fleet, imports, demand changes, exports, storage state, plant constraints, and transmission limits. It is not limited to solar and it may be national or trapped inside a grid zone.

Unmanaged surplus can cause renewable curtailment, inefficient thermal operation, congestion, weaker frequency control, lost zero-fuel-cost energy, and later reliance on more expensive generation. Saudi public data establishes capacity, annual demand, peak load, customers, and sector structure, but does not publish the complete real-time operational series needed to claim measured national surplus.

## The solution

SurplusZero builds a **national flexibility map** and operates a closed loop:

```text
Forecast → Locate → Reserve → Dispatch → Measure → Reallocate
```

For each grid zone and 5–15 minute interval it:

1. forecasts demand and production by source;
2. runs a network-aware balance and identifies probable excess;
3. checks transfer capacity to deficit zones;
4. evaluates safe redispatch of controllable generators;
5. schedules batteries and other storage;
6. activates contracted productive loads such as cooling, water, EV charging, cold storage, industry, and electrolysers;
7. verifies response from meters and reallocates any shortfall; and
8. recommends curtailment only for the residual that cannot be resolved safely.

## Correct system balance

For zone `z` and interval `t`:

```text
initial_excess = max(0,
  generation_all_sources + imports - demand - scheduled_exports
)

residual = max(0,
  initial_excess
  - feasible_transfer
  - feasible_generation_redispatch
  - available_storage_charging
  - verified_flexible_load
)
```

Network constraints, ramp limits, minimum stable generation, reserve obligations, storage state of charge, asset limits, forecast uncertainty, and security rules constrain every action. The result is a recommendation to the authorized system operator—not autonomous control of the national grid.

## Inputs

| Input group | Production source | Prototype status |
|---|---|---|
| Generation by source and plant | System operator/utility telemetry | Interface + scenario assumption |
| Demand by grid zone | SCADA/EMS and smart meters | Official baselines + scenario |
| Imports, exports and tie-line flows | EMS/market data | Interface + scenario assumption |
| Network limits and outages | EMS/network model | Interface + scenario assumption |
| Redispatch capability | Generator offers and plant constraints | Interface + scenario assumption |
| Storage state and charging limits | Storage telemetry | Simulated assets |
| Flexible-load availability | Asset meters and contracts | Simulated registry |
| Weather and renewable forecast | Weather observations/forecast | Actual archived weather in local PoC |
| Annual capacity, peak and consumption | Saudi official open data | Actual published data |

See [solution inputs](docs/solution-inputs.md) and the [official data catalogue](docs/data-sources.md).

## Evidence boundary

- **Official:** published government statistics used for structural calibration.
- **Measured:** pilot meter or participating-asset telemetry.
- **Calculated:** deterministic result derived from declared inputs.
- **Forecast:** model output with uncertainty.
- **Assumed:** transparent scenario value awaiting operational access.

The national dashboard anchors demand to the actual published 2024 Saudi grid peak of **74.8 GW**. Slider-adjusted demand is explicitly modeled from that official value; generation and grid actions remain scenario inputs until synchronized EMS/SCADA data is available. The dashboard is therefore not a claim of live Saudi grid operation. The earlier Riyadh 5 MW solar example remains a local proof that forecasting, dispatch, metering, and shortfall reallocation can work; it is not the scope or national result of SurplusZero.

## Why it is special and doable

The innovation is a verified flexibility exchange across sectors, combined with a grid action waterfall. A command is never counted as success: only metered response is credited, and underdelivery is reassigned automatically. The hackathon prototype can demonstrate the full decision logic using official structural data, actual weather, explicit assumptions, and simulated operational feeds. A production pilot then replaces assumed feeds zone by zone without changing the control workflow.

## Success measures

- residual avoidable curtailment (MWh)
- share of initial excess resolved by each action
- forecast error and uncertainty coverage
- response and reallocation time
- verified delivery rate
- cost per resolved MWh
- constraint and customer-override violations
- emissions and fuel avoided where applicable

## Claim boundary

The goal is **near-zero avoidable surplus/curtailment**, not a guarantee of absolute zero. Faults, congestion, minimum-generation constraints, insufficient flexible capacity, full storage, communications failure, and grid-security requirements can make curtailment necessary.

## Documentation

- [Concept and methodology](docs/methodology.md)
- [System architecture](docs/architecture.md)
- [Solution inputs](docs/solution-inputs.md)
- [Official data catalogue](docs/data-sources.md)
- [Prototype and roadmap](docs/roadmap.md)
- [Run the local Riyadh proof-of-control](docs/running-the-pipeline.md)

## Project status

Hackathon prototype and national digital-twin design. No live national grid connection or measured national saving is claimed.

## License

A license has not yet been selected. Until one is added, standard copyright applies.
