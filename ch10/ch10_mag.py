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

print(list(tel.keys()))
print(list(tel.values()))

k = "mag"

if k in tel:
    print(k, ":", tel[k])
else:
    print(k, ":", "not found!")
    
if "sarika" in tel:
    print("sarika", ":", tel["sarika"])
else:
    print("sarika", "not found")
    
    
counts = {"a": 3, "c":1, "b": 5}
labels = list(counts.keys())
labels.sort(key=lambda k:counts[k])
print(counts)
print(labels)

counts["g"] = 8
counts["f"] = 10
labels = list(counts.keys())
labels.sort(key=lambda k:counts[k])

print(counts)
print(labels)
labels = list(counts.keys())
labels.sort(key=lambda k:counts[k])
   

abc = {} 
abc = {
       1: ("greg","january",7 ),
       2: ("anna", "october",3),
       3: ("mag", "november", 13)
       }

print(list(abc.keys()))
print(list(abc.values()))


abc_keys = list(abc.keys())
abc_keys.sort(key=lambda k:abc[k][2])
print("second value keys:", abc_keys)
abc_keys.sort(key=lambda k:abc[k][1])
print("sort by first value keys:", abc_keys)

abc_keys.sort(key=lambda k:abc[k][1][-1])
print("sort by [k][1][-1]:", abc_keys)

print(sorted(abc.items(), key=lambda kv:kv[1]))
print(sorted(abc.items(), key=lambda kv:kv[1][2]))

for i in abc.items():
    print (i)

print(sorted(abc.items(), key=lambda kv:kv[0]))
#counts = {"a": 3, "c":1, "b": 5}
#sorted(counts.items(), key=lambda kv:kv[1])
#print(counts)
#sorted(counts.items(), key=lambda kv counts[k])