import sys, pygame, os
from pygame.locals import *
from Units.Unit import *


class Knight(Unit):
    img_src = "images/Knight-Idle-1-2.png"
    BaseMinimumRange = 0
    BaseMaximumRange = 1
    BaseMaxHealth = 30
    BaseAttack = 10
    BaseDefense = 5
    BaseEvasion = 3
    BaseAccuracy = 85
    BaseMovement = 5
    BaseCost = 1000

    def __init__(self, team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                 movement_bonus, cost_modifier):
        self.Type = Knight
        self.MinimumRange = Knight.BaseMinimumRange
        self.MaximumRange = Knight.BaseMaximumRange
        self.img_src = "images/knight-idle-1-" + str(team) + ".png"
        self.MaxHealth = Knight.BaseMaxHealth + health_bonus
        self.Attack = Knight.BaseAttack + attack_bonus
        self.Defense = Knight.BaseDefense + defense_bonus
        self.Evasion = Knight.BaseEvasion + evasion_bonus
        self.Accuracy = Knight.BaseAccuracy + accuracy_bonus
        self.Movement = Knight.BaseMovement + movement_bonus
        self.Cost = Knight.BaseCost + cost_modifier
        Unit.__init__(self, team)