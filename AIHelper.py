from MovementHelper import *


class AIHelper():
    def __init__(self):
        pass

    @staticmethod
    def play_turn(game_state):
        ai_units = AIHelper.get_ai_units(game_state)
        invalid_units = AIHelper.get_player_units(game_state)
        while len(ai_units) > 0:
            units_with_options = AIHelper.get_options(game_state, ai_units, invalid_units)
            highest_priority_unit = units_with_options[0]
            for unit_with_options in units_with_options:
                if unit_with_options[1][1] > highest_priority_unit[1][1]:
                    highest_priority_unit = unit_with_options

            conflicted_unit = AIHelper.get_at_tile(ai_units, highest_priority_unit[1][0][0])
            if conflicted_unit is None or conflicted_unit == highest_priority_unit[0]:
                AIHelper.move_unit(highest_priority_unit[0], highest_priority_unit[1][0][0])
                ai_units.remove(highest_priority_unit[0])
                invalid_units.append(highest_priority_unit[0])
            else:
                conflicted_unit_with_options = None
                for unit_with_options in units_with_options:
                    if unit_with_options[0] == conflicted_unit:
                        conflicted_unit_with_options = unit_with_options

                next_conflicted_unit = AIHelper.get_at_tile(ai_units, conflicted_unit_with_options[1][0][0])
                while next_conflicted_unit is not None:
                    conflicted_unit_with_options[1].remove(conflicted_unit_with_options[1][0])
                    next_conflicted_unit = AIHelper.get_at_tile(ai_units, conflicted_unit_with_options[1][0][0])
                AIHelper.move_unit(conflicted_unit_with_options[0], conflicted_unit_with_options[1][0][0])
                AIHelper.move_unit(highest_priority_unit[0], highest_priority_unit[1][0][0])
                ai_units.remove(highest_priority_unit[0])
                ai_units.remove(conflicted_unit_with_options[0])
                invalid_units.append(highest_priority_unit[0])
                invalid_units.append(conflicted_unit_with_options[0])

    @staticmethod
    def get_ai_units(game_state):
        units = []
        for unit in game_state.units:
            if unit.get_team() == 1:
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
            options = MovementHelper.get_movement_options(unit.get_location()[0], unit.get_location()[1], invalid_units, unit,
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
        # TODO actual logic
        return randint(1, 100)

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