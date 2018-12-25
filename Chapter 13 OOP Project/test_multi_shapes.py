# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:33:17 2018

@author: maggie
"""
from MovingShapes import *
frame = Frame()
numshapes = 3
shapes = [Square(frame, 100), Circle(frame, 80), Diamond(frame, 90)]
#for i in range(numshapes):
#    shapes.append(Square(frame, 100))
for i in range(100):
    for shape in shapes:
        shape.moveTick()
