import json
from dataclasses import dataclass
from urllib.parse import urlencode
from urllib.request import Request,urlopen

OPEN_DATA="https://open.data.gov.sa/data/api"
GASTAT="https://api.stats.gov.sa/v1/stats/DPV_HES_EHE_IT_HES0303"
WEATHER="https://archive-api.open-meteo.com/v1/archive"
DATASETS={
 "consumer_sales":"03b3fed0-d8c5-47e3-bf83-dfa59bc39897",
 "electricity_users":"eae27e00-386a-4212-9cd6-3087fb42c5e3",
 "category_consumption":"5e4851e8-7af1-4bfb-904f-c03dda024acb",
 "average_consumption":"f12628ed-d4cb-49d1-8618-4957dc848c97",
 "peak_load":"004003e8-343c-4eee-90bc-71370570dcdd"}

def fetch(url):
 req=Request(url,headers={"Accept":"application/json","User-Agent":"SurplusZeroAI/0.1"})
 with urlopen(req,timeout=30) as response:return json.load(response)
def metadata(dataset_id):return fetch(f"{OPEN_DATA}/datasets?{urlencode({'version':-1,'dataset':dataset_id})}")
def riyadh_consumption():return [x for x in fetch(GASTAT).get("value",[]) if x.get("REGION_ENGL")=="Riyadh"]
@dataclass(frozen=True)
class WeatherHour: timestamp:str; temperature_c:float; irradiance_w_m2:float
def weather(lat,lon,day,timezone):
 q=urlencode({"latitude":lat,"longitude":lon,"start_date":day,"end_date":day,"hourly":"temperature_2m,shortwave_radiation","timezone":timezone})
 h=fetch(f"{WEATHER}?{q}")["hourly"]
 return [WeatherHour(t,float(a),float(b)) for t,a,b in zip(h["time"],h["temperature_2m"],h["shortwave_radiation"],strict=True)]
