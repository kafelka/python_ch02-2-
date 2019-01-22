import requests
import json
from collections import Counter  #counts number of occurances
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta
import sqlite3

#Crimes at street-level; either within a 1 mile radius of a single point, or within a custom area.
#The street-level crimes returned in the API are only an approximation of where the actual crimes occurred, they are not the exact locations. 

#response = requests.get("https://data.police.uk/api/crimes-street/all-crime?lat=51.5517&lng=-0.1588&date=2018-11")
#data = response.json()
#print(data)

#endpoint = "https://data.police.uk/api/crimes-street/all-crime"
#payload = {"date": "2018-12", "lat": "51.540300", "lng": "-0.195647"}
#response = requests.get(endpoint, params=payload)
#data = response.json()

#print(response.url)
#print(response.status_code)
#print(response.headers["content-type"])
#print(response.text)

#crimeRecord = data[0]
#print(crimeRecord)
#crimeCategory = crimeRecord["category"]
#print(crimeCategory)

def showCrimeSummary(data): 
    crimeCategories = Counter([c["category"] for c in data]) ##counts number of occurances -> categories of crime
    return crimeCategories

#print("Camden:")    
#showCrimeSummary(data)

#response = requests.get("https://data.police.uk/api/crimes-street/all-crime?lat=51.53787&lng=-0.1929&date=2018-11")
#data2 = response.json()

#print("NW64HJ")  
#showCrimeSummary(data2)

startDate = datetime.strptime("2018-01-01", '%Y-%m-%d').date() #date as date, not string
endDate = datetime.strptime("2018-11-30", '%Y-%m-%d').date()

counter = 0 #counter for months between start and end dates
crimeCatSummary = Counter() 
result = {}
while startDate + relativedelta(months = counter) <= endDate: #relativedelta = duration in months, counter = number of months
    currentDate = (startDate + relativedelta(months = counter)).strftime("%Y-%m") #converted into string
    counter += 1 #advance to the next month
    print("\nFor month:", currentDate)
    response = requests.get(f"https://data.police.uk/api/crimes-street/all-crime?lat=51.53787&lng=-0.1929&date={currentDate}")
    data = response.json()
    monthData = showCrimeSummary(data) #see above
    result[currentDate] = monthData #key = result[currentDate], value = monthData
    print("Monthly data:", monthData)
    crimeCatSummary.update(monthData) #sum of all monthly data

print("Crime categories:", crimeCatSummary.keys()) #keys for all data
crimeColumns = [key + " REAL" for key in crimeCatSummary.keys()]
columns = ", ".join(crimeColumns).replace("-", "_")  #crimeColumns into 1 string and then "-" replaced with "_"

conn = sqlite3.connect("natGrid.db")
c = conn.cursor()

def create_table():
    print("Creating table...")
    c.execute("DROP TABLE IF EXISTS crime") #remove table
    c.execute(f"CREATE TABLE IF NOT EXISTS crime(month TEXT, {columns})")
    
    conn.commit()
     
create_table()

def crime_data_entry():
    print("Populating DB with data...")
    for month, data in result.items(): # m,d = kv pair, data = monthData in while loop
        questionMarks = "?, " * len(data.keys()) + "?"
        columnsString = ", ".join(data.keys()).replace("-", "_")
        print("\nData:", data)
        print(f"\nQuery: INSERT INTO crime(month, {columnsString}) VALUES({questionMarks})", (month, *data.values())) 
        c.execute(f'''INSERT INTO crime(month, {columnsString}) VALUES({questionMarks})''',
                 (month, *data.values()))   #star * unpacks the sequence/collection
        
    conn.commit()
        
crime_data_entry()

   

c.close()
conn.close()
