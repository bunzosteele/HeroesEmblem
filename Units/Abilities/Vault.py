from DrawingHelper import *


class Vault():
    highlight_color = (100, 100, 200, 150)

    def __init__(self):
        pass

    @staticmethod
    def draw_ability_shadow(game_state, screen):
        options = Vault.get_target_spaces(game_state.selected.get_location(), game_state)
        DrawingHelper.draw_shadow(options, game_state.battlefield, Vault.highlight_color, screen)

    @staticmethod
    def can_use_ability(unit, game_state):
        return Vault.is_active() \
               and (not Vault.is_daily() or not unit.has_used_ability) \
               and (not Vault.is_targeted() or len(Vault.get_targets(unit, game_state)) > 0)

    @staticmethod
    def is_valid_target(target_tile, target_unit, unit, game_state):
        return target_tile in Vault.get_targets(unit, game_state)

    @staticmethod
    def use_ability(target_tile, target_unit, unit, game_state):
        unit.x = target_tile[0] * Tile.Size
        unit.y = target_tile[1] * Tile.Size
        unit.has_acted = True
        unit.has_used_ability = True
        return True

    @staticmethod
    def get_ability_name():
        return "Vault"

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
        return Vault.get_target_spaces(unit.get_location(), game_state)

    @staticmethod
    def get_potential_targets(location, team, game_state):
        return Vault.get_target_spaces(location, game_state)

    @staticmethod
    def get_target_spaces(start, game_state):
        targets = []
        x_offset = -2
        y_offset = -2
        while x_offset <= 2:
            while y_offset <= 2:
                if not (abs(x_offset) <= 1 and abs(y_offset) <= 1):
                    next_tile = (start[0] + x_offset, start[1] + y_offset)
                    if BattlefieldHelper.is_in_bounds(next_tile[0], next_tile[1], game_state.battlefield) and \
                        Vault.check_target(game_state.selected, game_state.battlefield.get_tile(next_tile[0], next_tile[1])):
                            targets.append(next_tile)
                y_offset += 1
            x_offset += 1
            y_offset = -2
        return targets

    @staticmethod
    def check_target(unit, tile):
        return unit.Movement >= tile.movementCost