from Units.Abilities.Heal import Heal
from Units.Abilities.Rebirth import Rebirth
from Units.Abilities.Scholar import Scholar
from Units.Unit import *


class Priest(Unit):
    img_src = "images/Priest-Idle-1-2.png"
    BaseMinimumRange = 0
    BaseMaximumRange = 1
    BaseMaxHealth = 10
    BaseAttack = 4
    BaseDefense = 2
    BaseEvasion = 15
    BaseAccuracy = 100
    BaseMovement = 4
    BaseCost = 900

    def __init__(self, team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                 movement_bonus, ability, cost_modifier):
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
        if ability == 0:
            self.Ability = Heal
        elif ability == 1:
            self.Ability = Rebirth
        elif ability == 2:
            self.Ability = Scholar
        else:
            self.Ability = None
        Unit.__init__(self, team)