import pygame.gfxdraw
import UI.Buttons
import Game

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
                    Game.run()


        StartGame.create_button(screen, (50, 80, 200), 300, 150, 200, 100, None, "Start Game", (135, 144, 15))
        pygame.display.update()