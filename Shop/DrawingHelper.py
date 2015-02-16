from Battlefield.Tile import *
import pygame.gfxdraw


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
    def draw_all_the_things(shop_state, screen, buy, complete):
        DrawingHelper.draw_buy_button(buy, screen, shop_state)
        DrawingHelper.draw_complete_button(complete, screen, shop_state)
        DrawingHelper.draw_roster(shop_state, screen)
        DrawingHelper.draw_stock(shop_state, screen)
        DrawingHelper.draw_stats(shop_state, screen)

        pygame.display.update()


    @staticmethod
    def draw_roster(shop_state, screen):
        pygame.draw.rect(screen, (123, 100, 59),
                         pygame.Rect(shop_state.window_width / 5, shop_state.window_height - shop_state.button_height,
                                     (shop_state.window_width / 5) * 3, shop_state.button_height))
        pygame.draw.rect(screen, (113, 90, 49),
                         pygame.Rect(shop_state.window_width / 5, shop_state.window_height - shop_state.button_height,
                                     (shop_state.window_width / 5) * 3, shop_state.button_height), 5)

        x_offset = shop_state.roster_offset
        y_offset = shop_state.shop_height + (shop_state.button_height - Tile.Size) / 2
        for unit in shop_state.roster:
            unit.draw_preview(screen, (x_offset, y_offset), shop_state.animation_state, True)
            x_offset += shop_state.pedestals[0].size[0]

    @staticmethod
    def draw_stock(shop_state, screen):
        i = 0
        for pedestal in shop_state.pedestals:
            pygame.draw.rect(screen, (123, 100, 59), pedestal)
            pygame.draw.rect(screen, (113, 90, 49), pedestal, 5)
            shop_state.stock[i].draw_preview(screen, (
                (pedestal.left + (pedestal.size[0] - Tile.Size) / 2),
                (pedestal.top + (pedestal.size[0] - Tile.Size) / 2)),
                                             shop_state.animation_state, shop_state.selected == shop_state.stock[i])
            i += 1

    @staticmethod
    def draw_stats(shop_state, screen):
        pygame.draw.rect(screen, (123, 100, 59),
                         pygame.Rect(shop_state.window_width - shop_state.button_width, 0,
                                     shop_state.button_width, shop_state.window_height - shop_state.button_height - 2))
        pygame.draw.rect(screen, (113, 90, 49),
                         pygame.Rect(shop_state.window_width - shop_state.button_width, 0,
                                     shop_state.button_width, shop_state.window_height - shop_state.button_height - 2),
                         5)

        pygame.draw.rect(screen, (123, 100, 59),
                         pygame.Rect(0, 0,
                                     shop_state.button_width, shop_state.window_height - shop_state.button_height - 2))

        pygame.draw.rect(screen, (113, 90, 49),
                         pygame.Rect(0, 0,
                                     shop_state.button_width, shop_state.window_height - shop_state.button_height - 2),
                         5)
        if shop_state.selected is not None:
            unit = shop_state.selected
            status_offset = shop_state.window_width - shop_state.button_width
            unit.draw_preview(screen, (status_offset + 10, 10),
                              shop_state.animation_state, False)
            name_display = DrawingHelper.font.render(str(unit.name), 1, DrawingHelper.white_color)
            screen.blit(name_display, (status_offset + 10, Tile.Size + 10))
            hitpoint_display = DrawingHelper.font.render("HP: " + str(unit.CurrentHealth) + "/" + str(unit.MaxHealth),
                                                         1,
                                                         DrawingHelper.white_color)
            screen.blit(hitpoint_display, (status_offset + 10, Tile.Size + 24))
            attack_display = DrawingHelper.font.render("ATK: " + str(unit.AttackPower), 1, DrawingHelper.white_color)
            screen.blit(attack_display, (status_offset + 10, Tile.Size + 38))
            defense_display = DrawingHelper.font.render("DEF: " + str(unit.Defense), 1, DrawingHelper.white_color)
            screen.blit(defense_display, (status_offset + 10, Tile.Size + 52))

    @staticmethod
    def draw_buy_button(button, screen, shop_state):
        if shop_state.is_stock_selected() and shop_state.can_shop():
            background_color = DrawingHelper.active_button_color
        else:
            background_color = DrawingHelper.inactive_button_color

        DrawingHelper.draw_button(screen, button, background_color, 0,
                                  shop_state.window_height - shop_state.button_height, shop_state.button_width,
                                  shop_state.button_height, DrawingHelper.white_color)

    @staticmethod
    def draw_complete_button(button, screen, shop_state):
        if shop_state.is_draft and shop_state.can_shop():
            background_color = DrawingHelper.active_button_color
        else:
            background_color = DrawingHelper.selected_button_color

        DrawingHelper.draw_button(screen, button, background_color,
                                  shop_state.window_width - shop_state.button_width,
                                  shop_state.window_height - shop_state.button_height, shop_state.button_width,
                                  shop_state.button_height, DrawingHelper.white_color)

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

