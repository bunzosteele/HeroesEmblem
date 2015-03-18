from DrawingHelper import *


class Thrust():
    highlight_color = (200, 100, 100, 150)

    def __init__(self):
        pass

    @staticmethod
    def draw_ability_shadow(game_state, screen):
        options = Thrust.get_target_spaces(game_state.selected.get_location(), game_state)
        DrawingHelper.draw_shadow(options, game_state.battlefield, Thrust.highlight_color, screen)

    @staticmethod
    def can_use_ability(unit, game_state):
        return Thrust.is_active()\
               and (not Thrust.is_daily() or not unit.has_used_ability)\
               and (not Thrust.is_targeted() or len(Thrust.get_targets(unit, game_state)) > 0)

    @staticmethod
    def is_valid_target(target_tile, target_unit, unit, game_state):
        return target_unit in Thrust.get_targets(unit, game_state)

    @staticmethod
    def use_ability(target_tile, target_unit, unit, game_state):
        unit.attacking = True
        game_state.selected.attack_start_frame = game_state.animation_state + 1

        x_offset = target_tile[0] - unit.get_location()[0]
        y_offset = target_tile[1] - unit.get_location()[1]

        knockback_space = (target_tile[0] + x_offset, target_tile[1] + y_offset)
        is_blocked_by_terrain = BattlefieldHelper.is_in_bounds(knockback_space[0], knockback_space[1], game_state.battlefield)\
                                and target_unit.Movement < game_state.battlefield.get_tile(knockback_space[0], knockback_space[1]).movementCost
        damage = unit.Attack
        if is_blocked_by_terrain:
            damage = damage * 2

        blocking_unit = None
        for u in game_state.units:
            if u.get_location() == knockback_space:
                blocking_unit = u

        target_unit.CurrentHealth -= damage
        if target_unit.CurrentHealth <= 0:
            CombatHelper.kill_unit(target_unit, game_state)
            unit.x = target_unit.x
            unit.y = target_unit.y
        else:
            target_unit.incoming_effect(damage, "Damage")
            if blocking_unit is None and not is_blocked_by_terrain:
                unit.x = target_unit.x
                unit.y = target_unit.y
                target_unit.x += x_offset * Tile.Size
                target_unit.y += y_offset * Tile.Size

        if blocking_unit is not None:
            blocking_unit.CurrentHealth -= damage
            if blocking_unit.CurrentHealth <= 0:
                CombatHelper.kill_unit(blocking_unit, game_state)
            else:
                blocking_unit.incoming_effect(damage, "Damage")
        unit.has_used_ability = True
        unit.has_acted = True
        return True

    @staticmethod
    def get_ability_name():
        return "Thrust"

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
        options = Thrust.get_target_spaces(unit.get_location(), game_state)
        targets = []
        for target in game_state.units:
            if target.get_location() in options and target.get_team() != unit.get_team():
                targets.append(target)
        return targets

    @staticmethod
    def get_potential_targets(location, team, game_state):
        options = Thrust.get_target_spaces(location, game_state)
        targets = []
        for target in game_state.units:
            if target.get_location() in options and target.get_team() != team:
                targets.append(target)
        return targets

    @staticmethod
    def get_target_spaces(start, game_state):
        targets = []
        if BattlefieldHelper.is_in_bounds(start[0] + 1, start[1], game_state.battlefield):
            targets.append((start[0] + 1, start[1]))
        if BattlefieldHelper.is_in_bounds(start[0] - 1, start[1], game_state.battlefield):
            targets.append((start[0] - 1, start[1]))
        if BattlefieldHelper.is_in_bounds(start[0], start[1] - 1, game_state.battlefield):
            targets.append((start[0], start[1] - 1))
        if BattlefieldHelper.is_in_bounds(start[0], start[1] + 1, game_state.battlefield):
            targets.append((start[0], start[1] + 1))
        return targets