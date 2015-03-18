from DrawingHelper import *


class Rebirth():
    highlight_color = (20, 200, 20, 150)

    def __init__(self):
        pass

    @staticmethod
    def draw_ability_shadow(game_state, screen):
        options = Rebirth.get_target_spaces(game_state.selected.get_location(), game_state)
        DrawingHelper.draw_shadow(options, game_state.battlefield, Rebirth.highlight_color, screen)

    @staticmethod
    def can_use_ability(unit, game_state):
        return Rebirth.is_active()\
               and (not Rebirth.is_daily() or not unit.has_used_ability)\
               and (not Rebirth.is_targeted() or len(Rebirth.get_targets(unit, game_state)) > 0)

    @staticmethod
    def is_valid_target(target_tile, target_unit, unit, game_state):
        return target_unit in Rebirth.get_targets(unit, game_state)

    @staticmethod
    def use_ability(target_tile, target_unit, unit, game_state):
        unit.attacking = True
        game_state.selected.attack_start_frame = game_state.animation_state + 1
        heal = target_unit.MaxHealth
        target_unit.heal_damage(heal)
        target_unit.incoming_effect(heal, "Heal")
        target_unit.experience /= 2
        unit.has_used_ability = True
        unit.has_acted = True
        return True

    @staticmethod
    def get_ability_name():
        return "Rebirth"

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
        options = Rebirth.get_target_spaces(unit.get_location(), game_state)
        targets = []
        for target in game_state.units:
            if target.get_location() in options\
                    and target.get_team() == unit.get_team()\
                    and target.CurrentHealth < target.MaxHealth:
                targets.append(target)
        return targets

    @staticmethod
    def get_potential_targets(location, team, game_state):
        options = Rebirth.get_target_spaces(location, game_state)
        targets = []
        for target in game_state.units:
            if target.get_location() in options\
                    and target.get_team() == team\
                    and target.CurrentHealth < target.MaxHealth:
                targets.append(target)
        return targets

    @staticmethod
    def get_target_spaces(start, game_state):
        targets = []
        if BattlefieldHelper.is_in_bounds(start[0], start[1], game_state.battlefield):
            targets.append((start[0], start[1]))
        if BattlefieldHelper.is_in_bounds(start[0] + 1, start[1], game_state.battlefield):
            targets.append((start[0] + 1, start[1]))
        if BattlefieldHelper.is_in_bounds(start[0] - 1, start[1], game_state.battlefield):
            targets.append((start[0] - 1, start[1]))
        if BattlefieldHelper.is_in_bounds(start[0], start[1] - 1, game_state.battlefield):
            targets.append((start[0], start[1] - 1))
        if BattlefieldHelper.is_in_bounds(start[0], start[1] + 1, game_state.battlefield):
            targets.append((start[0], start[1] + 1))
        return targets