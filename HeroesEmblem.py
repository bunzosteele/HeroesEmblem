import pygame.gfxdraw
import UI.Buttons

pygame.init()
pygame.display.set_caption("Heroes Emblem")

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

StartGame = UI.Buttons.Button()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if StartGame.pressed(pos):
                pass

    StartGame.create_button(screen, (50, 80, 200), 00, 150, 200, 100, None, "Start Game", (255, 255, 255))