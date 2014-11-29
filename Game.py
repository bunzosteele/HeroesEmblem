import random
import pygame.gfxdraw
import UI.Buttons
from Units.Footman import *
from Units.Mage import *
from Units.Knight import *
from Units.Spearman import *
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

def draw_movement_shadow(x, y, units, current_unit,  battlefield, selected_color, tile_size, movement, screen):
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

def can_attack(attacker, battlefield, enemies):
    startingPosition = attacker.get_location()
    maxRangeOptions = get_attack_options(startingPosition[0], startingPosition[1], attacker.get_maximumRange(), battlefield, 0, [])
    minimumRangeOptions = get_attack_options(startingPosition[0], startingPosition[1], attacker.get_minimumRange(), battlefield, 0, [])
    options = []
    for option in maxRangeOptions:
        if option not in minimumRangeOptions:
            options.append(option)

    for enemy in enemies:
        if enemy.get_location() in options:
            return True

    return False

def draw_attack_shadow(attacker, battlefield, selected_color, screen):
    startingPosition = attacker.get_location()
    maxRangeOptions = get_attack_options(startingPosition[0], startingPosition[1], attacker.get_maximumRange(), battlefield, 0, [])
    minimumRangeOptions = get_attack_options(startingPosition[0], startingPosition[1], attacker.get_minimumRange(), battlefield, 0, [])
    options = []
    for option in maxRangeOptions:
        if option not in minimumRangeOptions:
            options.append(option)

    for option in options:
        temp_x = option[0] * Tile.Size
        temp_y = option[1] * Tile.Size
        battlefield.tiles[option[1]][option[0]].draw(screen, option[0], option[1])
        pygame.gfxdraw.box(screen, pygame.Rect(temp_x, temp_y, Tile.Size, Tile.Size), selected_color)

def get_attack_options(x, y, range, battlefield, distance, options):
    if is_in_bounds(x, y, battlefield) and distance <= range:
        options.append((x,y))

        get_attack_options(x + 1, y, range, battlefield, distance+1, options)
        get_attack_options(x - 1, y, range, battlefield, distance+1, options)
        get_attack_options(x, y + 1, range, battlefield, distance+1, options)
        get_attack_options(x, y - 1, range, battlefield, distance+1, options)
    return options


pygame.init()
running = True
c_EndTurnButtonHeight = 50
c_EndTurnPixelWidth = 150
current_player = 1
between_turns = True

#battlefieldSeed = random.randint(1, 6)
battlefieldSeed = 2
battlefield = Battlefield(Battlefield.build("Battlefield/"+ `battlefieldSeed` + ".txt"))

WindowPixelWidth = battlefield.width() * Tile.Size
WindowPixelHeight = battlefield.height() * Tile.Size + c_EndTurnButtonHeight
screen_size = width, height = WindowPixelWidth, WindowPixelHeight
screen = pygame.display.set_mode(screen_size)
battlefield.draw(screen)
movement_color = (100, 115, 245, 100)
selected_color = (150, 150, 150, 100)
attack_color = (200, 100, 100, 150)

unit1 = Footman(0, 0, 1)
unit2 = Mage(2, 2, 1)
unit3 = Mage(2, 3, 2)
unit4 = Footman(12, 4, 2)
unit5 = Knight(4, 5, 1)
unit6 = Knight(11, 4, 2)
unit7 = Spearman(1, 1, 1)
unit8 = Spearman(3, 6, 2)


clock = pygame.time.Clock()

units = [unit1, unit2, unit3, unit4, unit5, unit6, unit7, unit8]
tapped_units = []
unit_size = len(units)
selected = None
moving = False
attacking = False

EndTurn = UI.Buttons.Button()
NewTurn = UI.Buttons.Button()
Move = UI.Buttons.Button()
Attack = UI.Buttons.Button()

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
                    moving = False
                    current_player = end_turn(current_player)
                    between_turns = True
                    selected = None
            elif Move.pressed(pos):
                if selected is not None:
                    moving = not moving
            elif Attack.pressed(pos):
                if selected is not None:
                    moving = False
                    attacking = not attacking
            else:
                clicked_space = (pos[0]/Tile.Size, pos[1]/Tile.Size)
                if selected is not None and units[selected].get_location() == clicked_space:
                    selected = None
                    moving = False
                    attacking = False
                elif selected is not None and get_at(clicked_space, battlefield, units)[1] is not None\
                        and get_at(clicked_space, battlefield, units)[1].get_team() == current_player:
                    selection = get_at(clicked_space, battlefield, units)[1]
                    if selection not in tapped_units:
                        selected = units.index(selection)
                        moving = False
                        attacking = False
                elif selected is not None and moving:
                    selected = click_movement(units, tapped_units, battlefield, units[selected], clicked_space, selected)
                    moving = False
                    attacking = False
                else:
                    for unit in units:
                        if clicked_space == unit.get_location() and unit.get_team() == current_player and unit not in tapped_units:
                            selected = units.index(unit)
                            moving = False
                            attacking = False
                            break
                        else:
                            selected = None
                            moving = False
                            attacking = False

    battlefield.draw(screen)

    EndTurn.create_button\
        (screen, (200, 122, 90), WindowPixelWidth- c_EndTurnPixelWidth, WindowPixelHeight - c_EndTurnButtonHeight,
         c_EndTurnPixelWidth, c_EndTurnButtonHeight, None, "End Turn", (255,255,255))

    Move.create_button(screen, (160, 160, 160), 0, WindowPixelHeight - c_EndTurnButtonHeight,
        (WindowPixelWidth - c_EndTurnPixelWidth)/2, c_EndTurnButtonHeight, None, "Move", (255,255,255))
    Attack.create_button(screen, (160, 160, 160), (WindowPixelWidth - c_EndTurnPixelWidth)/2, WindowPixelHeight - c_EndTurnButtonHeight,
        (WindowPixelWidth - c_EndTurnPixelWidth)/2 + 1, c_EndTurnButtonHeight, None, "Attack", (255,255,255))


    if selected is not None:
        Move.create_button(screen, (180, 250, 140), 0, WindowPixelHeight - c_EndTurnButtonHeight,
            (WindowPixelWidth - c_EndTurnPixelWidth)/2, c_EndTurnButtonHeight, None, "Move", (255,255,255))
        location = units[selected].get_location()
        x, y = location[0], location[1]

        enemies = []
        for unit in units:
            if unit.get_team() != current_player:
                enemies.append(unit)
        if(can_attack(units[selected], battlefield, enemies)):
            Attack.create_button(screen, (180, 250, 140), (WindowPixelWidth - c_EndTurnPixelWidth)/2, WindowPixelHeight - c_EndTurnButtonHeight,
                (WindowPixelWidth - c_EndTurnPixelWidth)/2 + 1, c_EndTurnButtonHeight, None, "Attack", (255,255,255))

        if(moving):
            Move.create_button(screen, (100, 250, 105), 0, WindowPixelHeight - c_EndTurnButtonHeight,
                (WindowPixelWidth - c_EndTurnPixelWidth)/2, c_EndTurnButtonHeight, None, "Move", (255,255,255))
            draw_movement_shadow(x, y, units, units[selected],  battlefield, movement_color, Tile.Size, units[selected].movement, screen)
        else:
            if(attacking):
                Attack.create_button(screen, (100, 250, 105), (WindowPixelWidth - c_EndTurnPixelWidth)/2, WindowPixelHeight - c_EndTurnButtonHeight,
                    (WindowPixelWidth - c_EndTurnPixelWidth)/2 + 1, c_EndTurnButtonHeight, None, "Attack", (255,255,255))
                draw_attack_shadow(units[selected], battlefield, attack_color, screen)
            else:
                pygame.gfxdraw.box(screen, pygame.Rect(units[selected].x, units[selected].y, Tile.Size, Tile.Size), selected_color)


    for u in units :
        u.draw(screen)

    if(between_turns):
        draw_turn_indicator(WindowPixelHeight, WindowPixelWidth, c_EndTurnButtonHeight, current_player)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
