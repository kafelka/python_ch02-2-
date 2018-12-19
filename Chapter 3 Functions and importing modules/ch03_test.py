# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:44:55 2018

@author: nahas
"""

from ch03_mag import *

#ch03_mag.hello_world_3args(a1,b1,c3)
#
#ch03_mag.tempConverter(celsius)
#
#ch03_mag.convertDistance(10)


celsius = int(input("What's the temperature in your city today?"))
    
tempConverter(celsius)

a1 = "hello "
b1 = "world "
c1 = "it's "
a2 = "love "
b2 = "coding"
c2 = "Monday "
a3 = "I think I "
c3 = "again!"
hello_world_3args(a1,b1,c3)
hello_world_3args(a3,a2,b2)
hello_world_3args(c1,c2,c3)

convertDistance(10)