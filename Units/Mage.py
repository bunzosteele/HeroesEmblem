from Units.Unit import *


class Mage(Unit):
    Image = "images/mage.png"
    MaxHealth = 8
    AttackPower = 13
    Defense = 3
    Movement = 3

    def __init__(self, x, y, team):
        if team == 1:
            self.Image = "images/mage1.png"
        if team == 2:
            self.Image = "images/mage2.png"
        Unit.__init__(self, self.Image, x, y, Mage.Movement, Mage.MaxHealth, Mage.Defense, team)