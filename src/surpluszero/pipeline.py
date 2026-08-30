import argparse,csv,json
from dataclasses import asdict
from pathlib import Path
from .model import intervals,summary
from .sources import DATASETS,metadata,riyadh_consumption,weather

def run(config_path,output):
 cfg=json.loads(Path(config_path).read_text());output=Path(output);output.mkdir(parents=True,exist_ok=True)
 official={name:metadata(i) for name,i in DATASETS.items()}
 regional=riyadh_consumption();observations=weather(cfg["latitude"],cfg["longitude"],cfg["weather_date"],cfg["timezone"])
 rows=intervals(observations,cfg)
 with (output/"intervals.csv").open("w",newline="") as f:
  writer=csv.DictWriter(f,fieldnames=asdict(rows[0]).keys());writer.writeheader();writer.writerows(asdict(x) for x in rows)
 result={"zone":cfg["zone_name"],"summary":summary(rows),"provenance":{"government_metadata":{"class":"official","records":official},"riyadh_seasonal_consumption":{"class":"official","records":len(regional)},"weather":{"class":"measured","source":"Open-Meteo historical archive","records":len(observations)},"pv_capacity_mw":{"class":"assumed","value":cfg["pv_capacity_mw"]},"zone_average_demand_mw":{"class":"assumed","value":cfg["zone_average_demand_mw"]}},"flexible_assets":cfg["flexible_assets"],"claim_boundary":"Potential surplus in a configured pilot zone; not a measured national curtailment event."}
 (output/"manifest.json").write_text(json.dumps(result,ensure_ascii=False,indent=2));return result
def main():
 p=argparse.ArgumentParser();p.add_argument("--config",default="config/riyadh_demo.json");p.add_argument("--output",default="output/riyadh_demo");a=p.parse_args();print(json.dumps(run(a.config,a.output)["summary"],indent=2))
if __name__=="__main__":main()
