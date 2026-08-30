# Concept and Methodology

## Problem statement

As variable renewable generation grows, available generation can exceed the demand, storage, export, or network capability available at a particular time and location. When the energy cannot be absorbed safely, renewable output may be curtailed.

Saudi public datasets establish renewable capacity, electricity consumption, peak load, customer counts, and sector composition, but do not publish operational curtailment history at sub-hourly resolution. SurplusZero therefore addresses a forward-looking operational challenge without inventing a historical national curtailment claim.

## Virtual Energy Reservoir

SurplusZero treats flexible consumption as a portfolio capable of storing or converting energy:

| Resource | Converted value |
|---|---|
| Building pre-cooling | Thermal energy |
| District cooling | Chilled water or ice |
| Water pumping | Stored water |
| EV charging | Mobility |
| Battery | Electrical energy |
| Cold storage | Thermal inventory |
| Industry | Useful production |
| Electrolyser | Hydrogen |

## Operating cycle

1. Ingest official baselines and live/measured inputs.
2. Forecast demand and generation with uncertainty.
3. Identify the surplus window.
4. Request flexibility offers from eligible assets.
5. Reserve capacity above the central forecast.
6. Optimize and dispatch.
7. Measure delivered response.
8. Reallocate shortfall.
9. Settle incentives and publish an auditable result.

## Optimization formulation

For interval `t`, expected surplus is:

```text
S(t) = max(0, G(t) - D(t) - X(t) - B_scheduled(t))
```

Reserve requirement:

```text
sum(R_i(t)) >= S_forecast(t) + U(t)
```

A simplified objective is:

```text
minimize:
  curtailment_cost
  + incentive_cost
  + battery_degradation
  + comfort_deviation
  + network_penalty
  + non_delivery_risk
```

Subject to power, energy, timing, ramp, state-of-charge, comfort, process, network, and availability constraints.

## Baseline and verification

```text
delivered_i(t) = actual_i(t) - baseline_i(t)
shortfall_i(t) = max(0, requested_i(t) - delivered_i(t))
```

Only verified response contributes to the absorption KPI. Baseline methods must be documented and tested to prevent overstating performance.

## Data provenance

All displayed values carry one of these labels:

- **Official**
- **Measured**
- **Calculated**
- **Forecast**
- **Assumed**

## Primary KPIs

```text
absorption_rate = verified_absorbed_energy / available_surplus_energy
delivery_rate   = delivered_energy / committed_energy
```

Additional KPIs include forecast error, response time, reallocation success, comfort violations, overrides, incentive cost, and battery degradation.

## Claim boundary

The target is **near-zero avoidable curtailment**. Absolute zero cannot be guaranteed because faults, congestion, unavailable flexibility, full storage, communication failures, and security requirements may necessitate curtailment.
