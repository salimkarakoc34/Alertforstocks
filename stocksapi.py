import requests
from datetime import datetime
import datetime
url = "https://alpha-vantage.p.rapidapi.com/query"
stocks=['qqq']

headers = {
	"X-RapidAPI-Key": "9ff4476426mshf576a0611fd61c1p108237jsn9547d85b8ad3",
	"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
}

a = datetime.datetime.now()
saat=(a.hour)
gun=(a.day)


x = datetime.datetime(2023, 1, gun, saat)
y=datetime.datetime(2023, 1, gun, saat-1)

for i in stocks:
	querystring = {"interval": "60min", "function": "TIME_SERIES_INTRADAY", "symbol": i, "datatype": "json", "output_size": "compact"}
	response = requests.request("GET", url, headers=headers, params=querystring)
	myjson = response.json()
	myjson_data = myjson['Time Series (60min)']
	tarih1=myjson_data[f'{x}']
	tarih2=myjson_data[f'{y}']
	acilis1=tarih1['1. open']
	acilis2=tarih2['1. open']
	percentage=((abs(float(acilis1)-float(acilis2))/float(acilis2)*100))


