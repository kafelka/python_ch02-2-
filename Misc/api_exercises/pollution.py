import requests
import json
from time import strftime
import sqlite3
import random
from datetime import datetime, timedelta


startDate = datetime.strptime("2018-11-01", '%Y-%m-%d').date() #date as date, not string
#endDate = datetime.now().date() #today's date
endDate = datetime.strptime("2018-11-30", '%Y-%m-%d').date()
observationHours = [6, 12, 18, 22] #hours I'm interested in 

results = []
def createNewData(data):
    #transforming raw json into understandable dictionary
    for row in data["data"]["data"]:
        newData = {
            "time": datetime.strptime(row["from"], '%Y-%m-%dT%H:%MZ'),
            "intensityForecast": row["intensity"]["forecast"],
            "intensityIndex": row["intensity"]["index"]
        }
        #obejrzij sie na dol dziolszko
        for fuelDictionary in row["generationmix"]:
            fuel = fuelDictionary["fuel"].title()
            newData[f"fuel{fuel}"] = fuelDictionary["perc"]
        
        if newData["time"].hour in observationHours and newData["time"].minute == 0:
            results.append(newData)

print("Fetching data from API...")
counter = 0 #counter for days between start and end dates
while startDate + timedelta(days = counter) <= endDate: #timedelta = duration in days, counter = number of days
    currentDate = (startDate + timedelta(days = counter)).strftime("%Y-%m-%d") #converted into string
    counter += 1 #advance to the next day
    print("For date:", currentDate)
    #Get Carbon Intensity data for current half hour for specified postcode
    response = requests.get(f"https://api.carbonintensity.org.uk/regional/intensity/{currentDate}T00:00Z/{currentDate}T23:30Z/postcode/NW6")
    data = response.json()
    createNewData(data)
    
    
#print(response.url)
#print(response.status_code)
#print(response.headers["content-type"])
#print(response.text)

#city = data["data"]["shortname"]
#print(city)

print(results[0])
print("Number of results:", len(results))

   
conn = sqlite3.connect("natGrid.db")
c = conn.cursor()

def create_table():
    print("Creating table...")
    c.execute("CREATE TABLE IF NOT EXISTS pollution(datestamp TEXT, forecast REAL, intensityIndex TEXT, biomass REAL, coal REAL, imports REAL, gas REAL, nuclear REAL, other REAL, hydro REAL, solar REAL, wind REAL)")
    c.execute("DELETE FROM pollution")
    conn.commit()
     
create_table()

def carbIntensity_data_entry():
    print("Populating DB with data...")
    for item in results:
        c.execute('''INSERT INTO pollution(datestamp, forecast, intensityIndex, biomass, coal, imports, gas, nuclear, other, hydro, solar, wind) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                 (item["time"].strftime("%Y-%m-%d %H:00"), item['intensityForecast'], item['intensityIndex'],
                 item['fuelBiomass'], item['fuelCoal'], item['fuelImports'], item['fuelGas'],
                 item['fuelNuclear'], item['fuelOther'], item['fuelHydro'], item['fuelSolar'],
                 item['fuelWind']))
    conn.commit()
        
carbIntensity_data_entry()

   

#closing cursor
c.close()
#closing connection to db
conn.close()



#
#a = [{'name': "Wojtek", "age": 8}, {'name': "Magda", "age": 18}]  
#phoneBook = {}
#for person in a:
#    phoneBook[person["name"]] = person["age"]    
#print(phoneBook)