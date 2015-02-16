from Units.Unit import *


class Mage(Unit):
    img_src = "images/Mage-Idle-1-2.png"
    MinimumRange = 1
    MaximumRange = 3
    BaseMaxHealth = 20
    BaseAttack = 10
    BaseDefense = 2
    BaseEvasion = 3
    BaseAccuracy = 80
    BaseMovement = 3
    BaseCost = 900

    def __init__(self, team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                 movement_bonus, cost_modifier):
        self.Type = Mage
        self.img_src = "images/Mage-Idle-1-" + str(team) + ".png"
        self.MaxHealth = Mage.BaseMaxHealth + health_bonus
        self.Attack = Mage.BaseAttack + attack_bonus
        self.Defense = Mage.BaseDefense + defense_bonus
        self.Evasion = Mage.BaseEvasion + evasion_bonus
        self.Accuracy = Mage.BaseAccuracy + accuracy_bonus
        self.Movement = Mage.BaseMovement + movement_bonus
        self.Cost = Mage.BaseCost + cost_modifier
        Unit.__init__(self, team)