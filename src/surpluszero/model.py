from dataclasses import dataclass,asdict
from datetime import datetime,timedelta

@dataclass(frozen=True)
class Interval:
 timestamp:str;temperature_c:float;irradiance_w_m2:float;demand_mw:float;renewable_mw:float;surplus_mw:float;reserve_required_mw:float

def shape(hour,temp):
 return max(.55,.82+(.16 if 7<=hour<11 else 0)+(.30 if 12<=hour<18 else 0)+(.22 if 18<=hour<23 else 0)+(-.20 if hour<6 else 0)+max(0,temp-24)*.018)
def intervals(hours,cfg):
 raw=[]
 for n,current in enumerate(hours):
  nxt=hours[min(n+1,len(hours)-1)];start=datetime.fromisoformat(current.timestamp)
  for q in range(4):
   f=q/4;raw.append((start+timedelta(minutes=15*q),current.temperature_c+(nxt.temperature_c-current.temperature_c)*f,current.irradiance_w_m2+(nxt.irradiance_w_m2-current.irradiance_w_m2)*f))
 factors=[shape(t.hour+t.minute/60,temp) for t,temp,_ in raw];mean=sum(factors)/len(factors);out=[]
 for (t,temp,sun),factor in zip(raw,factors,strict=True):
  demand=cfg["zone_average_demand_mw"]*factor/mean
  renewable=cfg["pv_capacity_mw"]*min(1,max(0,sun/1000))*cfg["pv_performance_ratio"]
  surplus=max(0,renewable-demand-cfg["export_capacity_mw"]-cfg["scheduled_storage_mw"])
  out.append(Interval(t.isoformat(timespec="minutes"),round(temp,2),round(sun,2),round(demand,4),round(renewable,4),round(surplus,4),round(surplus*(1+cfg["forecast_uncertainty_fraction"]),4)))
 return out
def summary(rows):
 active=[x for x in rows if x.surplus_mw>0]
 return {"surplus_energy_mwh":round(sum(x.surplus_mw*.25 for x in rows),4),"peak_surplus_mw":max((x.surplus_mw for x in rows),default=0),"first_surplus_interval":active[0].timestamp if active else None,"last_surplus_interval":active[-1].timestamp if active else None,"renewable_energy_mwh":round(sum(x.renewable_mw*.25 for x in rows),4),"demand_energy_mwh":round(sum(x.demand_mw*.25 for x in rows),4)}
