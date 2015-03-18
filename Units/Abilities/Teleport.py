from DrawingHelper import *


class Teleport():
    highlight_color = (200, 100, 200, 150)
    teleporting_unit = None

    def __init__(self):
        pass

    @staticmethod
    def draw_ability_shadow(game_state, screen):
        options = Teleport.get_target_spaces(game_state.selected.get_location(), game_state)
        DrawingHelper.draw_shadow(options, game_state.battlefield, Teleport.highlight_color, screen)

    @staticmethod
    def can_use_ability(unit, game_state):
        return Teleport.is_active()\
               and (not Teleport.is_daily() or not unit.has_used_ability)\
               and (not Teleport.is_targeted() or len(Teleport.get_targets(unit, game_state)) > 0)

    @staticmethod
    def is_valid_target(target_tile, target_unit, unit, game_state):
        if Teleport.teleporting_unit is None:
            return target_unit in Teleport.get_targets(unit, game_state)
        else:
            return target_tile in Teleport.get_target_spaces(Teleport.teleporting_unit.get_location(), game_state)

    @staticmethod
    def use_ability(target_tile, target_unit, unit, game_state):
        if Teleport.teleporting_unit is None:
            Teleport.teleporting_unit = target_unit
            return False
        else:
            unit.attacking = True
            game_state.selected.attack_start_frame = game_state.animation_state + 1
            Teleport.teleporting_unit.x = target_tile[0] * Tile.Size
            Teleport.teleporting_unit.y = target_tile[1] * Tile.Size
            Teleport.teleporting_unit
            unit.has_used_ability = True
            unit.has_acted = True
            return True

    @staticmethod
    def get_ability_name():
        return "Teleport"

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
        options = Teleport.get_target_spaces(unit.get_location(), game_state)
        targets = []
        for target in game_state.units:
            if target.get_location() in options:
                targets.append(target)
        return targets


    @staticmethod
    def get_potential_targets(location, team, game_state):
        if Teleport.teleporting_unit is None:
            options = Teleport.get_target_spaces(location, game_state)
            targets = []
            for target in game_state.units:
                if target.get_location() in options:
                    targets.append(target)
            return targets

    @staticmethod
    def get_target_spaces(start, game_state):
        if Teleport.teleporting_unit is None:
            targets = []
            for unit in game_state.units:
                targets.append(unit.get_location())
            return targets
        else:
            targets = []
            y_index = 0
            for y in game_state.battlefield.tiles:
                x_index = 0
                for tile in y:
                    if Teleport.teleporting_unit.Movement >= tile.movementCost:
                        targets.append((x_index, y_index))
                    x_index += 1
                y_index += 1
            for unit in game_state.units:
                if unit.get_location() in targets:
                    targets.remove(unit.get_location())
            return targets