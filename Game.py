import random
import pygame.gfxdraw
from Units.Footman import *
from Battlefield.Battlefield import *
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

def click_movement(units, which_unit, clicked_space, selected):
    unit_x = units[which_unit].x/Tile.Size
    unit_y = units[which_unit].y/Tile.Size
    click_x = clicked_space[0]
    click_y = clicked_space[1]
    total_distance = abs((unit_x - click_x)) + abs((unit_y - click_y))
    if total_distance <= units[which_unit].movement:
        units[which_unit].x = click_x*Tile.Size
        units[which_unit].y = click_y*Tile.Size
        selected = False
    return selected

def draw_shadow(x, y, selected_color, tile_size, movement, screen):
    temp_x = x * tile_size
    temp_y = y * tile_size
    if x < len(battlefield.tiles[0]) and y < len(battlefield.tiles):
        battlefield.tiles[y][x].draw(screen, x, y)
        pygame.gfxdraw.box(screen, pygame.Rect(temp_x, temp_y, Tile.Size, Tile.Size), selected_color)
    if movement != 0:
        draw_shadow(x + 1, y, selected_color, tile_size, movement - 1, screen)
        draw_shadow(x - 1, y, selected_color, tile_size, movement - 1, screen)
        draw_shadow(x, y + 1, selected_color, tile_size, movement - 1, screen)
        draw_shadow(x, y - 1, selected_color, tile_size, movement - 1, screen)


pygame.init()
running = True

battlefieldSeed = random.randint(1, 6)
battlefield = Battlefield(Battlefield.build("Battlefield/"+ `battlefieldSeed` + ".txt"))

pixelWidth = len(battlefield.tiles[0]) * Tile.Size
pixelHeight = len(battlefield.tiles) * Tile.Size
screen_size = width, height = pixelWidth, pixelHeight
screen = pygame.display.set_mode(screen_size)
battlefield.draw(screen)
selected_color = (100, 115, 245, 100)

unit1 = Footman(0, 0, 4)

clock = pygame.time.Clock()

units = [unit1]
unit_size = len(units)
which_unit = 0
selected = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked_space = (pos[0]/Tile.Size, pos[1]/Tile.Size)
            if selected:
                selected = click_movement(units, which_unit, clicked_space, selected)
            else:
                for i in range(0, unit_size):
                    if clicked_space == units[i].get_location():
                        selected = True
                        which_unit = i
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

    if selected:
        location = units[which_unit].get_location()
        x, y = location[0], location[1]
        draw_shadow(x, y, selected_color, Tile.Size, units[which_unit].movement, screen)
    unit1.draw(screen)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
