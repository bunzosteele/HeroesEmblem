import sys, pygame, os
from pygame.locals import *
from Units.Unit import *

class Footman(Unit):
   
    def __init__(self, x , y, movement):
		Unit.__init__(self, "images/Knight.jpg", x, y, movement, 10, 5)