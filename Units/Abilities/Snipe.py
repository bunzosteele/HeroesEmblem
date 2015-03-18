from DrawingHelper import *


class Snipe():
    highlight_color = (200, 100, 100, 150)

    def __init__(self):
        pass

    @staticmethod
    def draw_ability_shadow(game_state, screen):
        options = Snipe.get_target_spaces(game_state.selected.get_location(), game_state)
        DrawingHelper.draw_shadow(options, game_state.battlefield, Snipe.highlight_color, screen)

    @staticmethod
    def can_use_ability(unit, game_state):
        return Snipe.is_active()\
               and (not Snipe.is_daily() or not unit.has_used_ability)\
               and (not Snipe.is_targeted() or len(Snipe.get_targets(unit, game_state)) > 0)

    @staticmethod
    def is_valid_target(target_tile, target_unit, unit, game_state):
        return target_unit in Snipe.get_targets(unit, game_state)

    @staticmethod
    def use_ability(target_tile, target_unit, unit, game_state):
        unit.attacking = True
        game_state.selected.attack_start_frame = game_state.animation_state + 1
        damage = unit.Attack
        target_unit.CurrentHealth -= damage
        if target_unit.CurrentHealth <= 0:
            CombatHelper.kill_unit(target_unit, game_state)
        else:
            target_unit.incoming_effect(damage, "Damage")
        unit.has_used_ability = True
        unit.has_acted = True
        return True

    @staticmethod
    def get_ability_name():
        return "Snipe"

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
        options = Snipe.get_target_spaces(unit.get_location(), game_state)
        targets = []
        for target in game_state.units:
            if target.get_location() in options and target.get_team() != unit.get_team():
                targets.append(target)
        return targets

    @staticmethod
    def get_potential_targets(location, team, game_state):
        options = Snipe.get_target_spaces(location, game_state)
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