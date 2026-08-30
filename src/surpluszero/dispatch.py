from dataclasses import dataclass

@dataclass(frozen=True)
class Dispatch:
 timestamp:str;asset_id:str;asset_type:str;stage:str;requested_mw:float;delivered_mw:float;shortfall_mw:float;cost_sar:float

def allocate(rows,assets,interval_hours=.25):
 remaining={a["id"]:a["energy_mwh"] for a in assets};events=[]
 for row in rows:
  need=row.surplus_mw;used=set()
  for stage in ("primary","reallocation"):
   target=need
   for asset in sorted(assets,key=lambda a:a["cost_sar_mwh"]):
    if target<=1e-9:break
    available=min(asset["capacity_mw"],remaining[asset["id"]]/interval_hours)
    if available<=0 or (stage=="reallocation" and asset["id"] in used):continue
    requested=min(target,available);fraction=asset.get("delivery_fraction",1) if stage=="primary" else 1
    delivered=requested*fraction;remaining[asset["id"]]-=delivered*interval_hours
    events.append(Dispatch(row.timestamp,asset["id"],asset["type"],stage,round(requested,4),round(delivered,4),round(requested-delivered,4),round(delivered*interval_hours*asset["cost_sar_mwh"],4)))
    used.add(asset["id"]);target-=requested
   delivered=sum(e.delivered_mw for e in events if e.timestamp==row.timestamp and e.stage==stage)
   need=max(0,(row.surplus_mw if stage=="primary" else need)-delivered)
 return events

def summarize_dispatch(rows,events):
 available=sum(r.surplus_mw*.25 for r in rows);delivered=sum(e.delivered_mw*.25 for e in events)
 return {"available_surplus_mwh":round(available,4),"verified_absorbed_mwh":round(min(available,delivered),4),"unabsorbed_mwh":round(max(0,available-delivered),4),"absorption_rate_pct":round(100*min(available,delivered)/available,2) if available else 100,"primary_shortfall_mwh":round(sum(e.shortfall_mw*.25 for e in events if e.stage=="primary"),4),"dispatch_cost_sar":round(sum(e.cost_sar for e in events),2)}
