from Battlefield.Tile import *
from CombatHelper import *

class DrawingHelper():

    inactive_button_color = (160, 160, 160)
    white_color = (255, 255, 255)
    black_color = (0, 0, 0)
    active_button_color = (180, 250, 140)
    selected_button_color = (100, 250, 105)
    selected_unit_color = (150, 150, 150, 100)
    font = pygame.font.SysFont("monospace", 15)

    def __init__(self):
        pass

    @staticmethod
    def draw_all_the_things(game_state, screen, end_turn, new_turn, move, attack, movement_helper):
        game_state.battlefield.draw(screen)
        DrawingHelper.draw_end_turn_button(end_turn, screen, game_state)
        if game_state.is_owned_unit_selected():
            DrawingHelper.draw_move_button(move, DrawingHelper.active_button_color, screen, game_state)
            location = game_state.get_selected_unit().get_location()
            if game_state.can_selected_unit_attack():
                DrawingHelper.draw_attack_button(attack, DrawingHelper.active_button_color, screen, game_state)
            if game_state.moving:
                DrawingHelper.draw_move_button(move, DrawingHelper.selected_button_color, screen, game_state)
                movement_helper.draw_movement_shadow(location[0], location[1], game_state, screen)
            else:
                if game_state.attacking:
                    DrawingHelper.draw_attack_button(attack, DrawingHelper.selected_button_color, screen, game_state)
                    CombatHelper.draw_attack_shadow(game_state.get_selected_unit(), game_state.battlefield, screen, DrawingHelper)
        else:
            DrawingHelper.draw_move_button(move, DrawingHelper.inactive_button_color, screen, game_state)
            DrawingHelper.draw_attack_button(attack, DrawingHelper.inactive_button_color, screen, game_state)
        if game_state.selected is not None:
            DrawingHelper.draw_selected_unit_highlight(game_state, screen)
        DrawingHelper.draw_units(game_state, screen)
        if game_state.between_turns:
            DrawingHelper.draw_turn_indicator(game_state, new_turn, screen)
        DrawingHelper.draw_stats(game_state, DrawingHelper.font, screen)
        turn_count_display = DrawingHelper.font.render("Round:" + str(game_state.turn_count), 1, DrawingHelper.white_color)
        screen.blit(turn_count_display, (game_state.battlefield.width() * Tile.Size + 13, game_state.battlefield.height() * Tile.Size - 20))
        pygame.display.update()

    @staticmethod
    def draw_shadow(options, battlefield, selected_color, screen):
        for option in options:
            temp_x = option[0] * Tile.Size
            temp_y = option[1] * Tile.Size
            battlefield.tiles[option[1]][option[0]].draw(screen, option[0], option[1])
            pygame.gfxdraw.box(screen, pygame.Rect(temp_x, temp_y, Tile.Size, Tile.Size), selected_color)

    @staticmethod
    def draw_turn_indicator(game_state, button, screen):
        new_turn_height = 100
        new_turn_width = 250
        new_turn_y = (game_state.get_window_height() - game_state.button_height - new_turn_height) / 2
        new_turn_x = (game_state.get_window_width() - new_turn_width) / 2
        DrawingHelper.draw_button(screen, button, DrawingHelper.black_color, new_turn_x, new_turn_y, new_turn_width, new_turn_height,
                          "It is player " + str(game_state.current_player + 1) + "'s turn", DrawingHelper.white_color)

    @staticmethod
    def draw_stats(game_state, font, screen):
        pygame.draw.rect(screen, (123, 100, 59),
            pygame.Rect(game_state.get_window_width() - game_state.status_width, 0, game_state.status_width, game_state.battlefield.height() * Tile.Size - 2))
        pygame.draw.rect(screen, (113, 90, 49),
            pygame.Rect(game_state.get_window_width() - game_state.status_width, 0, game_state.status_width, game_state.battlefield.height() * Tile.Size - 2), 5)
        if game_state.selected is not None:
            unit = game_state.get_selected_unit()
            screen.blit(unit.image, (game_state.battlefield.width() * Tile.Size + 10, 10))
            class_display = font.render(str(unit.Type), 1, DrawingHelper.white_color)
            screen.blit(class_display, (game_state.battlefield.width() * Tile.Size + 10, Tile.Size + 10))
            hitpoint_display = font.render("HP: " + str(unit.CurrentHealth) + "/" + str(unit.MaxHealth), 1, DrawingHelper.white_color)
            screen.blit(hitpoint_display, (game_state.battlefield.width() * Tile.Size + 10, Tile.Size + 24))
            attack_display = font.render("ATK: " + str(unit.AttackPower), 1, DrawingHelper.white_color)
            screen.blit(attack_display, (game_state.battlefield.width() * Tile.Size + 10, Tile.Size + 38))
            defense_display = font.render("DEF: " + str(unit.Defense), 1, DrawingHelper.white_color)
            screen.blit(defense_display, (game_state.battlefield.width() * Tile.Size + 10, Tile.Size + 52))

    @staticmethod
    def draw_end_turn_button(button, screen, game_state):
        DrawingHelper.draw_button(screen, button, (200, 122, 90), (game_state.button_width + 1) * 2,
            game_state.get_window_height() - game_state.button_height, game_state.button_width, game_state.button_height, "End Turn", DrawingHelper.white_color)

    @staticmethod
    def draw_move_button(button, background_color, screen, game_state):
        DrawingHelper.draw_button(screen, button, background_color, 0,
             game_state.get_window_height() - game_state.button_height, game_state.button_width, game_state.button_height, "Move", DrawingHelper.white_color)

    @staticmethod
    def draw_attack_button(button, background_color, screen, game_state):
        DrawingHelper.draw_button(screen, button, background_color, game_state.button_width + 1,
             game_state.get_window_height() - game_state.button_height, game_state.button_width, game_state.button_height, "Attack", DrawingHelper.white_color)


    @staticmethod
    def draw_button(screen, button, background_color, x_offset, y_offset, button_width, button_height, text, text_color):
        button.create_button(screen, background_color, x_offset, y_offset, button_width, button_height, None, text, text_color)

    @staticmethod
    def draw_selected_unit_highlight(game_state, screen):
        pygame.gfxdraw.box(screen, pygame.Rect(game_state.get_selected_unit().x, game_state.get_selected_unit().y, Tile.Size, Tile.Size),
                                   DrawingHelper.selected_unit_color)

    @staticmethod
    def draw_units(game_state, screen):
        for u in game_state.units:
            u.draw(screen, game_state.animation_state)

