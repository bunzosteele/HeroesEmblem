import random
import pygame.gfxdraw
import UI.Buttons
from Units.Footman import *
from Units.Mage import *
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

def click_movement(units, battlefield, moving_unit, clicked_space, selected):
    if clicked_space in get_movement_options(x, y, units, moving_unit, battlefield, moving_unit.get_movement()):
         moving_unit.x = clicked_space[0]*Tile.Size
         moving_unit.y = clicked_space[1]*Tile.Size
         selected = False
    return selected

def draw_shadow(x, y, units, current_unit,  battlefield, selected_color, tile_size, movement, screen):
    options = get_movement_options(x, y, units, current_unit, battlefield, movement)
    for option in options:
        temp_x = option[0] * tile_size
        temp_y = option[1] * tile_size
        battlefield.tiles[option[1]][option[0]].draw(screen, option[0], option[1])
        pygame.gfxdraw.box(screen, pygame.Rect(temp_x, temp_y, Tile.Size, Tile.Size), selected_color)

def get_movement_options(x, y, units, current_unit, battlefield, movement):
    options = get_movement_options_core(x, y, units, current_unit, battlefield, movement, [])
    for u in units:
        if u.get_location() in options:
            options = filter(lambda x: x != u.get_location(), options)
    return options

def get_movement_options_core(x, y, units, current_unit, battlefield, movement, options):
    if not (not (x < len(battlefield.tiles[0])) or not (y < len(battlefield.tiles)) or not (x >= 0)
            or not (y >= 0) or not is_space_empty(current_unit, units, battlefield, x, y)):
        options.append((x, y))
        if movement != 0:
            get_movement_options_core(x + 1, y, units, current_unit, battlefield, movement - 1, options)
            get_movement_options_core(x - 1, y, units, current_unit, battlefield, movement - 1, options)
            get_movement_options_core(x, y + 1, units, current_unit, battlefield, movement - 1, options)
            get_movement_options_core(x, y - 1, units, current_unit, battlefield, movement - 1, options)
        return options

def is_space_empty(current_unit, units, battlefield, x, y):
    empty = True
    tile = battlefield.getTile(x, y)
    if tile.solid:
        empty = False

    for u in units:
        other_unit_location = u.get_location()
        click_location = (x, y)
        if other_unit_location == click_location\
                and not u == current_unit\
                and not u.get_team() == current_unit.get_team():
            empty = False

    return empty

def end_turn(player):
    if player == 1:
        player = 2
    elif player == 2:
        player = 1
    print "It is player " + str(player) + "'s turn."
    return player

pygame.init()
running = True
button_height = 50
current_player = 1

#battlefieldSeed = random.randint(1, 6)
battlefieldSeed = 1
battlefield = Battlefield(Battlefield.build("Battlefield/"+ `battlefieldSeed` + ".txt"))

pixel_width = len(battlefield.tiles[0]) * Tile.Size
pixel_height = len(battlefield.tiles) * Tile.Size + button_height
screen_size = width, height = pixel_width, pixel_height
screen = pygame.display.set_mode(screen_size)
battlefield.draw(screen)
selected_color = (100, 115, 245, 100)

unit1 = Footman(0, 0, 4, 1)
unit2 = Mage(2, 2, 3, 1)
unit3 = Mage(7, 6, 6, 2)
unit4 = Footman(12, 4, 1, 2)

clock = pygame.time.Clock()

units = [unit1, unit2, unit3, unit4]
unit_size = len(units)
which_unit = 0
selected = False

EndTurn = UI.Buttons.Button()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if EndTurn.pressed(pos):
                    current_player = end_turn(current_player)
            else:
                clicked_space = (pos[0]/Tile.Size, pos[1]/Tile.Size)
                if selected:
                    selected = click_movement(units, battlefield, units[which_unit], clicked_space, selected)
                else:
                    for i in range(0, unit_size):
                        if clicked_space == units[i].get_location() and units[i].get_team() == current_player:
                            selected = True
                            which_unit = i

    battlefield.draw(screen)

    if selected:
        location = units[which_unit].get_location()
        x, y = location[0], location[1]
        draw_shadow(x, y, units, units[which_unit],  battlefield, selected_color, Tile.Size, units[which_unit].movement, screen)

    for u in units :
        u.draw(screen)

    EndTurn.create_button(screen, (200,122,90), 0, pixel_height - button_height, pixel_width, button_height, 100, "End Turn", (255,255,255))
    pygame.display.update()

    clock.tick(60)

pygame.quit()
