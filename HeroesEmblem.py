from Battlefield.Battlefield import *
from GameState import GameState
import UI.Buttons
import Game
from Units.Footman import *
from Units.Mage import *
from Units.Knight import *
from Units.Archer import *

def launch_game():
    battlefield = Battlefield(Battlefield.build("Battlefield/2.txt"))
    units = [Archer(4, 4, 0), Archer(6, 4, 1), Footman(7, 4, 1), Footman(2, 4, 0), Knight(4, 3, 0), Knight(6, 3, 1),
             Mage(7, 3, 1), Mage(2, 3, 0)]
    button_height = 50
    status_width = 100
    game_state = GameState(battlefield, button_height, status_width, units)
    battle_screen = pygame.display.set_mode((game_state.get_window_width(), game_state.get_window_height()))
    Game.run(battle_screen, game_state)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Heroes Emblem")

    screen = pygame.display.set_mode((800, 400))

    clock = pygame.time.Clock()

    StartGame = UI.Buttons.Button("Start Game")
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if StartGame.pressed(pos):
                    launch_game()

        StartGame.create_button(screen, (50, 80, 200), 300, 150, 200, 100, None, (135, 144, 15))
        pygame.display.update()


