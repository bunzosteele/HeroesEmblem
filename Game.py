import random
import pygame.gfxdraw
import UI.Buttons
from Units.Footman import *
from Units.Mage import *
from Battlefield.Battlefield import *
from Battlefield.Tile import *

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

def click_movement(units, tapped_units, battlefield, moving_unit, clicked_space, selected):
    if clicked_space in get_movement_options(x, y, units, moving_unit, battlefield, moving_unit.get_movement()):
        moving_unit.x = clicked_space[0]* Tile.Size
        moving_unit.y = clicked_space[1]* Tile.Size
        tapped_units.append(moving_unit)
    selected = None
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
        if any(options) and u.get_location in options:
            options = filter(lambda x: x != u.get_location(), options)
    return options

def get_movement_options_core(x, y, units, current_unit, battlefield, movement, options):
    if is_in_bounds(x, y, battlefield) and is_space_empty(current_unit, units, x, y):
        options.append((x, y))

        if is_in_bounds(x + 1, y, battlefield) and movement >= battlefield.tiles[y][x+1].movementCost:
            get_movement_options_core(x + 1, y, units, current_unit, battlefield, movement - battlefield.tiles[y][x+1].movementCost, options)
        if is_in_bounds(x - 1, y, battlefield) and movement >= battlefield.tiles[y][x-1].movementCost:
            get_movement_options_core(x - 1, y, units, current_unit, battlefield, movement - battlefield.tiles[y][x-1].movementCost, options)
        if is_in_bounds(x, y + 1, battlefield) and movement >= battlefield.tiles[y+1][x].movementCost:
            get_movement_options_core(x, y + 1, units, current_unit, battlefield, movement - battlefield.tiles[y+1][x].movementCost, options)
        if is_in_bounds(x, y - 1, battlefield) and movement >= battlefield.tiles[y-1][x].movementCost:
            get_movement_options_core(x, y - 1, units, current_unit, battlefield, movement - battlefield.tiles[y-1][x].movementCost, options)
        return options

def is_in_bounds(x, y, battlefield):
    return x < battlefield.width() and y < battlefield.height() and x >= 0 and y >=0


def is_space_empty(current_unit, units, x, y):
    empty = True

    for u in units:
        other_unit_location = u.get_location()
        click_location = (x, y)
        if other_unit_location == click_location\
                and u != current_unit\
                and u.get_team() != current_unit.get_team():
            empty = False

    return empty

def end_turn(player):
    if player == 1:
        player = 2
    elif player == 2:
        player = 1
    return player

def draw_turn_indicator(pixel_height, pixel_width, button_height, current_player):
    NewTurnHeight = 100
    NewTurnWidth = 250
    NewTurnY = (pixel_height - button_height - NewTurnHeight) / 2
    NewTurnX = (pixel_width - NewTurnWidth) / 2
    NewTurn.create_button(screen, (0, 0, 0), NewTurnX, NewTurnY, NewTurnWidth, NewTurnHeight, 100, "It is player " + str(current_player) + "'s turn", (255,255,255))

def get_at(clicked_space, battlefield, units):
    unit = None
    for u in units:
        if u.x / Tile.Size == clicked_space[0] and u.y / Tile.Size == clicked_space[1]:
            unit = u

    tile = battlefield.tiles[clicked_space[1]][clicked_space[0]]

    return (tile, unit)




pygame.init()
running = True
button_height = 50
current_player = 1
between_turns = True

#battlefieldSeed = random.randint(1, 6)
battlefieldSeed = 2
battlefield = Battlefield(Battlefield.build("Battlefield/"+ `battlefieldSeed` + ".txt"))

pixel_width = len(battlefield.tiles[0]) * Tile.Size
pixel_height = len(battlefield.tiles) * Tile.Size + button_height
screen_size = width, height = pixel_width, pixel_height
screen = pygame.display.set_mode(screen_size)
battlefield.draw(screen)
selected_color = (100, 115, 245, 100)

unit1 = Footman(0, 0, 1)
unit2 = Mage(2, 2, 1)
unit3 = Mage(7, 6, 2)
unit4 = Footman(12, 4, 2)

clock = pygame.time.Clock()

units = [unit1, unit2, unit3, unit4]
tapped_units = []
unit_size = len(units)
selected = None

EndTurn = UI.Buttons.Button()
NewTurn = UI.Buttons.Button()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if between_turns:
                if NewTurn.pressed(pos):
                    between_turns = False
                    tapped_units = []
            elif EndTurn.pressed(pos):
                    current_player = end_turn(current_player)
                    between_turns = True
                    selected = None
            else:
                clicked_space = (pos[0]/Tile.Size, pos[1]/Tile.Size)
                if selected is not None and units[selected].get_location() == clicked_space:
                    selected = None
                elif selected is not None and get_at(clicked_space, battlefield, units)[1] is not None and get_at(clicked_space, battlefield, units)[1].get_team() == current_player:
                    selection = get_at(clicked_space, battlefield, units)[1]
                    if selection not in tapped_units:
                        selected = units.index(selection)
                elif selected is not None:
                    selected = click_movement(units, tapped_units, battlefield, units[selected], clicked_space, selected)
                else:
                    for unit in units:
                        if clicked_space == unit.get_location() and unit.get_team() == current_player and unit not in tapped_units:
                            selected = units.index(unit)
                            break
                        else:
                            selected = None

    battlefield.draw(screen)

    if selected is not None:
        location = units[selected].get_location()
        x, y = location[0], location[1]
        draw_shadow(x, y, units, units[selected],  battlefield, selected_color, Tile.Size, units[selected].movement, screen)

    for u in units :
        u.draw(screen)

    EndTurn.create_button\
        (screen, (200, 122, 90), 0, pixel_height - button_height,
         pixel_width, button_height, 100, "End Turn", (255,255,255))
    if(between_turns):
        draw_turn_indicator(pixel_height, pixel_width, button_height, current_player)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
