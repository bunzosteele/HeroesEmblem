from Battlefield.Battlefield import *
from FileReader import *
from GameState import GameState
from Shop import Shop
from Shop.ShopState import ShopState
from StoryGenerator import StoryGenerator
import UI.Buttons
import Battle
import pygame

def launch_game():
    StoryGenerator.create_story()
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
    RestartGame = UI.Buttons.Button("YOU SHOULDNT SEE THIS")
    running = True
    not_lost = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if StartGame.pressed(pos) or (not_lost == False and RestartGame.pressed(pos)):
                    rounds_survived = 0
                    difficulty = 1
                    gold = 5000
                    units = []
                    not_lost = True

                    while not_lost:
                        chosen_field = FileReader.generate_battlefield(difficulty)
                        difficulty -= int(chosen_field)
                        game_result = launch_game()
                        not_lost = game_result[0]
                        if not_lost:
                            rounds_survived += 1
                        difficulty += int(chosen_field)
                        gold -= game_result[1]
                        gold += difficulty * 50
                        difficulty += rounds_survived

                    font = pygame.font.SysFont("monospace", 32)

                    RestartGame.change_name("Rounds Survived: " + str(rounds_survived))
                    RestartGame.create_button(screen, (0, 0, 0), 0, 0, (32 * 16) * 1.25, (32 * 9) + 50, None,
                                              (255, 255, 255))
        if not_lost:
            StartGame.create_button(screen, (50, 80, 200), ((32 * 16) - 100) / 2, ((32 * 9) - 50) / 2, 200, 100, None,
                                    (135, 144, 15))
        pygame.display.update()


