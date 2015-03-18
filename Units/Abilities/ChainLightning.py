from DrawingHelper import *


class ChainLightning():
    highlight_color = (200, 100, 100, 150)

    def __init__(self):
        pass

    @staticmethod
    def draw_ability_shadow(game_state, screen):
        options = ChainLightning.get_target_spaces(game_state.selected.get_location(), game_state)
        DrawingHelper.draw_shadow(options, game_state.battlefield, ChainLightning.highlight_color, screen)

    @staticmethod
    def can_use_ability(unit, game_state):
        return ChainLightning.is_active()\
               and (not ChainLightning.is_daily() or not unit.has_used_ability)\
               and (not ChainLightning.is_targeted() or len(ChainLightning.get_targets(unit, game_state)) > 0)

    @staticmethod
    def is_valid_target(target_tile, target_unit, unit, game_state):
        return target_unit in ChainLightning.get_targets(unit, game_state)

    @staticmethod
    def use_ability(target_tile, target_unit, unit, game_state):
        unit.attacking = True
        game_state.selected.attack_start_frame = game_state.animation_state + 1
        damage = unit.Attack
        damaged_units = []
        while damage > 0 and target_unit is not None:
            target_unit.CurrentHealth -= damage
            damaged_units.append(target_unit)
            if target_unit.CurrentHealth <= 0:
                CombatHelper.kill_unit(target_unit, game_state)
            else:
                target_unit.incoming_damage(str(damage), False)
            damage /= 2
            target_unit = ChainLightning.get_next_target(game_state.units, damaged_units, target_unit)
        unit.has_used_ability = True
        unit.has_acted = True
        return True

    @staticmethod
    def get_next_target(units, damaged_units, previous_target):
        next_target = None
        for unit in units:
            if unit not in damaged_units:
                if next_target is None \
                        or ChainLightning.calculate_distance(previous_target.get_location(), unit.get_location()) \
                                < ChainLightning.calculate_distance(previous_target.get_location(), next_target.get_location()):
                    next_target = unit
        return next_target

    @staticmethod
    def calculate_distance(start, finish):
        return abs(start[0] - finish[0]) + abs(start[1] - finish[1])

    @staticmethod
    def get_ability_name():
        return "Chain Light"

    @staticmethod
    def is_daily():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_targeted():
        return True

    @staticmethod
    def get_targets(unit, game_state):
        options = ChainLightning.get_target_spaces(unit.get_location(), game_state)
        targets = []
        for target in game_state.units:
            if target.get_location() in options and target.get_team() != unit.get_team():
                targets.append(target)
        return targets

    @staticmethod
    def get_potential_targets(location, team, game_state):
        options = ChainLightning.get_target_spaces(location, game_state)
        targets = []
        for target in game_state.units:
            if target.get_location() in options and target.get_team() != team:
                targets.append(target)
        return targets

    @staticmethod
    def get_target_spaces(start, game_state):
        targets = []
        for unit in game_state.units:
            if unit.get_team() != game_state.selected.get_team():
                targets.append(unit.get_location())
        return targets