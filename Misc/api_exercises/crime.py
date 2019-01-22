import requests
import json
from collections import Counter  #counts number of occuranes
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta
import sqlite3

#Crimes at street-level; either within a 1 mile radius of a single point, or within a custom area.
#The street-level crimes returned in the API are only an approximation of where the actual crimes occurred, they are not the exact locations. 

response = requests.get("https://data.police.uk/api/crimes-street/all-crime?lat=51.5517&lng=-0.1588&date=2018-11")
data = response.json()
#print(data)

#endpoint = "https://data.police.uk/api/crimes-street/all-crime"
#payload = {"date": "2018-12", "lat": "51.540300", "lng": "-0.195647"}
#response = requests.get(endpoint, params=payload)
#data = response.json()

#print(response.url)
#print(response.status_code)
#print(response.headers["content-type"])
#print(response.text)

crimeRecord = data[0]
print(crimeRecord)
crimeCategory = crimeRecord["category"]
print(crimeCategory)

def showCrimeSummary(data):
    crimeCategories = Counter([c["category"] for c in data])
    return crimeCategories

#print("Camden:")    
#showCrimeSummary(data)

response = requests.get("https://data.police.uk/api/crimes-street/all-crime?lat=51.53787&lng=-0.1929&date=2018-11")
data2 = response.json()

#print("NW64HJ")  
#showCrimeSummary(data2)

startDate = datetime.strptime("2018-01-01", '%Y-%m-%d').date() #date as date, not string
endDate = datetime.strptime("2018-11-30", '%Y-%m-%d').date()

counter = 0 #counter for days between start and end dates
crimeCatSummary = Counter([])
result = {}
while startDate + relativedelta(months = counter) <= endDate: #timedelta = duration in days, counter = number of days
    currentDate = (startDate + relativedelta(months = counter)).strftime("%Y-%m") #converted into string
    counter += 1 #advance to the next day
    print("For month:", currentDate)
    response = requests.get(f"https://data.police.uk/api/crimes-street/all-crime?lat=51.53787&lng=-0.1929&date={currentDate}")
    data = response.json()
    monthData = showCrimeSummary(data)
    result[currentDate] = monthData
    print("Monthly data:", monthData)
    crimeCatSummary.update(monthData)

print("Crime categories:", crimeCatSummary.keys())
crimeColumns = [key + " REAL" for key in crimeCatSummary.keys()]
columns = ", ".join(crimeColumns).replace("-", "_")

conn = sqlite3.connect("natGrid.db")
c = conn.cursor()

def create_table():
    print("Creating table...")
    c.execute("DROP TABLE IF EXISTS crime")
    c.execute(f"CREATE TABLE IF NOT EXISTS crime(month TEXT, {columns})")
    
    conn.commit()
     
create_table()

def crime_data_entry():
    print("Populating DB with data...")
    for item in results:
        c.execute('''INSERT INTO pollution(datestamp, forecast, intensityIndex, biomass, coal, imports, gas, nuclear, other, hydro, solar, wind) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                 (item["time"].strftime("%Y-%m-%d %H:00"), item['intensityForecast'], item['intensityIndex'],
                 item['fuelBiomass'], item['fuelCoal'], item['fuelImports'], item['fuelGas'],
                 item['fuelNuclear'], item['fuelOther'], item['fuelHydro'], item['fuelSolar'],
                 item['fuelWind']))
    conn.commit()
        
crime_data_entry()

   

c.close()
conn.close()
