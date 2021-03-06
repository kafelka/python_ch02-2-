# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:56:06 2018

@author: mag
"""
#ex1 creating a dictionry, assigning and updating values
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

#ex2, ex3 create your own dictionary, look up and delete values
tel = {"sarika":156, "martina":380, "mag": 241}
print(tel)

print(tel["sarika"])
tel["sarika"] = 1156
tel["martina"] = 3380
tel["mag"] = 1041
print(tel)
tel["kirsty"] = 4290
print(tel)

del tel["mag"]
print(tel)

#ex4 keys and values - retrieving them from dictionary

keysTel = tel.keys()
valuesTel = tel.values()
print(keysTel)
print(valuesTel)
print(type(valuesTel))

#ex5 convert keys and values to list data type
print(list(tel.keys()))
print(list(tel.values()))

#ex6 in order to avoid errors, we can run a test:
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
       2: ("anna", "october",31),
       3: ("mag", "november", 13)
       }
#converting keys and value to list data type:
print(list(abc.keys()))
print(list(abc.values()))

#ex7 & ex8 sorting dictionaries
abc_keys = list(abc.keys())
print("***************8", abc_keys)
abc_keys.sort(key=lambda k:abc[k][2])
print("second value keys:", abc_keys)
abc_keys.sort(key=lambda k:abc[k][1])
print("sort by first value keys:", abc_keys)

abc_keys.sort(key=lambda k:abc[k][1][-1])
print("sort by [k][1][-1]:", abc_keys)

print(sorted(abc.items(), key=lambda kv:kv[1]))
print(sorted(abc.items(), key=lambda kv:kv[1][2]))
print(sorted(abc, key=lambda k:abc[k][1]))

for i in abc.items():
    print (i)

print(sorted(abc.items(), key=lambda kv:kv[0]))
counts = {"a": 3, "c":1, "b": 5}
sorted(counts.items(), key=lambda kv:kv[1])   
print(counts)

print(sorted(abc, key=lambda k: abc[k]))
print(sorted(abc, key=lambda k: abc[k][2]))

#reverse order when sorting (descending order)
abc_keys.sort(reverse=True, key = lambda k:abc[k][2])

sorted(abc, key=lambda k:abc[k][2], reverse=True)
sorted(abc.items(), key=lambda kv: kv[1][2], reverse=True)


metals = {}
metals = {
        "gold": (19320, 40.81, 10),
        "silver": (10490, 0.53, 100),
        "platinum": (21400, 1, 1)
        }
#* second value = price per gram in USD

print(metals)
print("***********")
print("list keys", list(metals.keys()))
print("list values", list(metals.values()))

metals_keys = list(metals.keys())
print(metals_keys)
metals_values = list(metals.values())

print("***********")

metals_keys.sort(key=lambda k:metals[k][2])
print("sort by second value keys:", metals_keys)
metals_keys.sort(key=lambda k:metals[k][1])
print("sort by first value keys:", metals_keys)

print("***********")
print(sorted(metals, key=lambda k:metals[k][2], reverse=True))
print(metals_values)
y = sorted(metals,key = lambda k:metals[k][2])
print(y)
x = sorted(metals.items(), key=lambda kv: kv[1][2], reverse=True)
print(x)

print(metals_values)