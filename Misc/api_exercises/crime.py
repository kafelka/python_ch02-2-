import requests
import json

#Crimes at street-level; either within a 1 mile radius of a single point, or within a custom area.
#The street-level crimes returned in the API are only an approximation of where the actual crimes occurred, they are not the exact locations. 
#NW64HJ 51.5378 -0.1929 below nw6

response = requests.get("https://data.police.uk/api/crimes-street/all-crime?lat=51.5403&lng=-0.195647&date=2018-11")
data = response.json()

#endpoint = "https://data.police.uk/api/crimes-street/all-crime"
#payload = {"date": "2018-12", "lat": "51.540300", "lng": "-0.195647"}
#response = requests.get(endpoint, params=payload)
#data = response.json()
#print(data)
#print(response.url)
#print(response.status_code)
#print(response.headers["content-type"])
print(response.text)