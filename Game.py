import sys, pygame, os
from pygame.locals import *
from Units.Footman import *
from Battlefield.Battlefield import *
from Battlefield.Tile import *
from Battlefield.Grass import *
from Battlefield.Mountain import *

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


backround_color = 100, 100, 100
grid_color = 0, 0, 0
running = True

battlefield = Battlefield([
	[Mountain(), Mountain(), Mountain(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass()],
	[Mountain(), Mountain(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass()],
	[Mountain(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass()],
	[Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass()],
	[Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass()],
	[Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass()],
	[Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Mountain()],
	[Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Mountain(), Mountain()],
	[Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Grass(), Mountain(), Mountain(), Mountain()]])

pixelWidth = len(battlefield.tiles[0]) * Tile.Size
pixelHeight = len(battlefield.tiles) * Tile.Size
screen_size = width, height = pixelWidth, pixelHeight
screen = pygame.display.set_mode(screen_size)
battlefield.draw(screen)

unit1 = Footman(0 , 0, 6)

clock = pygame.time.Clock()

units = [unit1]
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
				
	battlefield.draw(screen)
    unit1.draw(screen)
    
    pygame.display.update()

    clock.tick(60)

pygame.quit()
