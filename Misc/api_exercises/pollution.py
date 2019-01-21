import requests
import json

from time import strftime
import sqlite3
import time
import datetime
import random
from datetime import datetime

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

data_czas = datetime.strptime(dateTest, '%Y-%m-%dT%H:%MZ')
print(data_czas)
sama_data = datetime.strptime(dateTest, '%Y-%m-%dT%H:%MZ').date()
print(sama_data)


for i in data["data"]["data"]:
   print("date:", i["from"], "\n", "forecast:", i["intensity"]["forecast"], "\n", "index:", i["intensity"]["index"], "\n",
         i["generationmix"][0]["fuel"], i["generationmix"][0]["perc"], "\n",
         i["generationmix"][1]["fuel"], i["generationmix"][1]["perc"], "\n",
         i["generationmix"][2]["fuel"], i["generationmix"][2]["perc"], "\n",
         i["generationmix"][3]["fuel"], i["generationmix"][3]["perc"], "\n",
         i["generationmix"][4]["fuel"], i["generationmix"][4]["perc"], "\n",
         i["generationmix"][5]["fuel"], i["generationmix"][5]["perc"], "\n",
         i["generationmix"][6]["fuel"], i["generationmix"][6]["perc"], "\n",
         i["generationmix"][7]["fuel"], i["generationmix"][7]["perc"], "\n",
         i["generationmix"][8]["fuel"], i["generationmix"][8]["perc"]
         )
   
   
conn = sqlite3.connect("natGrid.db")
c = conn.cursor()

#def create_table():
#    c.execute("CREATE TABLE IF NOT EXISTS pollution(datestamp TEXT, forecast REAL, index TEXT, biomass REAL, coal REAL, imports REAL, gas REAL, nuclear REAL, other REAL, hydro REAL, solar REAL, wind REAL)")
#    conn.commit()
#     
##create_table()
#
#def carbIntensity_data_entry():
#    c.execute('''INSERT INTO pollution(datestamp, forecast, index, biomass, coal, imports, gas, nuclear, other, hydro, solar, wind) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                  
#
##    conn.commit()
   