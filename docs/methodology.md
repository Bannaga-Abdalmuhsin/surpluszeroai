# Concept and methodology

## System interpretation

SurplusZero manages the combined electricity balance, not the output of one technology. Grid-connected solar has no dedicated destination: its output joins all other injections. The platform therefore observes a national or zonal imbalance and dispatches resources whose electrical location and operating constraints make them useful.

## Detection

For grid zone `z` and interval `t`:

```text
E0(z,t) = max(0, G(z,t) + I(z,t) - D(z,t) - X(z,t))
```

`G` is scheduled/forecast production from every source; `I` and `X` are feasible imports and scheduled exports; `D` is demand. Reserve is not subtracted as consumed energy. Instead, reserve obligations constrain generation schedules and how far a unit may be redispatched.

The engine must solve this across network zones because a Kingdom-wide energy balance can conceal local congestion.

## Action waterfall

The optimizer chooses a secure, least-cost combination rather than blindly applying a fixed order. A transparent operational waterfall for the prototype is:

1. transfer to a connected deficit zone within line limits;
2. reduce controllable generation within ramp, reserve, emissions, and minimum-stable-output limits;
3. charge available storage;
4. increase contracted productive demand;
5. use feasible export opportunity; and
6. curtail the unresolved residual.

```text
E_residual = max(0, E0 - T - R - B - F - X_extra)
```

Here `T` is transfer, `R` is safe redispatch, `B` is storage charging, and `F` is verified flexible load. Each term is capped by physical and contractual availability in that interval.

## Forecast and robustness

Forecasts cover demand, solar, wind, generator availability, and asset response. The system evaluates multiple uncertainty scenarios and reserves enough compatible flexibility for a selected confidence level. It must preserve spinning/contingency reserve and N-1 security; “zero surplus” never overrides system security.

## Productive flexible demand

| Resource | Energy converted or shifted |
|---|---|
| Building/district pre-cooling | Thermal energy |
| Water pumping/desalination | Stored or produced water |
| Cold storage | Thermal inventory |
| EV fleet charging | Mobility |
| Batteries | Electrical energy |
| Flexible industry | Useful output |
| Electrolysers | Hydrogen |

Each resource supplies location, capacity, energy window, ramp time, rebound effect, operational constraints, price, telemetry health, and delivery confidence.

## Verification

```text
delivered_i(t) = max(0, actual_i(t) - approved_baseline_i(t))
shortfall_i(t) = max(0, requested_i(t) - delivered_i(t))
```

Only meter-verified incremental demand or charging is credited. Shortfall is immediately offered to standby assets. Settlement must guard against inflated baselines and double counting.

## Objective

The optimization minimizes expected curtailment, redispatch cost, flexibility incentives, storage degradation, emissions, customer impact, congestion risk, and nondelivery risk, subject to network, plant, reserve, ramp, state-of-charge, comfort, process, and communications constraints.

## Evidence and claim boundary

Official annual data calibrates scale and sector opportunity; it cannot substitute for operational SCADA. The prototype labels official, measured, calculated, forecast, and assumed values separately. The target is near-zero **avoidable** curtailment. Absolute zero cannot be promised.
