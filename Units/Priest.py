from Units.Unit import *


class Priest(Unit):
    img_src = "images/Priest-Idle-1-2.png"
    BaseMinimumRange = 0
    BaseMaximumRange = 1
    BaseMaxHealth = 10
    BaseAttack = 4
    BaseDefense = 3
    BaseEvasion = 10
    BaseAccuracy = 100
    BaseMovement = 3
    BaseCost = 400

    def __init__(self, team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                 movement_bonus, cost_modifier):
        self.Type = Priest
        self.MinimumRange = Priest.BaseMinimumRange
        self.MaximumRange = Priest.BaseMaximumRange
        self.img_src = "images/Priest-Idle-1-" + str(team) + ".png"
        self.MaxHealth = Priest.BaseMaxHealth + health_bonus
        self.Attack = Priest.BaseAttack + attack_bonus
        self.Defense = Priest.BaseDefense + defense_bonus
        self.Evasion = Priest.BaseEvasion + evasion_bonus
        self.Accuracy = Priest.BaseAccuracy + accuracy_bonus
        self.Movement = Priest.BaseMovement + movement_bonus
        self.Cost = Priest.BaseCost + cost_modifier
        Unit.__init__(self, team)