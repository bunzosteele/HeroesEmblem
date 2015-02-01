from BattlefieldHelper import *

class CombatHelper():

    def __init__(self):
        pass

    attack_color = (200, 100, 100, 150)

    @staticmethod
    def draw_attack_shadow(attacker, battlefield, screen, drawing_helper):
        starting_pos = attacker.get_location()
        max_range_options = CombatHelper.get_attack_options(starting_pos[0], starting_pos[1], attacker.get_maximumRange(),
                                         battlefield.tiles[starting_pos[1]][starting_pos[0]].Altitude,
                                         battlefield, 0, [])
        min_range_option = CombatHelper.get_attack_options(starting_pos[0], starting_pos[1], attacker.get_minimumRange(),
                                             battlefield.tiles[starting_pos[1]][starting_pos[0]].Altitude,
                                             battlefield, 0, [])
        options = []
        for option in max_range_options:
            if option not in min_range_option:
                options.append(option)
        drawing_helper.draw_shadow(options, battlefield, CombatHelper.attack_color, screen)


    @staticmethod
    def get_attack_options(x, y, range, attacker_altitude, battlefield, distance, options):
        if BattlefieldHelper.is_in_bounds(x, y, battlefield) and distance <= range:
            options.append((x, y))

            if attacker_altitude >= battlefield.tiles[y][x].Altitude:
                CombatHelper.get_attack_options(x + 1, y, range, attacker_altitude, battlefield, distance + 1, options)
                CombatHelper.get_attack_options(x - 1, y, range, attacker_altitude, battlefield, distance + 1, options)
                CombatHelper.get_attack_options(x, y + 1, range, attacker_altitude, battlefield, distance + 1, options)
                CombatHelper.get_attack_options(x, y - 1, range, attacker_altitude, battlefield, distance + 1, options)
        return options



    @staticmethod
    def can_attack(attacker, battlefield, units, current_player):
        enemies = []
        for unit in units:
            if unit.get_team() != current_player:
                enemies.append(unit)
        starting_pos = attacker.get_location()
        max_range_options = CombatHelper.get_attack_options(starting_pos[0], starting_pos[1], attacker.get_maximumRange(),
                                         battlefield.tiles[starting_pos[1]][starting_pos[0]].Altitude,
                                         battlefield, 0, [])
        min_range_options = CombatHelper.get_attack_options(starting_pos[0], starting_pos[1], attacker.get_minimumRange(),
                                             battlefield.tiles[starting_pos[1]][starting_pos[0]].Altitude,
                                             battlefield, 0, [])
        options = []
        for option in max_range_options:
            if option not in min_range_options:
                options.append(option)
        for enemy in enemies:
            if enemy.get_location() in options:
                return True
        return False