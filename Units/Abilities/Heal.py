from DrawingHelper import *


class Heal():
    highlight_color = (20, 200, 20)

    def __init__(self):
        pass

    @staticmethod
    def draw_ability_shadow(unit, battlefield, screen):
        options = Heal.get_target_spaces(unit.get_location())
        DrawingHelper.draw_shadow(options, battlefield, Heal.highlight_color, screen)

    @staticmethod
    def can_use_ability(unit, game_state):
        return Heal.is_active()\
               and (not Heal.is_daily() or not unit.has_used_ability)\
               and (not Heal.is_targeted() or len(Heal.get_targets(unit, game_state)) > 0)

    @staticmethod
    def is_valid_target(target_tile, target_unit, unit, game_state):
        return target_unit in Heal.get_targets(unit, game_state)

    @staticmethod
    def use_ability(target_tile, target_unit, unit, game_state):
        unit.attacking = True
        game_state.selected.attack_start_frame = game_state.animation_state + 1
        heal = CombatHelper.heal(target_unit, unit)
        target_unit.incoming_damage(heal, True)
        unit.has_used_ability = True
        unit.has_acted = True

    @staticmethod
    def get_ability_name():
        return "Heal"

    @staticmethod
    def is_daily():
        return False

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_targeted():
        return True

    @staticmethod
    def get_targets(unit, game_state):
        options = Heal.get_target_spaces(unit.get_location())
        targets = []
        for target in game_state.units:
            if target.get_location() in options\
                    and target.get_team() == unit.get_team()\
                    and target.CurrentHealth < target.MaxHealth:
                targets.append(target)
        return targets

    @staticmethod
    def get_potential_targets(location, team, game_state):
        options = Heal.get_target_spaces(location)
        targets = []
        for target in game_state.units:
            if target.get_location() in options\
                    and target.get_team() == team\
                    and target.CurrentHealth < target.MaxHealth:
                targets.append(target)
        return targets

    @staticmethod
    def get_target_spaces(start):
        return [(start[0] + 1, start[1]), (start[0] - 1, start[1]), (start[0], start[1] + 1),
                   (start[0], start[1] - 1)]
