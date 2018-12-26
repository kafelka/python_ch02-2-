# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:20:52 2018

@author: mag
"""
from Shapes import *

frame = Frame()
s1 = Shape('square',100)
s1.goto(200,100)

for i in range(100):
    s1.goto(x,y)
    x = x + 5
    y = y + 5