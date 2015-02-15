import sys, pygame, os
from pygame.locals import *
from Units.Unit import *


class Spearman(Unit):
    img_src = "images/Spearman-Idle-1-2.png"
    Type = "Spearman"
    MaxHealth = 25
    AttackPower = 9
    Defense = 2
    Evasion = 7
    Accuracy = 90
    Movement = 4
    MinimumRange = 0
    MaximumRange = 2

    def __init__(self, team):
        if team == 0:
            self.img_src = "images/Spearman-Idle-1-0.png"
        if team == 1:
            self.img_src = "images/Spearman-Idle-1-1.png"
        Unit.__init__(self, team)