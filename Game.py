import sys, pygame, os
from pygame.locals import *
from Units.Footman import *

def change_unit(units_length, unit_num):
    if unit_num < units_length - 1:
        unit_num += 1
    else:
        unit_num = 0
    return unit_num

def handle_movement(units, which_unit):
    units[which_unit].movement_clac()
    if units[which_unit].temp_movement == 0:
        units[which_unit].reset_movement()
        which_unit = change_unit(unit_size, which_unit)
    return which_unit

pygame.init()

screen_size = width, height = 900,590
wid = 900/31
hght = 600/31
space_size = 31

backround_color = 255, 255, 255
grid_color = 0, 0, 0
running = True

screen = pygame.display.set_mode(screen_size)
unit1 = Footman(0 , 0, 6)
unit2 = Footman(310, 310, 5)
unit3 = Footman(62, 62, 4)
clock = pygame.time.Clock()

units = [unit1, unit2, unit3]
unit_size = len(units)
which_unit = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP: 
                units[which_unit].move_up()
                which_unit = handle_movement(units, which_unit)
            if event.key == pygame.K_DOWN: 
                units[which_unit].move_down()
                which_unit = handle_movement(units, which_unit)
            if event.key == pygame.K_LEFT: 
                units[which_unit].move_left()
                which_unit = handle_movement(units, which_unit)
            if event.key == pygame.K_RIGHT: 
                units[which_unit].move_right()
                which_unit = handle_movement(units, which_unit)
				

    screen.fill(backround_color)
    unit1.draw(screen)
    unit2.draw(screen)
    unit3.draw(screen)

    for i in range(1, wid):
        pygame.draw.line (screen, grid_color, (space_size*i,0), (space_size*i,height), 1)
        pygame.draw.line (screen, grid_color, (0, space_size*i), (width, space_size*i), 1)
    
    pygame.display.update()

    clock.tick(60)

pygame.quit()
