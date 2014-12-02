import sys, pygame, os
from pygame.locals import *
from Units.Unit import *

class Knight(Unit):
    Image = "images/Knight-Idle-1-2.png"
    MaxHealth = 20
    AttackPower = 15
    Defense = 10
    Movement = 5
    MinimumRange = 0
    MaximumRange = 1
   
    def __init__(self, x , y, team):
        if team == 0:
            self.Image = "images/Knight-Idle-1-0.png"
        if team == 1:
            self.Image = "images/Knight-Idle-1-1.png"
        Unit.__init__(self, self.Image, x, y, Knight.Movement,
                      Knight.MaxHealth, Knight.Defense, Knight.MinimumRange, Knight.MaximumRange, team)