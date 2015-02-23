from Battlefield.Tile import *
import pygame.gfxdraw
from CombatHelper import *
from UI.HealthBar import HealthBar

class DrawingHelper():
    inactive_button_color = (160, 160, 160)
    white_color = (255, 255, 255)
    black_color = (0, 0, 0)
    active_button_color = (180, 250, 140)
    selected_button_color = (100, 250, 105)
    selected_unit_color = (150, 150, 150, 100)
    pygame.font.init()
    font = pygame.font.SysFont("monospace", 15)

    def __init__(self):
        pass

    @staticmethod
    def draw_all_the_things(game_state, screen, end_turn, new_turn, move, attack, abilities, inventory, move_helper):
        game_state.battlefield.draw(screen)
        DrawingHelper.draw_end_turn_button(end_turn, screen, game_state)
        if game_state.is_owned_unit_selected():
            if game_state.can_selected_unit_move():
                DrawingHelper.draw_move_button(move, DrawingHelper.active_button_color, screen, game_state)
                DrawingHelper.draw_inventory_button(inventory, DrawingHelper.active_button_color, screen, game_state)
            else:
                DrawingHelper.draw_move_button(move, DrawingHelper.inactive_button_color, screen, game_state)
            if game_state.can_selected_unit_attack():
                DrawingHelper.draw_attack_button(attack, DrawingHelper.active_button_color, screen, game_state)
                DrawingHelper.draw_ability_button(abilities, DrawingHelper.active_button_color, screen, game_state)
                DrawingHelper.draw_inventory_button(inventory, DrawingHelper.active_button_color, screen, game_state)
            else:
                DrawingHelper.draw_attack_button(attack, DrawingHelper.inactive_button_color, screen, game_state)
                DrawingHelper.draw_ability_button(abilities, DrawingHelper.inactive_button_color, screen, game_state)
            if game_state.moving:
                location = game_state.get_selected_unit().get_location()
                DrawingHelper.draw_move_button(move, DrawingHelper.selected_button_color, screen, game_state)
                move_helper.draw_movement_shadow(location[0], location[1], game_state, screen)
            else:
                if game_state.attacking:
                    DrawingHelper.draw_attack_button(attack, DrawingHelper.selected_button_color, screen, game_state)
                    CombatHelper.draw_attack_shadow(game_state.get_selected_unit(), game_state.battlefield, screen,
                                                    DrawingHelper)
            if not game_state.can_selected_unit_attack and not game_state.can_selected_unit_move:
                DrawingHelper.draw_inventory_button(inventory, DrawingHelper.inactive_button_color, screen, game_state)
        else:
            DrawingHelper.draw_move_button(move, DrawingHelper.inactive_button_color, screen, game_state)
            DrawingHelper.draw_attack_button(attack, DrawingHelper.inactive_button_color, screen, game_state)
            DrawingHelper.draw_ability_button(abilities, DrawingHelper.inactive_button_color, screen, game_state)
            DrawingHelper.draw_inventory_button(inventory, DrawingHelper.inactive_button_color, screen, game_state)
        if game_state.selected is not None:
            DrawingHelper.draw_selected_unit_highlight(game_state, screen)
        DrawingHelper.draw_units(game_state, screen)
        DrawingHelper.draw_unit_healthbars(game_state, screen)
        if game_state.between_turns and game_state.current_player == 0:
            DrawingHelper.draw_turn_indicator(game_state, new_turn, screen)
        DrawingHelper.draw_stats(game_state, DrawingHelper.font, screen)
        turn_count_display = DrawingHelper.font.render("Round:" + str(game_state.turn_count), 1,
                                                       DrawingHelper.white_color)
        screen.blit(turn_count_display,
                    (game_state.battlefield.width() * Tile.Size + 13, game_state.battlefield.height() * Tile.Size - 20))
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
        new_turn_height = game_state.battlefield.height() * Tile.Size
        new_turn_width = game_state.battlefield.width() * Tile.Size
        new_turn_y = (game_state.get_window_height() - game_state.button_height - new_turn_height) / 2
        new_turn_x = 0
        button.change_name("It is player " + str(game_state.current_player + 1) + "'s turn")
        DrawingHelper.draw_button(screen, button, DrawingHelper.black_color, new_turn_x, new_turn_y, new_turn_width,
                                  new_turn_height, DrawingHelper.white_color)

    @staticmethod
    def draw_stats(game_state, font, screen):
        pygame.draw.rect(screen, (123, 100, 59),
                         pygame.Rect(game_state.get_window_width() - game_state.button_width, 0,
                                     game_state.button_width, game_state.battlefield.height() * Tile.Size - 2))
        pygame.draw.rect(screen, (113, 90, 49),
                         pygame.Rect(game_state.get_window_width() - game_state.button_width, 0,
                                     game_state.button_width, game_state.battlefield.height() * Tile.Size - 2), 5)
        if game_state.selected is not None:
            unit = game_state.get_selected_unit()
            unit.draw_preview(screen, (game_state.battlefield.width() * Tile.Size + 10, 10), game_state.animation_state,
                              game_state.attacking)
            screen.blit(unit.image, (game_state.battlefield.width() * Tile.Size + 10, 10))
            class_display = font.render(str(unit.name), 1, DrawingHelper.white_color)
            screen.blit(class_display, (game_state.battlefield.width() * Tile.Size + 10, Tile.Size + 10))
            hitpoint_display = font.render("HP: " + str(unit.CurrentHealth) + "/" + str(unit.MaxHealth), 1,
                                           DrawingHelper.white_color)
            screen.blit(hitpoint_display, (game_state.battlefield.width() * Tile.Size + 10, Tile.Size + 38))
            level_display = font.render("LVL: " + str(unit.level), 1, DrawingHelper.white_color)
            screen.blit(level_display, (game_state.battlefield.width() * Tile.Size + 10, Tile.Size + 24))

            if unit.get_team() == game_state.current_player:
                attack_display = font.render("ATK: " + str(unit.Attack), 1, DrawingHelper.white_color)
                screen.blit(attack_display, (game_state.battlefield.width() * Tile.Size + 10, Tile.Size + 52))
                defense_display = font.render("DEF: " + str(unit.Defense), 1, DrawingHelper.white_color)
                screen.blit(defense_display, (game_state.battlefield.width() * Tile.Size + 10, Tile.Size + 66))
                experience_display = font.render("EXP: " + str(unit.experience), 1, DrawingHelper.white_color)
                screen.blit(experience_display, (game_state.battlefield.width() * Tile.Size + 10, Tile.Size + 80))
                next_level_display = font.render("NXT LVL: " + str(unit.next_level_exp), 1, DrawingHelper.white_color)
                screen.blit(next_level_display, (game_state.battlefield.width() * Tile.Size + 10, Tile.Size + 94))


    @staticmethod
    def draw_move_button(button, background_color, screen, game_state):
        DrawingHelper.draw_button(screen, button, background_color, 0,
                                  game_state.get_window_height() - game_state.button_height, game_state.button_width,
                                  game_state.button_height, DrawingHelper.white_color)

    @staticmethod
    def draw_attack_button(button, background_color, screen, game_state):
        DrawingHelper.draw_button(screen, button, background_color, game_state.button_width + 1,
                                  game_state.get_window_height() - game_state.button_height, game_state.button_width,
                                  game_state.button_height, DrawingHelper.white_color)

    @staticmethod
    def draw_ability_button(button, background_color, screen, game_state):
        DrawingHelper.draw_button(screen, button, background_color, (game_state.button_width + 1) * 2,
                                  game_state.get_window_height() - game_state.button_height, game_state.button_width,
                                  game_state.button_height, DrawingHelper.white_color)

    @staticmethod
    def draw_inventory_button(button, background_color, screen, game_state):
        DrawingHelper.draw_button(screen, button, background_color, (game_state.button_width + 1) * 3,
                                  game_state.get_window_height() - game_state.button_height, game_state.button_width,
                                  game_state.button_height, DrawingHelper.white_color)

    @staticmethod
    def draw_end_turn_button(button, screen, game_state):
        DrawingHelper.draw_button(screen, button, (200, 122, 90), (game_state.button_width + 1) * 4,
                                  game_state.get_window_height() - game_state.button_height, game_state.button_width,
                                  game_state.button_height, DrawingHelper.white_color)

    @staticmethod
    def draw_button(screen, button, background_color, x_offset, y_offset, button_width, button_height,
                    text_color):
        button.create_button(screen, background_color, x_offset, y_offset, button_width, button_height, None,
                             text_color)

    @staticmethod
    def draw_selected_unit_highlight(game_state, screen):
        pygame.gfxdraw.box(screen,
                           pygame.Rect(game_state.get_selected_unit().x, game_state.get_selected_unit().y, Tile.Size,
                                       Tile.Size),
                           DrawingHelper.selected_unit_color)

    @staticmethod
    def draw_units(game_state, screen):
        for u in game_state.units:
            u.draw(screen, game_state.animation_state, u in game_state.tapped_units)

    @staticmethod
    def draw_unit_healthbars(game_state, screen):
        for u in game_state.units:
            HealthBar.draw_healthbar(screen, u)
