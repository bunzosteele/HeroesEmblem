import sys, pygame, os
from pygame.locals import *
from Units.Unit import *


class Footman(Unit):
    img_src = "images/Footman-Idle-1-2.png"
    Type = "Footman"
    MaxHealth = 20
    AttackPower = 9
    Defense = 4
    Evasion = 5
    Accuracy = 95
    Movement = 4
    MinimumRange = 0
    MaximumRange = 1

    def __init__(self, team):
        if team == 0:
            self.img_src = "images/footman-idle-1-0.png"
        if team == 1:
            self.img_src = "images/footman-idle-1-1.png"
        Unit.__init__(self, team)