from Units.Unit import *


class Mage(Unit):
    img_src = "images/Mage-Idle-1-2.png"
    Type = "Mage"
    MaxHealth = 20
    AttackPower = 10
    Defense = 1
    Evasion = 1
    Accuracy = 80
    Movement = 3
    MinimumRange = 1
    MaximumRange = 3
    MagicPower = 9000

    def __init__(self, x, y, team):
        if team == 0:
            self.img_src = "images/Mage-Idle-1-0.png"
        if team == 1:
            self.img_src = "images/Mage-Idle-1-1.png"
        Unit.__init__(self, x, y, team)