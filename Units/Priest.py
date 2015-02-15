import sys, pygame, os
from pygame.locals import *
from Units.Unit import *


class Priest(Unit):
    img_src = "images/Priest-Idle-1-2.png"
    Type = "Priest"
    MaxHealth = 10
    AttackPower = 0
    Defense = 2
    Evasion = 10
    Accuracy = 100
    Movement = 3
    MinimumRange = 0
    MaximumRange = 1

    def __init__(self, team):
        if team == 0:
            self.img_src = "images/Priest-Idle-1-0.png"
        if team == 1:
            self.img_src = "images/Priest-Idle-1-1.png"
        Unit.__init__(self, team)