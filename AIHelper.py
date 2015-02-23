from MovementHelper import *


class AIHelper():
    def __init__(self):
        pass

    @staticmethod
    def play_turn(game_state):
        ai_units = AIHelper.get_ai_units(game_state)
        if len(ai_units) == 0:
            return False

        invalid_units = game_state.tapped_units
        units_with_options = AIHelper.get_options(game_state, ai_units, invalid_units)
        highest_priority_unit = units_with_options[0]
        for unit_with_options in units_with_options:
            if unit_with_options[1][1] > highest_priority_unit[1][1]:
                highest_priority_unit = unit_with_options

        conflicted_unit = AIHelper.get_at_tile(ai_units, highest_priority_unit[1][0][0])
        if conflicted_unit is None or conflicted_unit == highest_priority_unit[0]:
            game_state.selected = highest_priority_unit[0]
            AIHelper.move_unit(highest_priority_unit[0], highest_priority_unit[1][0][0])
            AIHelper.attack_with_unit(highest_priority_unit[0], game_state)
            game_state.tapped_units.append(highest_priority_unit[0])
        else:
            conflicted_unit_with_options = None
            for unit_with_options in units_with_options:
                if unit_with_options[0] == conflicted_unit:
                    conflicted_unit_with_options = unit_with_options

            next_conflicted_unit = AIHelper.get_at_tile(ai_units, conflicted_unit_with_options[1][0][0])
            while next_conflicted_unit is not None:
                conflicted_unit_with_options[1].remove(conflicted_unit_with_options[1][0])
                next_conflicted_unit = AIHelper.get_at_tile(ai_units, conflicted_unit_with_options[1][0][0])

            game_state.selected = conflicted_unit_with_options[0]
            AIHelper.move_unit(conflicted_unit_with_options[0], conflicted_unit_with_options[1][0][0])
            AIHelper.attack_with_unit(conflicted_unit_with_options[0], game_state)
            game_state.tapped_units.append(conflicted_unit_with_options[0])
            game_state.selected = highest_priority_unit[0]
            AIHelper.move_unit(highest_priority_unit[0], highest_priority_unit[1][0][0])
            AIHelper.attack_with_unit(highest_priority_unit[0], game_state)
            game_state.tapped_units.append(highest_priority_unit[0])

        return True

    @staticmethod
    def get_ai_units(game_state):
        units = []
        for unit in game_state.units:
            if unit.get_team() == 1 and unit not in game_state.tapped_units:
                units.append(unit)
        return units

    @staticmethod
    def get_player_units(game_state):
        units = []
        for unit in game_state.units:
            if unit.get_team() == 0:
                units.append(unit)
        return units

    @staticmethod
    def get_ranged_units(units):
        ranged_units = []
        for unit in units:
            if unit.BaseMaximumRange > 1:
                ranged_units.append(unit)
        return ranged_units

    @staticmethod
    def get_options(game_state, units, invalid_units):
        units_with_options = []
        for unit in units:
            options = MovementHelper.get_movement_options(unit.get_location()[0], unit.get_location()[1], invalid_units,
                                                          unit,
                                                          game_state.battlefield, unit.get_movement())
            options.append(unit.get_location())
            options_with_values = []
            for option in options:
                option_with_value = (option, AIHelper.calculate_value(game_state, option, unit))
                options_with_values.append(option_with_value)
            units_with_options.append((unit, sorted(options_with_values, key=lambda option: option[1], reverse=True)))
        return units_with_options

    @staticmethod
    def calculate_value(game_state, option, unit):
        value = 0
        targets = AIHelper.get_attackable_units(unit, option, game_state)
        if len(targets) > 0:
            value += AIHelper.get_targets_value(targets, unit)
        enemies = AIHelper.get_player_units(game_state)
        distance = AIHelper.get_shortest_distance(option, enemies)
        if distance > unit.MaximumRange + unit.Movement:
            value -= 2 ** distance
        value -= AIHelper.get_shortest_distance(option, enemies)
        value += AIHelper.get_terrain_value(game_state.battlefield, option)
        return value

    @staticmethod
    def get_attackable_units(attacker, option, game_state):
        enemies = []
        for unit in game_state.units:
            if unit.get_team() != game_state.current_player:
                enemies.append(unit)
        return AIHelper.can_attack_targets(attacker, option, game_state.battlefield, enemies)

    @staticmethod
    def can_attack_targets(attacker, starting_pos, battlefield, targets):
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
        hittable_targets = []
        for target in targets:
            if target.get_location() in options:
                hittable_targets.append(target)

        return hittable_targets

    @staticmethod
    def get_targets_value(targets, unit):
        value = 0
        i = 0
        for target in targets:
            if i == 0:
                value += 50
            if i > 0:
                if (unit.CurrentHealth / float(unit.MaxHealth)) <= .4:
                    value -= 10
                else:
                    value -= 5
            if target.CurrentHealth <= unit.Attack:
                value += 25
            distance = AIHelper.calculate_distance((unit.get_location()[0], unit.get_location()[1]), target)
            while unit.MinimumRange < distance < unit.MaximumRange:
                value -= 10
                distance -= 1
            i += 1
        return value

    @staticmethod
    def get_terrain_value(battlefield, coordinate):
        value = 0
        tile = battlefield.get_tile(coordinate[0], coordinate[1])
        if tile.altitude != 1:
            value += tile.altitude
        if tile.defenseBoost != 0:
            value += tile.defenseBoost * 5
        if tile.accuracyPenalty != 0:
            value += tile.accuracyPenalty
        return value

    @staticmethod
    def get_at_tile(units, space):
        for unit in units:
            if unit.get_location() == space:
                return unit
        return None

    @staticmethod
    def move_unit(unit, location):
        unit.x = location[0] * Tile.Size
        unit.y = location[1] * Tile.Size

    @staticmethod
    def attack_with_unit(attacking_unit, game_state):
        if CombatHelper.can_attack(attacking_unit, game_state.battlefield, game_state.units, game_state.current_player):
            targets = AIHelper.get_attackable_units(attacking_unit, attacking_unit.get_location(), game_state)
            weakest_target = targets[0]
            for target in targets:
                if target.CurrentHealth < weakest_target.CurrentHealth:
                    weakest_target = target
            target_tile, target_unit = AIHelper.get_target_tile_and_unit(target.get_location(), game_state)
            game_state.ai_attack(target_tile, target_unit)

    @staticmethod
    def calculate_distance(location, target):
        return abs(location[0] - target.get_location()[0]) + abs(location[1] - target.get_location()[1])

    @staticmethod
    def get_shortest_distance(location, enemies):
        shortest_distance = 25
        for enemy in enemies:
            distance = AIHelper.calculate_distance(location, enemy)
            if distance < shortest_distance:
                shortest_distance = distance
        return distance

    @staticmethod
    def get_target_tile_and_unit(target_space, game_state):
        unit = None
        for u in game_state.units:
            if u.x / Tile.Size == target_space[0] and u.y / Tile.Size == target_space[1]:
                unit = u
        tile = game_state.battlefield.tiles[target_space[1]][target_space[0]]
        return tile, unit