from Units.Unit import *


class Footman(Unit):
    img_src = "images/Footman-Idle-1-2.png"
    BaseMinimumRange = 0
    BaseMaximumRange = 1
    BaseMaxHealth = 20
    BaseAttack = 9
    BaseDefense = 3
    BaseEvasion = 5
    BaseAccuracy = 95
    BaseMovement = 4
    BaseCost = 750

    def __init__(self, team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                 movement_bonus, ability, cost_modifier):
        self.Type = Footman
        self.MinimumRange = Footman.BaseMinimumRange
        self.MaximumRange = Footman.BaseMaximumRange
        self.img_src = "images/Footman-Idle-1-" + str(team) + ".png"
        self.MaxHealth = Footman.BaseMaxHealth + health_bonus
        self.Attack = Footman.BaseAttack + attack_bonus
        self.Defense = Footman.BaseDefense + defense_bonus
        self.Evasion = Footman.BaseEvasion + evasion_bonus
        self.Accuracy = Footman.BaseAccuracy + accuracy_bonus
        self.Movement = Footman.BaseMovement + movement_bonus
        self.Cost = Footman.BaseCost + cost_modifier
        self.Ability = None
        Unit.__init__(self, team)