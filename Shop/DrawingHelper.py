from Battlefield.Tile import *
import pygame.gfxdraw


class DrawingHelper():
    inactive_button_color = (160, 160, 160)
    white_color = (255, 255, 255)
    red_color = (255, 150, 150)
    gold_color = (255, 215, 0)
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
        DrawingHelper.draw_shop_data(shop_state, screen)
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

            if shop_state.selected in shop_state.stock:
                cost_display = pygame.font.SysFont("monospace", 32).render(str(shop_state.selected.Cost), 1,
                                                                           DrawingHelper.white_color)
                screen.blit(cost_display, (status_offset + 42, 10))

            font_color = DrawingHelper.white_color
            if unit.MaxHealth > unit.Type.BaseMaxHealth:
                font_color = DrawingHelper.gold_color

            if unit.MaxHealth < unit.Type.BaseMaxHealth:
                font_color = DrawingHelper.red_color

            hitpoint_display = DrawingHelper.font.render("HP: " + str(unit.CurrentHealth) + "/" + str(unit.MaxHealth),
                                                         1,
                                                         font_color)
            screen.blit(hitpoint_display, (status_offset + 10, Tile.Size + 24))

            font_color = DrawingHelper.white_color
            if unit.Attack > unit.Type.BaseAttack:
                font_color = DrawingHelper.gold_color

            if unit.Attack < unit.Type.BaseAttack:
                font_color = DrawingHelper.red_color
            attack_display = DrawingHelper.font.render("ATK: " + str(unit.Attack), 1, font_color)
            screen.blit(attack_display, (status_offset + 10, Tile.Size + 38))

            font_color = DrawingHelper.white_color
            if unit.Defense > unit.Type.BaseDefense:
                font_color = DrawingHelper.gold_color

            if unit.Defense < unit.Type.BaseDefense:
                font_color = DrawingHelper.red_color
            defense_display = DrawingHelper.font.render("DEF: " + str(unit.Defense), 1, font_color)
            screen.blit(defense_display, (status_offset + 10, Tile.Size + 52))

            font_color = DrawingHelper.white_color
            if unit.Evasion > unit.Type.BaseEvasion:
                font_color = DrawingHelper.gold_color

            if unit.Evasion < unit.Type.BaseEvasion:
                font_color = DrawingHelper.red_color
            evasion_display = DrawingHelper.font.render("EVP: " + str(unit.Evasion), 1, font_color)
            screen.blit(evasion_display, (status_offset + 10, Tile.Size + 64))

            font_color = DrawingHelper.white_color
            if unit.Accuracy > unit.Type.BaseAccuracy:
                font_color = DrawingHelper.gold_color

            if unit.Accuracy < unit.Type.BaseAccuracy:
                font_color = DrawingHelper.red_color
            accuracy_display = DrawingHelper.font.render("ACC: " + str(unit.Accuracy), 1, font_color)
            screen.blit(accuracy_display, (status_offset + 10, Tile.Size + 78))

            font_color = DrawingHelper.white_color
            if unit.Movement > unit.Type.BaseMovement:
                font_color = DrawingHelper.gold_color

            if unit.Movement < unit.Type.BaseMovement:
                font_color = DrawingHelper.red_color
            movement_display = DrawingHelper.font.render("MOVE: " + str(unit.Movement), 1, font_color)
            screen.blit(movement_display, (status_offset + 10, Tile.Size + 92))

            movement_display = DrawingHelper.font.render("Hails from:", 1, DrawingHelper.white_color)
            screen.blit(movement_display, (status_offset + 10, Tile.Size + 106))
            movement_display = DrawingHelper.font.render(str(unit.hometown), 1, DrawingHelper.gold_color)
            screen.blit(movement_display, (status_offset + 10, Tile.Size + 120))
            movement_display = DrawingHelper.font.render("Likes:", 1, DrawingHelper.white_color)
            screen.blit(movement_display, (status_offset + 10, Tile.Size + 134))
            movement_display = DrawingHelper.font.render(str(unit.like), 1, DrawingHelper.gold_color)
            screen.blit(movement_display, (status_offset + 10, Tile.Size + 148))
            movement_display = DrawingHelper.font.render("Dislikes:", 1, DrawingHelper.white_color)
            screen.blit(movement_display, (status_offset + 10, Tile.Size + 162))
            movement_display = DrawingHelper.font.render(str(unit.dislike), 1, DrawingHelper.gold_color)
            screen.blit(movement_display, (status_offset + 10, Tile.Size + 176))
            movement_display = DrawingHelper.font.render("Hobby:", 1, DrawingHelper.white_color)
            screen.blit(movement_display, (status_offset + 10, Tile.Size + 190))
            movement_display = DrawingHelper.font.render(str(unit.hobby), 1, DrawingHelper.gold_color)
            screen.blit(movement_display, (status_offset + 10, Tile.Size + 204))
    @staticmethod
    def draw_shop_data(shop_state, screen):
        screen.blit(pygame.image.load(DrawingHelper.resource_path("images/Shopkeeper.png")), (10, 10))
        screen.blit(pygame.image.load(DrawingHelper.resource_path("images/gold.png")),
                    (10, shop_state.window_height - (shop_state.button_height + 42)))
        gold_display = pygame.font.SysFont("monospace", 32).render(str(shop_state.gold), 1, DrawingHelper.gold_color)
        screen.blit(gold_display, (42, shop_state.window_height - (shop_state.button_height + 42)))


    @staticmethod
    def draw_buy_button(button, screen, shop_state):
        if shop_state.is_stock_selected() and shop_state.can_buy_selected():
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
    def resource_path(relative):
        return os.path.join(
            os.environ.get(
                "_MEIPASS2",
                os.path.abspath(".")
            ),
            relative
        )

