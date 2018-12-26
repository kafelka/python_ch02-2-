# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:49:51 2018

@author: maggie
"""
from Shapes import *
from pylab import random as r
from random import randint


class MovingShape:
    def __init__(self, frame, shape, diameter, dx, dy):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
#        setting min and max x and y for centre of the figure
        self.minx = diameter / 2
        self.maxx = frame.width - diameter / 2
        self.miny = diameter / 2
        self.maxy = frame.height - diameter / 2
        # original version with random
#        self.x = frame.width * r()
#        self.y = frame.height * r()    
#        self.x = self.minx + (frame.width - diameter) * r()
#        self.y = self.miny + (frame.height - diameter) * r()
        
#        use randint instead of the above cause it's easier
        self.x = randint(self.minx, self.maxx)
        self.y = randint(self.miny, self.maxy)
        
#        setting starting position and speed(velocity)
        self.goto(self.x, self.y)
        self.dx = dx
        self.dy = dy
        
#        move figure to position x, y 
    def goto(self, x, y):
        self.figure.goto(x, y)
        
#        function that moves the figure one step further
    def moveTick(self):
#        randomly change direction
        if r() < 0.05:
            self.dx = self.dx * -1
        if r() < 0.05:
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
        MovingShape.__init__ (self, frame, "square", diameter, randint(3, 10), randint(3, 10))
class Diamond(MovingShape):
    def __init__(self, frame, diameter):
#        MovingShape.__init__ (self, frame, "diamond", diameter, 1 + 3 * r(), 1 + 3 * r())
        MovingShape.__init__ (self, frame, "diamond", diameter, randint(1, 6), randint(1, 6))
class Circle(MovingShape):
    def __init__(self, frame, diameter):
#        MovingShape.__init__ (self, frame, "circle", diameter, 1 + 3 * r(), 1 + 3 * r())
        MovingShape.__init__ (self, frame, "circle", diameter, randint(2, 7), randint(2, 7))
