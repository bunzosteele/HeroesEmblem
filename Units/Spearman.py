import sys, pygame, os
from pygame.locals import *
from Units.Unit import *


class Spearman(Unit):
    img_src = "images/spearman2.png"
    Type = "Spearman"
    MaxHealth = 8
    AttackPower = 8
    Defense = 3
    Evasion = 3
    Accuracy = 95
    Movement = 3
    MinimumRange = 0
    MaximumRange = 2

    def __init__(self, x, y, team):
        if team == 0:
            self.img_src = "images/spearman.png"
        if team == 1:
            self.img_src = "images/spearman1.png"
        Unit.__init__(self, x, y, team)