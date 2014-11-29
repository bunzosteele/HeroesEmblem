import sys, pygame, os
from pygame.locals import *
from Units.Unit import *

class Spearman(Unit):
    Image = "images/spearman.png"
    MaxHealth = 8
    AttackPower = 8
    Defense = 3
    Movement = 3
    MinimumRange = 0
    MaximumRange = 2
   
    def __init__(self, x , y, team):
        if team == 1:
            self.Image = "images/spearman1.png"
        if team == 2:
            self.Image = "images/spearman2.png"
        Unit.__init__(self, self.Image, x, y, Spearman.Movement,
                      Spearman.MaxHealth, Spearman.Defense, Spearman.MinimumRange, Spearman.MaximumRange, team)