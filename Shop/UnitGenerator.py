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
            ability = UnitGenerator.get_ability(randint(0, 100))
            cost_modifier += ability * 250

            generated_units.append(
                UnitGenerator.generate_unit(0, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                                            movement_bonus, ability, cost_modifier))
        return generated_units

    @staticmethod
    def generate_enemies(difficulty, max_enemies):
        enemies = []
        for i in range(0, difficulty):
            if len(enemies) == 0:
                enemies.append(UnitGenerator.generate_unit(1, 0, 0, 0, 0, 0, 0, 0, 0))
            else:
                coin = randint(1, 2)
                if coin == 1 and len(enemies) < max_enemies:
                    enemies.append(UnitGenerator.generate_unit(1, 0, 0, 0, 0, 0, 0, 0, 0))
                else:
                    random_unit = randint(0, len(enemies) - 1)
                    enemies[random_unit].experience += 50 + 50*enemies[random_unit].level
                    enemies[random_unit].calculate_level()
        return enemies

    @staticmethod
    def generate_unit(team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                      movement_bonus, ability, cost_modifier):
        class_seed = randint(1, 6)
        if class_seed == 1:
            return Archer(team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                          movement_bonus, ability, cost_modifier)
        elif class_seed == 2:
            return Footman(team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                           movement_bonus, ability, cost_modifier)
        elif class_seed == 3:
            return Knight(team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                          movement_bonus, ability, cost_modifier)
        elif class_seed == 4:
            return Mage(team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                        movement_bonus, ability, cost_modifier)
        elif class_seed == 5:
            return Priest(team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                          movement_bonus, ability, cost_modifier)
        else:
            return Spearman(team, health_bonus, attack_bonus, defense_bonus, evasion_bonus, accuracy_bonus,
                            movement_bonus, ability, cost_modifier)

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

    @staticmethod
    def get_ability(roll):
        if roll <= 40:
            return 0
        if roll <= 90:
            return 1
        return 2

