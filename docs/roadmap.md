# Prototype and roadmap

## Hackathon MVP

The MVP demonstrates a four-zone Kingdom digital twin plus one physical or simulated asset-control loop. It does not require access to live national control systems.

1. Load official Saudi capacity, peak, consumption, and sector baselines.
2. Create transparent 15-minute zonal demand and all-source generation scenarios.
3. Detect a constrained zonal excess.
4. allocate transfer, safe redispatch, storage, and productive flexible demand;
5. deliberately underdeliver one flexible-load command;
6. detect and reallocate the shortfall; and
7. display residual curtailment and provenance.

## Acceptance criteria

- all generation sources enter one balance;
- the national aggregate and zonal constraints are both visible;
- no action exceeds its physical availability;
- reserve and minimum-generation constraints are preserved;
- assumptions cannot appear as measurements;
- only meter-verified flexible response is credited;
- underdelivery is detected and reassigned;
- manual override and safety constraints work; and
- absolute zero is never promised when a residual remains.

## Delivery phases

| Phase | Deliverable |
|---|---|
| 1. National digital twin | Data contracts, four-zone scenario, waterfall engine, dashboard |
| 2. Metered local proof | One safe load, gateway, baseline, command, verification, override |
| 3. Zone pilot | 5–10 sites plus storage and utility-provided zonal signal |
| 4. Multi-sector pilot | Cooling, water, EVs, cold storage, batteries, industry |
| 5. Operator sandbox | Historical/replayed EMS inputs and security-constrained validation |
| 6. Authorized integration | Advisory deployment, then controlled dispatch under grid governance |

## Immediate backlog

- validate and version every official resource file;
- obtain representative 5–15 minute anonymized load/generation traces;
- define four electrical zones and transfer constraints with an operator partner;
- specify generator redispatch and reserve data contracts;
- implement probabilistic forecasts and a security-constrained optimizer;
- connect one metered asset and test shortfall reallocation;
- quantify business value per resolved MWh; and
- complete cybersecurity, fail-safe, and governance tests.
