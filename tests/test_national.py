from surpluszero.national import ZoneState, balance_zone


def test_all_generation_sources_enter_one_balance():
    result = balance_zone(
        ZoneState(
            zone_id="central",
            generation_mw={"solar": 1200, "wind": 200, "gas": 3600, "other": 500},
            demand_mw=4600,
            transfer_headroom_mw=250,
            deficit_elsewhere_mw=200,
            redispatch_available_mw=180,
            storage_charge_available_mw=120,
            flexible_load_available_mw=250,
        )
    )
    assert result.generation_mw == 5500
    assert result.initial_excess_mw == 900
    assert result.transfer_mw == 200
    assert result.redispatch_mw == 180
    assert result.storage_mw == 120
    assert result.flexible_load_mw == 250
    assert result.residual_curtailment_mw == 150


def test_actions_never_exceed_initial_excess():
    result = balance_zone(
        ZoneState(
            zone_id="west",
            generation_mw={"solar": 20, "gas": 80},
            demand_mw=90,
            transfer_headroom_mw=100,
            deficit_elsewhere_mw=100,
            redispatch_available_mw=100,
            storage_charge_available_mw=100,
            flexible_load_available_mw=100,
        )
    )
    assert result.transfer_mw == 10
    assert result.redispatch_mw == 0
    assert result.residual_curtailment_mw == 0
