from Units.Unit import *
from Units.Abilities.Teleport import *
from Units.Abilities.ChainLightning import *

class Mage(Unit):
    img_src = "images/Mage-Idle-1-2.png"
    MinimumRange = 1
    MaximumRange = 3
    BaseMaxHealth = 15
    BaseAttack = 9
    BaseDefense = 2
    BaseEvasion = 10
    BaseAccuracy = 80
    BaseMovement = 4
    BaseCost = 800

    def __init__(self, team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                 movement_bonus, ability, cost_modifier):
        self.Type = Mage
        self.img_src = "images/Mage-Idle-1-" + str(team) + ".png"
        self.MaxHealth = Mage.BaseMaxHealth + health_bonus
        self.Attack = Mage.BaseAttack + attack_bonus
        self.Defense = Mage.BaseDefense + defense_bonus
        self.Evasion = Mage.BaseEvasion + evasion_bonus
        self.Accuracy = Mage.BaseAccuracy + accuracy_bonus
        self.Movement = Mage.BaseMovement + movement_bonus
        self.Cost = Mage.BaseCost + cost_modifier
        if ability == 0:
            self.Ability = None
        elif ability == 1:
            self.Ability = ChainLightning
        elif ability == 2:
            self.Ability = Teleport
        Unit.__init__(self, team)