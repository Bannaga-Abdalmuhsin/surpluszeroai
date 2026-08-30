# Prototype and Roadmap

## Hackathon MVP

The MVP demonstrates one complete closed loop in a Surplus Absorption Zone.

### Inputs

- Actual Saudi government energy datasets
- Actual weather observations
- A transparent 15-minute demand profile calibrated to official energy and peak-load values
- Renewable generation estimated from official project capacity and weather
- Measured telemetry from at least one safe demonstration load
- Clearly labelled scenarios for resources not physically available

### Flexible portfolio

- Commercial cooling
- Government-building cooling
- Water pumping
- EV charging
- Battery storage
- Cold storage
- Optional electrolyser

### Required demonstration

1. Predict a surplus interval.
2. Reserve flexibility plus uncertainty.
3. Dispatch multiple asset types.
4. Force one asset to underdeliver.
5. Detect the shortfall from measured data.
6. Reallocate to standby capacity.
7. Report verified absorption and provenance.

## Acceptance criteria

- Government datasets load successfully
- Units and sources are visible
- Forecast and uncertainty are displayed
- Asset constraints affect dispatch
- Manual override works
- Underdelivery is detected
- Shortfall is reallocated
- Only metered response is counted
- No comfort or safety constraint is violated
- Assumed values are clearly labelled

## Delivery phases

### Phase 1 — Documentation and data foundation

Data catalogue, ingestion contracts, provenance model, scenario definition, and baseline methodology.

### Phase 2 — Digital prototype

Forecasting, registry, optimizer, dashboard, and simulated multi-asset dispatch.

### Phase 3 — Physical proof

One metered controllable load and edge gateway demonstrating command, response, verification, and override.

### Phase 4 — Building pilot

Five to ten sites with cooling flexibility, actual interval metering, and verified comfort constraints.

### Phase 5 — Multi-sector pilot

Buildings, water, EV charging, cold storage, and batteries within one geographic zone.

### Phase 6 — Authorized grid integration

Day-ahead and intraday signals, network constraints, secure dispatch, measurement, and settlement.

## Immediate backlog

- Download and validate every official resource file
- Confirm units and sector definitions
- Select pilot region
- Create a normalized data schema
- Choose weather source and project coordinates
- Define 15-minute baseline methodology
- Build initial demand and renewable models
- Define asset API contract
- Implement deterministic optimizer
- Design dashboard wireframes
- Select safe physical demo hardware
- Define cybersecurity and override tests
