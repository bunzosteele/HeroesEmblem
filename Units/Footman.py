import sys, pygame, os
from pygame.locals import *
from Units.Unit import *

class Footman(Unit):
    Image = "images/Footman-Idle-1-2.png"
    MaxHealth = 10
    AttackPower = 10
    Defense = 5
    Movement = 4
    MinimumRange = 0
    MaximumRange = 1
   
    def __init__(self, x , y, team):
        if team == 0:
            self.Image = "images/footman-idle-1-0.png"
        if team == 1:
            self.Image = "images/footman-idle-1-1.png"
        Unit.__init__(self, self.Image, x, y, Footman.Movement,
                      Footman.MaxHealth, Footman.Defense, Footman.MinimumRange, Footman.MaximumRange, team)