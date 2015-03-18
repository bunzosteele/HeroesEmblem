from Units.Unit import *
from Units.Abilities.Vault import *
from Units.Abilities.Thrust import *


class Spearman(Unit):
    img_src = "images/Spearman-Idle-1-2.png"
    BaseMinimumRange = 0
    BaseMaximumRange = 2
    BaseMaxHealth = 20
    BaseAttack = 10
    BaseDefense = 3
    BaseEvasion = 10
    BaseAccuracy = 90
    BaseMovement = 4
    BaseCost = 950

    def __init__(self, team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                 movement_bonus, ability, cost_modifier):
        self.Type = Spearman
        self.MinimumRange = Spearman.BaseMinimumRange
        self.MaximumRange = Spearman.BaseMaximumRange
        self.img_src = "images/Spearman-Idle-1-" + str(team) + ".png"
        self.MaxHealth = Spearman.BaseMaxHealth + health_bonus
        self.Attack = Spearman.BaseAttack + attack_bonus
        self.Defense = Spearman.BaseDefense + defense_bonus
        self.Evasion = Spearman.BaseEvasion + evasion_bonus
        self.Accuracy = Spearman.BaseAccuracy + accuracy_bonus
        self.Movement = Spearman.BaseMovement + movement_bonus
        self.Cost = Spearman.BaseCost + cost_modifier
        if ability == 0:
            self.Ability = None
        elif ability == 1:
            self.Ability = Thrust
        elif ability == 2:
            self.Ability = Vault
        Unit.__init__(self, team)