# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:02:36 2019

@author: mag
"""
import requests
import json

#loading file content as a json:
with open("key.secret") as f:
    secret = json.load(f)

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox500a7ee37b5945b1b1d386df64193779.mailgun.org/messages",
        auth=("api", secret["api_key_gunmail"]),
        data={"from": "<magdalena.kafel@bt.com>",
              "to": ["na.hasiok@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
    

send_simple_message()