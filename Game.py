import sys, pygame, os
from pygame.locals import *
from Unit import *
        
pygame.init()

screen_size = width, height = 900,590
wid = 900/31
hght = 600/31

backround_color = 255, 255, 255
grid_color = 0, 0, 0
running = True

screen = pygame.display.set_mode(screen_size)
unit1 = Unit("images/Luigi.jpg", 0 , 0)
unit2 = Unit("images/Puff.png", 310, 310)
unit3 = Unit("images/Knight.jpg", 62, 62)
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP: 
                unit1.move_up()
                unit2.move_up()
                unit3.move_up()
            if event.key == pygame.K_DOWN: 
                unit1.move_down()
                unit2.move_down()
                unit3.move_down()
            if event.key == pygame.K_LEFT: 
                unit1.move_left() 
                unit2.move_left() 
                unit3.move_left() 
            if event.key == pygame.K_RIGHT: 
                unit1.move_right()
                unit2.move_right()
                unit3.move_right()
				

    screen.fill(backround_color)
    unit1.draw(screen)
    unit2.draw(screen)
    unit3.draw(screen)

    for i in range(1, wid):
        pygame.draw.line (screen, grid_color, (31*i,0), (31*i,600), 1)
        pygame.draw.line (screen, grid_color, (0, 31*i), (900, 31*i), 1)
    
    pygame.display.update()

    clock.tick(60)

pygame.quit()
