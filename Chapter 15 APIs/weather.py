# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:34:18 2019

@author: mag
"""
#ex2 the weather app
import requests
import json

#loading file content as a json:
with open("key.secret") as f:
    secret = json.load(f)
    
endpoint = "http://api.openweathermap.org/data/2.5/weather"
#Minimum info to pass to API with data
payload = {"q": "London,UK", "units":"metric", "appid": secret["api_key_weather"]}
response = requests.get(endpoint, params=payload)
data = response.json()

print(data)
print("this is what data looks like: \n")

#ex3 further refinements for the weather app
print(response.url)
print(response.status_code)
print(response.headers["content-type"])

#ex4 conert response to json
print(response.text)

temperature = int(data["main"]["temp"])
print(temperature)
name = data["name"]
weather = data["weather"][0]["main"]
print(f"It's {temperature}C in {name}, and the sky is {weather}.")





#method = function within a class