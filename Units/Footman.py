import sys, pygame, os
from pygame.locals import *
from Units.Unit import *

class Footman(Unit):
    Image = "images/Footman.png"
    MaxHealth = 10
    AttackPower = 10
    Defense = 5
   
    def __init__(self, x , y, movement, team):
        if team == 1:
            self.Image = "images/footman1.png"
        if team == 2:
            self.Image = "images/footman2.png"
        Unit.__init__(self, self.Image, x, y, movement, Footman.MaxHealth, Footman.Defense, team)