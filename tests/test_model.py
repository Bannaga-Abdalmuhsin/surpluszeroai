from surpluszero.model import intervals,summary
from surpluszero.sources import WeatherHour
from surpluszero.dispatch import allocate,summarize_dispatch
def test_intervals():
 hours=[WeatherHour(f"2024-06-15T{h:02d}:00",28+h*.4,max(0,900-abs(12-h)*120)) for h in range(24)]
 cfg={"zone_average_demand_mw":2.2,"pv_capacity_mw":5,"pv_performance_ratio":.82,"export_capacity_mw":0,"scheduled_storage_mw":0,"forecast_uncertainty_fraction":.15}
 rows=intervals(hours,cfg);result=summary(rows)
 assert len(rows)==96 and all(x.surplus_mw>=0 for x in rows)
 assert all(x.reserve_required_mw>=x.surplus_mw for x in rows)
 assert result["renewable_energy_mwh"]>0
 events=allocate(rows,[{"id":"a","type":"cooling","capacity_mw":2,"energy_mwh":20,"cost_sar_mwh":10,"delivery_fraction":.5},{"id":"b","type":"battery","capacity_mw":2,"energy_mwh":20,"cost_sar_mwh":20}])
 assert any(x.stage=="reallocation" for x in events)
 assert summarize_dispatch(rows,events)["verified_absorbed_mwh"]>0
