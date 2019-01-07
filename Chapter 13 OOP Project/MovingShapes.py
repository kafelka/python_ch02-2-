# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:49:51 2018

@author: maggie
"""
from Shapes import *
from pylab import random as r
from random import randint


class MovingShape:
    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        self.dx = randint(1, 10)
        self.dy = randint(1, 10)
        self.setXY(frame)
        
    def setXY(self,frame):
#        setting min and max x and y for centre of the figure
        self.minx = self.diameter / 2
        self.maxx = frame.width - self.diameter / 2
        self.miny = self.diameter / 2
        self.maxy = frame.height - self.diameter / 2
        # original version with random
#        self.x = frame.width * r()
#        self.y = frame.height * r()    
#        self.x = self.minx + (frame.width - self.diameter) * r()
#        self.y = self.miny + (frame.height - self.diameter) * r()
        
#        use randint instead of the above cause it's easier
        self.x = randint(self.minx, self.maxx)
        self.y = randint(self.miny, self.maxy)
        
#        setting starting position and speed(velocity)
        self.goto(self.x, self.y)
        
        
#        move figure to position x, y 
    def goto(self, x, y):
        self.figure.goto(x, y)
        
#        function that moves the figure one step further
    def moveTick(self):
#        randomly change direction
        if r() < 0.03:
            self.dx = self.dx * -1
        if r() < 0.03:
            self.dy = self.dy * -1
#        move
        self.x = self.x + self.dx
        self.y = self.y + self.dy
               
        if self.x < self.minx:
#            reversing the direction of the move
            self.dx = self.dx * -1
#            self.x does not cross the border
            self.x = self.minx
        elif self.x > self.maxx:
            self.dx = self.dx * -1
            self.x = self.maxx
        if self.y < self.miny:
            self.dy = self.dy * -1
            self.y = self.miny
        elif self.y > self.maxy:
            self.dy = self.dy * -1
            self.y = self.maxy
            
        self.goto(self.x, self.y)
        
class Square(MovingShape):
    def __init__(self, frame, diameter):
#        MovingShape.__init__ (self, frame, "square", diameter, 1 + 3 * r(), 1 + 3 * r())
        MovingShape.__init__ (self, frame, "square", diameter)
        
class Diamond(MovingShape):
    def __init__(self, frame, diameter):
#        MovingShape.__init__ (self, frame, "diamond", diameter, 1 + 3 * r(), 1 + 3 * r())
        MovingShape.__init__ (self, frame, "diamond", diameter)
        
    def setXY(self,frame):
#        diameter ** 2
        self.minx = int((self.diameter / 2) * 2**0.5)
        self.maxx = int(frame.width - (self.diameter / 2) * 2**0.5)
        self.miny = int((self.diameter / 2) * 2**0.5)
        self.maxy = int(frame.height - (self.diameter / 2) * 2**0.5)
        self.x = randint(self.minx, self.maxx)
        self.y = randint(self.miny, self.maxy)
        self.goto(self.x, self.y)
        
class Circle(MovingShape):
    def __init__(self, frame, diameter):
#        MovingShape.__init__ (self, frame, "circle", diameter, 1 + 3 * r(), 1 + 3 * r())
        MovingShape.__init__ (self, frame, "circle", diameter)
