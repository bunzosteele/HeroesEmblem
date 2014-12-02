from Units.Unit import *


class Mage(Unit):
    Image = "images/Mage-Idle-1-2.png"
    MaxHealth = 8
    AttackPower = 13
    Defense = 3
    Movement = 3
    MinimumRange = 1
    MaximumRange = 3

    def __init__(self, x, y, team):
        if team == 0:
            self.Image = "images/Mage-Idle-1-0.png"
        if team == 1:
            self.Image = "images/Mage-Idle-1-1.png"
        Unit.__init__(self, self.Image, x, y, Mage.Movement, Mage.MaxHealth, Mage.Defense, Mage.MinimumRange, Mage.MaximumRange, team)