from DrawingHelper import *


class PowerShot():
    highlight_color = (200, 100, 100, 150)

    def __init__(self):
        pass

    @staticmethod
    def draw_ability_shadow(game_state, screen):
        options = PowerShot.get_target_spaces(game_state.selected.get_location(), game_state)
        DrawingHelper.draw_shadow(options, game_state.battlefield, PowerShot.highlight_color, screen)

    @staticmethod
    def can_use_ability(unit, game_state):
        return PowerShot.is_active()\
               and (not PowerShot.is_daily() or not unit.has_used_ability)\
               and (not PowerShot.is_targeted() or len(PowerShot.get_targets(unit, game_state)) > 0)

    @staticmethod
    def is_valid_target(target_tile, target_unit, unit, game_state):
        x_offset = target_tile[0] - unit.get_location()[0]
        if x_offset != 0:
            x_offset = x_offset / abs(unit.get_location()[0] - target_tile[0])
        y_offset = target_tile[1] - unit.get_location()[1]
        if y_offset != 0:
            y_offset = y_offset / abs(unit.get_location()[1] - target_tile[1])
        start = unit.get_location()
        next_tile = (start[0] + x_offset, start[1] + y_offset)
        target_tiles = []
        while BattlefieldHelper.is_in_bounds(next_tile[0], next_tile[1], game_state.battlefield):
            target_tiles.append(next_tile)
            next_tile = (next_tile[0] + x_offset, next_tile[1] + y_offset)

        for unit in game_state.units:
            if unit.get_location() in target_tiles:
                return True
        return False

    @staticmethod
    def use_ability(target_tile, target_unit, unit, game_state):
        unit.attacking = True
        game_state.selected.attack_start_frame = game_state.animation_state + 1
        damage = unit.Attack
        x_offset = target_tile[0] - unit.get_location()[0]
        if x_offset != 0:
            x_offset = x_offset / abs(unit.get_location()[0] - target_tile[0])
        y_offset = target_tile[1] - unit.get_location()[1]
        if y_offset != 0:
            y_offset = y_offset / abs(unit.get_location()[1] - target_tile[1])
        start = unit.get_location()
        next_tile = (start[0] + x_offset, start[1] + y_offset)
        target_tiles = []
        while BattlefieldHelper.is_in_bounds(next_tile[0], next_tile[1], game_state.battlefield):
            target_tiles.append(next_tile)
            next_tile = (next_tile[0] + x_offset, next_tile[1] + y_offset)
        for u in game_state.units:
            if u.get_location() in target_tiles:
                u.CurrentHealth -= damage
                if u.CurrentHealth <= 0:
                    CombatHelper.kill_unit(u, game_state)
                else:
                    u.incoming_effect(damage, "Damage")
        unit.has_used_ability = True
        unit.has_acted = True
        return True

    @staticmethod
    def get_ability_name():
        return "Power Shot"

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
        options = PowerShot.get_target_spaces(unit.get_location(), game_state)
        targets = []
        for target in game_state.units:
            if target.get_location() in options and target.get_team() != unit.get_team():
                targets.append(target)
        return targets

    @staticmethod
    def get_potential_targets(location, team, game_state):
        options = PowerShot.get_target_spaces(location, game_state)
        targets = []
        for target in game_state.units:
            if target.get_location() in options and target.get_team() != team:
                targets.append(target)
        return targets

    @staticmethod
    def get_target_spaces(start, game_state):
        targets = []
        next_tile = (start[0] + 1, start[1])
        starting_altitude = game_state.battlefield.get_tile(start[0], start[1]).Altitude
        while BattlefieldHelper.is_in_bounds(next_tile[0], next_tile[1], game_state.battlefield)\
                and PowerShot.check_altitude(starting_altitude, game_state.battlefield.get_tile(next_tile[0], next_tile[1]).altitude):
            targets.append(next_tile)
            next_tile = (next_tile[0] + 1, next_tile[1])
        next_tile = (start[0] - 1, start[1])
        while BattlefieldHelper.is_in_bounds(next_tile[0], next_tile[1], game_state.battlefield)\
                and PowerShot.check_altitude(starting_altitude, game_state.battlefield.get_tile(next_tile[0], next_tile[1]).altitude):
            targets.append(next_tile)
            next_tile = (next_tile[0] - 1, next_tile[1])
        next_tile = (start[0], start[1] + 1)
        while BattlefieldHelper.is_in_bounds(next_tile[0], next_tile[1], game_state.battlefield)\
                and PowerShot.check_altitude(starting_altitude, game_state.battlefield.get_tile(next_tile[0], next_tile[1]).altitude):
            targets.append(next_tile)
            next_tile = (next_tile[0], next_tile[1] + 1)
        next_tile = (start[0], start[1] - 1)
        while BattlefieldHelper.is_in_bounds(next_tile[0], next_tile[1], game_state.battlefield)\
                and PowerShot.check_altitude(starting_altitude, game_state.battlefield.get_tile(next_tile[0], next_tile[1]).altitude):
            targets.append(next_tile)
            next_tile = (next_tile[0], next_tile[1] - 1)
        return targets

    @staticmethod
    def check_altitude(start, target):
        if target > start:
            return False
        return True