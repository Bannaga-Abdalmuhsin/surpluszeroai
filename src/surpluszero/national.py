"""Network-zone balance and response waterfall for the national concept model."""

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class ZoneState:
    zone_id: str
    generation_mw: dict[str, float]
    demand_mw: float
    imports_mw: float = 0.0
    scheduled_exports_mw: float = 0.0
    transfer_headroom_mw: float = 0.0
    deficit_elsewhere_mw: float = 0.0
    redispatch_available_mw: float = 0.0
    storage_charge_available_mw: float = 0.0
    flexible_load_available_mw: float = 0.0
    extra_export_available_mw: float = 0.0


@dataclass(frozen=True)
class BalanceResult:
    zone_id: str
    generation_mw: float
    initial_excess_mw: float
    transfer_mw: float
    redispatch_mw: float
    storage_mw: float
    flexible_load_mw: float
    extra_export_mw: float
    residual_curtailment_mw: float


def _take(remaining: float, available: float) -> tuple[float, float]:
    used = min(max(0.0, remaining), max(0.0, available))
    return used, remaining - used


def balance_zone(state: ZoneState) -> BalanceResult:
    """Apply the transparent prototype waterfall to one grid-zone interval."""
    generation = sum(max(0.0, value) for value in state.generation_mw.values())
    excess = max(
        0.0,
        generation + state.imports_mw - state.demand_mw - state.scheduled_exports_mw,
    )
    remaining = excess
    transfer, remaining = _take(
        remaining, min(state.transfer_headroom_mw, state.deficit_elsewhere_mw)
    )
    redispatch, remaining = _take(remaining, state.redispatch_available_mw)
    storage, remaining = _take(remaining, state.storage_charge_available_mw)
    flexible, remaining = _take(remaining, state.flexible_load_available_mw)
    extra_export, remaining = _take(remaining, state.extra_export_available_mw)
    return BalanceResult(
        zone_id=state.zone_id,
        generation_mw=round(generation, 3),
        initial_excess_mw=round(excess, 3),
        transfer_mw=round(transfer, 3),
        redispatch_mw=round(redispatch, 3),
        storage_mw=round(storage, 3),
        flexible_load_mw=round(flexible, 3),
        extra_export_mw=round(extra_export, 3),
        residual_curtailment_mw=round(remaining, 3),
    )


def as_record(result: BalanceResult) -> dict[str, float | str]:
    return asdict(result)
