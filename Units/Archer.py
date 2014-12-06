from Units.Unit import *


class Archer(Unit):
    Image = "images/archer-idle-1-2.png"
    Type = "Archer"
    MaxHealth = 6
    AttackPower = 10
    Defense = 2
    Movement = 3
    MinimumRange = 2
    MaximumRange = 4

    def __init__(self, x, y, team):
        if team == 0:
            self.Image = "images/archer-idle-1-0.png"
        if team == 1:
            self.Image = "images/archer-idle-1-1.png"
        Unit.__init__(self, x, y, team)