from BattlefieldHelper import *
from random import randint


class CombatHelper():
    def __init__(self):
        pass

    attack_color = (200, 100, 100, 150)

    @staticmethod
    def draw_attack_shadow(attacker, battlefield, screen, drawing_helper):
        starting_pos = attacker.get_location()
        max_range_options = CombatHelper.get_attack_options(starting_pos[0], starting_pos[1],
                                                            attacker.get_maximum_range(),
                                                            battlefield.tiles[starting_pos[1]][
                                                                starting_pos[0]].Altitude,
                                                            battlefield, 0, [])
        min_range_option = CombatHelper.get_attack_options(starting_pos[0], starting_pos[1],
                                                           attacker.get_minimum_range(),
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
        return CombatHelper.can_attack_targets(attacker, battlefield, enemies)

    @staticmethod
    def can_attack_targets(attacker, battlefield, targets):
        starting_pos = attacker.get_location()
        max_range_options = CombatHelper.get_attack_options(starting_pos[0], starting_pos[1],
                                                            attacker.get_maximum_range(),
                                                            battlefield.tiles[starting_pos[1]][
                                                                starting_pos[0]].Altitude,
                                                            battlefield, 0, [])
        min_range_options = CombatHelper.get_attack_options(starting_pos[0], starting_pos[1],
                                                            attacker.get_minimum_range(),
                                                            battlefield.tiles[starting_pos[1]][
                                                                starting_pos[0]].Altitude,
                                                            battlefield, 0, [])
        options = []
        for option in max_range_options:
            if option not in min_range_options:
                options.append(option)
        for target in targets:
            if target.get_location() in options:
                return True
        return False

    @staticmethod
    def attack(target_tile, target_unit, game_state):
        game_state.selected.attacking = True
        game_state.selected.attack_start_frame = game_state.animation_state + 1
        if CombatHelper.check_hit(target_tile, target_unit, game_state.selected):
            damage = CombatHelper.deal_damage(target_tile, target_unit, game_state.selected)
        else:
            damage = 0
        return damage

    @staticmethod
    def check_hit(target_tile, target_unit, attacker):
        chance_to_hit = attacker.Accuracy
        chance_to_hit = chance_to_hit - target_unit.Evasion
        chance_to_hit = chance_to_hit - target_tile.AccuracyPenalty
        roll = randint(1, 100)
        return roll <= chance_to_hit

    @staticmethod
    def deal_damage(target_tile, target_unit, attacker):
        damage_dealt = attacker.AttackPower
        damage_dealt = damage_dealt - target_unit.Defense
        damage_dealt = damage_dealt - target_tile.DefenseBoost
        roll = randint(1, 100)
        if roll <= 10:
            damage_dealt -= 1
        if 90 <= roll < 100:
            damage_dealt += 1
        if roll == 100:
            damage_dealt *= 2
        target_unit.deal_damage(damage_dealt)
        return damage_dealt

