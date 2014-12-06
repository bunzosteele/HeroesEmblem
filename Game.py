import random
import pygame.gfxdraw
import UI.Buttons
from Units.Footman import *
from Units.Mage import *
from Units.Knight import *
from Units.Spearman import *
from Units.Archer import *
from Battlefield.Battlefield import *
from Battlefield.Tile import *

windowX = 1400
windowY = -640
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (windowX, windowY)


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
        moving_unit.x = clicked_space[0] * Tile.Size
        moving_unit.y = clicked_space[1] * Tile.Size
    selected = None
    return selected


def draw_movement_shadow(x, y, units, current_unit, battlefield, selected_color, tile_size, movement, screen):
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

        if is_in_bounds(x + 1, y, battlefield) and movement >= battlefield.tiles[y][x + 1].movementCost:
            get_movement_options_core(x + 1, y, units, current_unit, battlefield,
                                      movement - battlefield.tiles[y][x + 1].movementCost, options)
        if is_in_bounds(x - 1, y, battlefield) and movement >= battlefield.tiles[y][x - 1].movementCost:
            get_movement_options_core(x - 1, y, units, current_unit, battlefield,
                                      movement - battlefield.tiles[y][x - 1].movementCost, options)
        if is_in_bounds(x, y + 1, battlefield) and movement >= battlefield.tiles[y + 1][x].movementCost:
            get_movement_options_core(x, y + 1, units, current_unit, battlefield,
                                      movement - battlefield.tiles[y + 1][x].movementCost, options)
        if is_in_bounds(x, y - 1, battlefield) and movement >= battlefield.tiles[y - 1][x].movementCost:
            get_movement_options_core(x, y - 1, units, current_unit, battlefield,
                                      movement - battlefield.tiles[y - 1][x].movementCost, options)
        return options


def is_in_bounds(x, y, battlefield):
    return x < battlefield.width() and y < battlefield.height() and x >= 0 and y >= 0


def is_space_empty(current_unit, units, x, y):
    empty = True

    for u in units:
        other_unit_location = u.get_location()
        click_location = (x, y)
        if other_unit_location == click_location \
                and u != current_unit \
                and u.get_team() != current_unit.get_team():
            empty = False

    return empty


def end_turn(player, turnCount):
    if player == 0:
        player = 1
    elif player == 1:
        player = 0
    return player


def draw_turn_indicator(pixel_height, pixel_width, button_height, current_player):
    NewTurnHeight = 100
    NewTurnWidth = 250
    NewTurnY = (pixel_height - button_height - NewTurnHeight) / 2
    NewTurnX = (pixel_width - NewTurnWidth) / 2
    NewTurn.create_button(screen, (0, 0, 0), NewTurnX, NewTurnY, NewTurnWidth, NewTurnHeight, 100,
                          "It is player " + str(current_player + 1) + "'s turn", (255, 255, 255))


def get_at(clicked_space, battlefield, units):
    unit = None
    for u in units:
        if u.x / Tile.Size == clicked_space[0] and u.y / Tile.Size == clicked_space[1]:
            unit = u

    tile = battlefield.tiles[clicked_space[1]][clicked_space[0]]

    return (tile, unit)


def can_attack(attacker, battlefield, units):
    enemies = []
    for unit in units:
        if unit.get_team() != current_player:
            enemies.append(unit)
    startingPosition = attacker.get_location()
    maxRangeOptions = get_attack_options(startingPosition[0], startingPosition[1], attacker.get_maximumRange(),
                                         battlefield.tiles[startingPosition[1]][startingPosition[0]].Altitude,
                                         battlefield, 0, [])
    minimumRangeOptions = get_attack_options(startingPosition[0], startingPosition[1], attacker.get_minimumRange(),
                                             battlefield.tiles[startingPosition[1]][startingPosition[0]].Altitude,
                                             battlefield, 0, [])
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
    maxRangeOptions = get_attack_options(startingPosition[0], startingPosition[1], attacker.get_maximumRange(),
                                         battlefield.tiles[startingPosition[1]][startingPosition[0]].Altitude,
                                         battlefield, 0, [])
    minimumRangeOptions = get_attack_options(startingPosition[0], startingPosition[1], attacker.get_minimumRange(),
                                             battlefield.tiles[startingPosition[1]][startingPosition[0]].Altitude,
                                             battlefield, 0, [])
    options = []
    for option in maxRangeOptions:
        if option not in minimumRangeOptions:
            options.append(option)

    for option in options:
        temp_x = option[0] * Tile.Size
        temp_y = option[1] * Tile.Size
        battlefield.tiles[option[1]][option[0]].draw(screen, option[0], option[1])
        pygame.gfxdraw.box(screen, pygame.Rect(temp_x, temp_y, Tile.Size, Tile.Size), selected_color)


def get_attack_options(x, y, range, attackerAltitude, battlefield, distance, options):
    if is_in_bounds(x, y, battlefield) and distance <= range:
        options.append((x, y))

        if attackerAltitude >= battlefield.tiles[y][x].Altitude:
            get_attack_options(x + 1, y, range, attackerAltitude, battlefield, distance + 1, options)
            get_attack_options(x - 1, y, range, attackerAltitude, battlefield, distance + 1, options)
            get_attack_options(x, y + 1, range, attackerAltitude, battlefield, distance + 1, options)
            get_attack_options(x, y - 1, range, attackerAltitude, battlefield, distance + 1, options)
    return options


def nextAnimation(animationState):
    if (animationState == 3):
        return 1
    else:
        return animationState + 1


def drawStats(unit, battlefield, surface):
    surface.blit(unit.image, (battlefieldWidth, 10))
    classDisplay = myFont.render(str(unit.Type), 1, (255, 255, 255))
    screen.blit(classDisplay, (battlefield.width() * Tile.Size + 10, Tile.Size + 10))
    hitpointDisplay = myFont.render("HP: " + str(unit.CurrentHealth) + "/" + str(unit.MaxHealth), 1, (255, 255, 255))
    screen.blit(hitpointDisplay, (battlefield.width() * Tile.Size + 10, Tile.Size + 24))
    attackDisplay = myFont.render("ATK: " + str(unit.AttackPower), 1, (255, 255, 255))
    screen.blit(attackDisplay, (battlefield.width() * Tile.Size + 10, Tile.Size + 38))
    defenseDisplay = myFont.render("DEF: " + str(unit.Defense), 1, (255, 255, 255))
    screen.blit(defenseDisplay, (battlefield.width() * Tile.Size + 10, Tile.Size + 52))



pygame.init()
pygame.display.set_caption("Heroes Emblem")
running = True
c_EndTurnButtonHeight = 50
c_EndTurnPixelWidth = 150
c_StatusWindowWidth = 100
myFont = pygame.font.SysFont("monospace", 15)
current_player = 0
between_turns = True

# battlefieldSeed = random.randint(1, 6)
battlefieldSeed = 2
battlefield = Battlefield(Battlefield.build("Battlefield/" + `battlefieldSeed` + ".txt"))

WindowPixelWidth = battlefield.width() * Tile.Size + c_StatusWindowWidth
WindowPixelHeight = battlefield.height() * Tile.Size + c_EndTurnButtonHeight
screen_size = width, height = WindowPixelWidth, WindowPixelHeight
screen = pygame.display.set_mode(screen_size)
battlefield.draw(screen)
movement_color = (100, 115, 245, 100)
selected_color = (150, 150, 150, 100)
attack_color = (200, 100, 100, 150)

unit1 = Archer(4, 4, 0)
unit2 = Archer(6, 4, 1)
unit3 = Footman(7, 4, 1)
unit4 = Footman(2, 4, 0)
unit5 = Knight(4, 3, 0)
unit6 = Knight(6, 3, 1)
unit7 = Mage(7, 3, 1)
unit8 = Mage(2, 3, 0)

clock = pygame.time.Clock()
animationState = 1
animationTimer = pygame.time.set_timer(pygame.USEREVENT, 500)

units = [unit1, unit2, unit3, unit4, unit5, unit6, unit7, unit8]
tapped_units = []
unit_size = len(units)
previously_moved = None
selected = None
moving = False
attacking = False
turnCount = 1

EndTurn = UI.Buttons.Button()
NewTurn = UI.Buttons.Button()
Move = UI.Buttons.Button()
Attack = UI.Buttons.Button()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            animationState = nextAnimation(animationState)
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if between_turns:
                if NewTurn.pressed(pos):
                    between_turns = False
                    tapped_units = []
                    previously_moved = None
            elif EndTurn.pressed(pos):
                moving = False
                current_player = end_turn(current_player, turnCount)
                if current_player == 0:
                    turnCount += 1
                between_turns = True
                selected = None
            elif Move.pressed(pos):
                if selected is not None:
                    moving = not moving
            elif Attack.pressed(pos):
                if selected is not None and can_attack(units[selected], battlefield, units):
                    moving = False
                    attacking = not attacking
            else:
                clicked_space = (pos[0] / Tile.Size, pos[1] / Tile.Size)
                if selected is not None and units[selected].get_location() == clicked_space:
                    selected = None
                    moving = False
                    attacking = False
                elif selected is not None and get_at(clicked_space, battlefield, units)[1] is not None \
                        and get_at(clicked_space, battlefield, units)[1].get_team() == current_player:
                    selection = get_at(clicked_space, battlefield, units)[1]
                    if selection not in tapped_units:
                        selected = units.index(selection)
                        moving = False
                        attacking = False
                elif selected is not None and moving:
                    movingUnit = units[selected]
                    current_location = movingUnit.get_location()
                    newSelected = click_movement(units, tapped_units, battlefield, movingUnit, clicked_space, selected)
                    new_location = movingUnit.get_location()
                    moving = False
                    canAttack = can_attack(movingUnit, battlefield, units)
                    if (canAttack):
                        attacking = canAttack
                        previously_moved = movingUnit
                    else:
                        selected = newSelected
                    if (selected is None and current_location != new_location):
                        tapped_units.append(movingUnit)
                elif selected is not None and attacking:
                    #TODO IMPLEMENT ATTACKING
                    attacking_unit = units[selected]
                    moving = False
                    attacking = not attacking
                    if attacking_unit == previously_moved:
                        tapped_units.append(attacking_unit)
                    selected = None

                else:
                    for unit in units:
                        if clicked_space == unit.get_location() and unit not in tapped_units:
                            selected = units.index(unit)
                            moving = False
                            attacking = False
                            break
                        else:
                            selected = None
                            moving = False
                            attacking = False

    battlefield.draw(screen)

    EndTurn.create_button \
        (screen, (200, 122, 90), WindowPixelWidth - c_EndTurnPixelWidth, WindowPixelHeight - c_EndTurnButtonHeight,
         c_EndTurnPixelWidth, c_EndTurnButtonHeight, None, "End Turn", (255, 255, 255))

    Move.create_button(screen, (160, 160, 160), 0, WindowPixelHeight - c_EndTurnButtonHeight,
                       (WindowPixelWidth - c_EndTurnPixelWidth) / 2, c_EndTurnButtonHeight, None, "Move",
                       (255, 255, 255))
    Attack.create_button(screen, (160, 160, 160), (WindowPixelWidth - c_EndTurnPixelWidth) / 2,
                         WindowPixelHeight - c_EndTurnButtonHeight,
                         (WindowPixelWidth - c_EndTurnPixelWidth) / 2 + 1, c_EndTurnButtonHeight, None, "Attack",
                         (255, 255, 255))

    if selected is not None and units[selected].get_team() == current_player:
        Move.create_button(screen, (180, 250, 140), 0, WindowPixelHeight - c_EndTurnButtonHeight,
                           (WindowPixelWidth - c_EndTurnPixelWidth) / 2, c_EndTurnButtonHeight, None, "Move",
                           (255, 255, 255))
        location = units[selected].get_location()
        x, y = location[0], location[1]

        if (can_attack(units[selected], battlefield, units)):
            Attack.create_button(screen, (180, 250, 140), (WindowPixelWidth - c_EndTurnPixelWidth) / 2,
                                 WindowPixelHeight - c_EndTurnButtonHeight,
                                 (WindowPixelWidth - c_EndTurnPixelWidth) / 2 + 1, c_EndTurnButtonHeight, None,
                                 "Attack", (255, 255, 255))

        if (moving):
            Move.create_button(screen, (100, 250, 105), 0, WindowPixelHeight - c_EndTurnButtonHeight,
                               (WindowPixelWidth - c_EndTurnPixelWidth) / 2, c_EndTurnButtonHeight, None, "Move",
                               (255, 255, 255))
            draw_movement_shadow(x, y, units, units[selected], battlefield, movement_color, Tile.Size,
                                 units[selected].Movement, screen)
        else:
            if (attacking):
                Attack.create_button(screen, (100, 250, 105), (WindowPixelWidth - c_EndTurnPixelWidth) / 2,
                                     WindowPixelHeight - c_EndTurnButtonHeight,
                                     (WindowPixelWidth - c_EndTurnPixelWidth) / 2 + 1, c_EndTurnButtonHeight, None,
                                     "Attack", (255, 255, 255))
                draw_attack_shadow(units[selected], battlefield, attack_color, screen)

    if selected is not None:
        pygame.gfxdraw.box(screen, pygame.Rect(units[selected].x, units[selected].y, Tile.Size, Tile.Size),
                                   selected_color)


    for u in units:
        if (u in tapped_units):
            u.draw(screen, 1, True)
        else:
            u.draw(screen, animationState, False)

    if (between_turns):
        draw_turn_indicator(WindowPixelHeight, WindowPixelWidth, c_EndTurnButtonHeight, current_player)

    pygame.draw.rect(screen, (123, 100, 59), pygame.Rect(WindowPixelWidth - c_StatusWindowWidth, 0, c_StatusWindowWidth,
                                                         battlefield.height() * Tile.Size - 2))
    pygame.draw.rect(screen, (113, 90, 49), pygame.Rect(WindowPixelWidth - c_StatusWindowWidth, 0, c_StatusWindowWidth,
                                                        battlefield.height() * Tile.Size - 2), 5)
    if (selected is not None):
        drawStats(units[selected], battlefield, screen)
    turnCountDisplay = myFont.render("Turn:" + str(turnCount), 1, (255, 255, 255))
    screen.blit(turnCountDisplay, (battlefield.width() * Tile.Size + 13, battlefield.height() * Tile.Size - 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
