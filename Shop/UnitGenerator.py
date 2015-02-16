from random import randint
from Units.Archer import Archer
from Units.Footman import Footman
from Units.Knight import Knight
from Units.Mage import Mage
from Units.Priest import Priest
from Units.Spearman import Spearman


class UnitGenerator():
    def __init__(self):
        pass

    @staticmethod
    def generate_units():
        generated_units = []
        while len(generated_units) < 8:
            class_seed = randint(1, 6)
            cost_modifier = 0
            health_bonus = UnitGenerator.get_health_bonus(randint(0, 100))
            cost_modifier += health_bonus * 50
            attack_bonus = UnitGenerator.get_attack_bonus(randint(0, 100))
            cost_modifier += attack_bonus * 50
            defense_bonus = UnitGenerator.get_defense_bonus(randint(0, 100))
            cost_modifier += defense_bonus * 50
            evasion_bonus = UnitGenerator.get_evasion_bonus(randint(0, 100))
            cost_modifier += evasion_bonus * 25
            accuracy_bonus = UnitGenerator.get_accuracy_bonus(randint(0, 100))
            cost_modifier += accuracy_bonus * 10
            movement_bonus = UnitGenerator.get_movement_bonus(randint(0, 100))
            cost_modifier += movement_bonus * 250

            if class_seed == 1:
                unit = Archer(0, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                              movement_bonus, cost_modifier)
            elif class_seed == 2:
                unit = Footman(0, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                               movement_bonus, cost_modifier)
            elif class_seed == 3:
                unit = Knight(0, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                              movement_bonus, cost_modifier)
            elif class_seed == 4:
                unit = Mage(0, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                            movement_bonus, cost_modifier)
            elif class_seed == 5:
                unit = Priest(0, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                              movement_bonus, cost_modifier)
            else:
                unit = Spearman(0, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                                movement_bonus, cost_modifier)

            generated_units.append(unit)
        return generated_units

    @staticmethod
    def generate_enemies(difficulty):
        return [Archer(1, 0, 0, 0, 0, 0, 0, 0)]


    @staticmethod
    def get_health_bonus(roll):
        if roll > 99:
            return 5
        if roll > 95:
            return 4
        if roll > 90:
            return 3
        if roll > 80:
            return 2
        if roll > 70:
            return 1
        if roll < 30:
            return -1
        if roll < 20:
            return -2
        if roll < 10:
            return -3
        if roll < 5:
            return -4
        if roll < 1:
            return -5
        return 0

    @staticmethod
    def get_attack_bonus(roll):
        if roll > 90:
            return 2
        if roll > 70:
            return 1
        if roll < 30:
            return -1
        if roll < 10:
            return -2
        return 0

    @staticmethod
    def get_defense_bonus(roll):
        if roll > 90:
            return 2
        if roll > 70:
            return 1
        if roll < 30:
            return -1
        if roll < 10:
            return -2
        return 0

    @staticmethod
    def get_evasion_bonus(roll):
        if roll > 90:
            return 3
        if roll > 80:
            return 2
        if roll > 70:
            return 1
        if roll < 30:
            return -1
        if roll < 20:
            return -3
        if roll < 10:
            return -3
        return 0

    @staticmethod
    def get_accuracy_bonus(roll):
        if roll > 99:
            return 5
        if roll > 95:
            return 4
        if roll > 90:
            return 3
        if roll > 80:
            return 2
        if roll > 70:
            return 1
        if roll < 30:
            return -1
        if roll < 20:
            return -2
        if roll < 10:
            return -3
        if roll < 5:
            return -4
        if roll < 1:
            return -5
        return 0

    @staticmethod
    def get_movement_bonus(roll):
        if roll > 90:
            return 1
        if roll < 10:
            return -1
        return 0
