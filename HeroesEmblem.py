from Battlefield.Battlefield import *
from FileReader import *
from GameState import GameState
from Shop import Shop
from Shop.ShopState import ShopState
import UI.Buttons
import Battle
import pygame


def launch_game():
    button_height = 50
    battlefield = Battlefield(Battlefield.build("Battlefield/" + chosen_field + ".txt"))
    shop_state = ShopState(units, button_height, difficulty, gold, battlefield.get_enemy_spawn_count())
    shopping_screen = pygame.display.set_mode((shop_state.window_width, shop_state.window_height))
    shop_result = Shop.run(shopping_screen, shop_state)
    for unit in shop_result[0]:
        if unit not in units:
            units.append(unit)
    game_state = GameState(battlefield, button_height, units)
    battle_screen = pygame.display.set_mode((game_state.get_window_width(), game_state.get_window_height()))
    survivors = Battle.run(battle_screen, game_state)

    if is_game_over(survivors):
        return False, shop_result[1]

    return True, shop_result[1]


def is_game_over(survivors):
    for survivor in survivors:
        if survivor.get_team() == 0:
            return False
    return True


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Heroes Emblem")

    screen = pygame.display.set_mode(((32 * 16) + 100, (32 * 9) + 50))
    StartGame = UI.Buttons.Button("Start Game")
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if StartGame.pressed(pos):
                    difficulty = 1
                    gold = 5000
                    units = []
                    while running:
                        chosen_field = FileReader.generate_battlefield(difficulty)
                        difficulty -= int(chosen_field)
                        game_result = launch_game()
                        gold -= game_result[1]
                        gold += difficulty * 50
                        difficulty += 1
                        running = game_result[0]

        StartGame.create_button(screen, (50, 80, 200), ((32 * 16) - 100) / 2, ((32 * 9) - 50) / 2, 200, 100, None,
                                (135, 144, 15))
        pygame.display.update()


