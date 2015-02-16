from Units.Unit import *


class Archer(Unit):
    img_src = "images/Archer-Idle-1-2.png"
    BaseMinimumRange = 2
    BaseMaximumRange = 4
    BaseMaxHealth = 15
    BaseAttack = 10
    BaseDefense = 2
    BaseEvasion = 10
    BaseAccuracy = 75
    BaseMovement = 3
    BaseCost = 800

    def __init__(self, team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                 movement_bonus, cost_modifier):
        self.Type = Archer
        self.MinimumRange = Archer.BaseMinimumRange
        self.MaximumRange = Archer.BaseMaximumRange
        self.img_src = "images/Archer-Idle-1-" + str(team) + ".png"
        self.MaxHealth = Archer.BaseMaxHealth + health_bonus
        self.Attack = Archer.BaseAttack + attack_bonus
        self.Defense = Archer.BaseDefense + defense_bonus
        self.Evasion = Archer.BaseEvasion + evasion_bonus
        self.Accuracy = Archer.BaseAccuracy + accuracy_bonus
        self.Movement = Archer.BaseMovement + movement_bonus
        self.Cost = Archer.BaseCost + cost_modifier
        Unit.__init__(self, team)