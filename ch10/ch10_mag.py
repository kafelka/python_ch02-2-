# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:56:06 2018

@author: nahas
"""

salary = {}
print(salary)

salary['al'] = 20000
print(salary)

salary["name"] = "mag"
print(salary)

salary[2] = 20
print(salary)

salary["al"] = 20500
print(salary)

salary[7] = ("Joke", "Chen", "Bond")
print(salary)

salary["bo"] = 50000
print(salary)

salary["al"] += 2000
print(salary)

tel = {"sarika":156, "martina":380, "mag": 241}
print(tel)

tel["sarika"] = 1156
tel["martina"] = 3380
tel["mag"] = 1041
print(tel)
tel["kirsty"] = 4290
print(tel)

del tel["mag"]
print(tel)

keysTel = tel.keys()
valuesTel = tel.values()
print(keysTel)
print(valuesTel)
print(type(valuesTel))

list(tel.keys())[0]