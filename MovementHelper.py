from DrawingHelper import *


class MovementHelper():
    def __init__(self):
        pass

    movement_color = (100, 115, 245, 100)

    @staticmethod
    def click_movement(units, battlefield, moving_unit, clicked_space, ):
        if clicked_space in MovementHelper.get_movement_options(moving_unit.get_location()[0],
                                                                moving_unit.get_location()[1], units, moving_unit,
                                                                battlefield, moving_unit.get_movement()):
            moving_unit.x = clicked_space[0] * Tile.Size
            moving_unit.y = clicked_space[1] * Tile.Size

    @staticmethod
    def get_movement_options(x, y, units, current_unit, battlefield, movement):
        options = MovementHelper.get_movement_options_core(x, y, units, current_unit, battlefield, movement, [])
        if any(options):
            for u in units:
                while u.get_location() in options:
                    options.remove(u.get_location())
        return options

    @staticmethod
    def get_movement_options_core(x, y, units, current_unit, battlefield, movement, options):
        if BattlefieldHelper.is_in_bounds(x, y, battlefield) and MovementHelper.is_space_empty(current_unit, units, x,
                                                                                               y):
            options.append((x, y))

            if BattlefieldHelper.is_in_bounds(x + 1, y, battlefield) and movement >= battlefield.tiles[y][
                        x + 1].movementCost:
                MovementHelper.get_movement_options_core(x + 1, y, units, current_unit, battlefield,
                                                         movement - battlefield.tiles[y][x + 1].movementCost, options)
            if BattlefieldHelper.is_in_bounds(x - 1, y, battlefield) and movement >= battlefield.tiles[y][
                        x - 1].movementCost:
                MovementHelper.get_movement_options_core(x - 1, y, units, current_unit, battlefield,
                                                         movement - battlefield.tiles[y][x - 1].movementCost, options)
            if BattlefieldHelper.is_in_bounds(x, y + 1, battlefield) and movement >= battlefield.tiles[y + 1][
                x].movementCost:
                MovementHelper.get_movement_options_core(x, y + 1, units, current_unit, battlefield,
                                                         movement - battlefield.tiles[y + 1][x].movementCost, options)
            if BattlefieldHelper.is_in_bounds(x, y - 1, battlefield) and movement >= battlefield.tiles[y - 1][
                x].movementCost:
                MovementHelper.get_movement_options_core(x, y - 1, units, current_unit, battlefield,
                                                         movement - battlefield.tiles[y - 1][x].movementCost, options)
            return options

    @staticmethod
    def is_space_empty(current_unit, units, x, y):
        empty = True

        for u in units:
            other_unit_location = u.get_location()
            click_location = (x, y)
            if other_unit_location == click_location \
                    and u != current_unit \
                    and u.get_team() != current_unit.get_team():
                empty = False
        return empty

    @staticmethod
    def draw_movement_shadow(x, y, game_state, screen):
        options = MovementHelper.get_movement_options(x, y, game_state.units, game_state.get_selected_unit(),
                                                      game_state.battlefield, game_state.get_selected_unit().Movement)
        DrawingHelper.draw_shadow(options, game_state.battlefield, MovementHelper.movement_color, screen)

