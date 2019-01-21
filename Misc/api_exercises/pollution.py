import requests
import json
import datetime
from time import strftime

#Get Carbon Intensity data for past 24h for specified postcode
#response = requests.get("https://api.carbonintensity.org.uk/regional/intensity/2019-01-21T09:00Z/pt12h/postcode/NW6")
#Get Carbon Intensity data for current half hour for specified postcode
response3 = requests.get("https://api.carbonintensity.org.uk/regional/intensity/2019-01-20T10:00Z/2019-01-21T10:00Z/postcode/NW6")
#response = requests.get("https://api.carbonintensity.org.uk/regional/postcode/NW6")
data = response3.json()

print(response3.url)
print(response3.status_code)
print(response3.headers["content-type"])
print(response3.text)
print("************")
#city = data["data"][0]["shortname"]
#print("City:", city)
#postcode = data["data"][0]["postcode"]
#print("Postcode:", postcode)
#date = data["data"][0]["data"][0]["from"]
#print("date:", date)
#
#intensity = data["data"][0]["data"][0]["intensity"]
#print("Intensity:", intensity)
#forecast = data["data"][0]["data"][0]["intensity"]["forecast"]
#print("Forecast:", forecast)
#index = data["data"][0]["data"][0]["intensity"]["index"]
#print("Index:", index)

city = data["data"]["shortname"]
print(city)
test = data["data"]["data"]
print(test)
print("************")
test2 = test[0]
print(test2)
forecast = test2["intensity"]["forecast"]
print(forecast)
print("************")
test2keys = list(test2.keys())
test2values  = list(test2.values())


for i in test2keys:
    print("keys:", i)
    
for i in test2values:
    print("values:", i)

    
dateTest = test2["from"]
print(dateTest)




