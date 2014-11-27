from Units.Unit import *


class Mage(Unit):
    Image = "images/magea.gif"
    MaxHealth = 8
    AttackPower = 13
    Defense = 3

    def __init__(self, x, y, movement, team):
        if team == 1:
            self.Image = "images/magea1.gif"
        if team == 2:
            self.Image = "images/magea2.gif"
        Unit.__init__(self, self.Image, x, y, movement, Mage.MaxHealth, Mage.Defense, team)