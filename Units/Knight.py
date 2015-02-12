import sys, pygame, os
from pygame.locals import *
from Units.Unit import *


class Knight(Unit):
    img_src = "images/Knight-Idle-1-2.png"
    Type = "Knight"
    MaxHealth = 30
    AttackPower = 10
    Defense = 5
    Evasion = 1
    Accuracy = 85
    Movement = 5
    MinimumRange = 0
    MaximumRange = 1

    def __init__(self, x, y, team):
        if team == 0:
            self.img_src = "images/Knight-Idle-1-0.png"
        if team == 1:
            self.img_src = "images/Knight-Idle-1-1.png"
        Unit.__init__(self, x, y, team)