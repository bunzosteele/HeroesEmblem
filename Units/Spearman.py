import sys, pygame, os
from pygame.locals import *
from Units.Unit import *


class Spearman(Unit):
    img_src = "images/Spearman-Idle-1-2.png"
    BaseMinimumRange = 0
    BaseMaximumRange = 2
    BaseMaxHealth = 15
    BaseAttack = 9
    BaseDefense = 2
    BaseEvasion = 7
    BaseAccuracy = 90
    BaseMovement = 4
    BaseCost = 700

    def __init__(self, team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                 movement_bonus, cost_modifier):
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
        Unit.__init__(self, team)