# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:12:29 2018

@author: maggie
"""
from MovingShapes import *
frame = Frame()
shape1 = Square(frame, 100)
for i in range(100):
    shape1.moveTick()
