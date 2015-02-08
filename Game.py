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
from GameState import *
from MovementHelper import *
from DrawingHelper import *
from CombatHelper import *
from BattlefieldHelper import *

pygame.init()
pygame.display.set_caption("Heroes Emblem")
button_height = 50
status_width = 100
battlefield = Battlefield(Battlefield.build("Battlefield/2.txt"))
units = [Archer(4, 4, 0), Archer(6, 4, 1), Footman(7, 4, 1), Footman(2, 4, 0), Knight(4, 3, 0), Knight(6, 3, 1), Mage(7, 3, 1), Mage(2, 3, 0)]
game_state = GameState(battlefield, button_height, status_width, units)
screen = pygame.display.set_mode((game_state.get_window_width(), game_state.get_window_height()))
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 500)

EndTurn = UI.Buttons.Button()
NewTurn = UI.Buttons.Button()
Move = UI.Buttons.Button()
Attack = UI.Buttons.Button()

field_height = battlefield.height() * Tile.Size

while game_state.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.running = False
        elif event.type == pygame.USEREVENT:
            game_state.cycle_animation()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if game_state.between_turns and NewTurn.pressed(pos):
                if NewTurn.pressed(pos):
                    game_state.start_new_turn()
            elif EndTurn.pressed(pos):
                game_state.end_turn()
            elif Move.pressed(pos):
                if game_state.selected is not None and game_state.can_selected_unit_move():
                    game_state.moving = not game_state.moving
            elif Attack.pressed(pos):
                if game_state.can_selected_unit_attack():
                    game_state.toggle_attacking()
            else:
                clicked_space = (pos[0] / Tile.Size, pos[1] / Tile.Size)
                if game_state.is_click_in_bounds(clicked_space):
                    if game_state.is_clicking_selected_unit(clicked_space):
                        game_state.deselect_unit()
                    elif game_state.is_clicking_own_unit(clicked_space):
                        game_state.attempt_to_select_unit(clicked_space)
                    elif game_state.is_unit_moving():
                        game_state.attempt_to_move_unit(clicked_space)
                    elif game_state.is_unit_attacking():
                        game_state.attempt_to_attack(clicked_space)
                    else:
                        game_state.attempt_to_select_unit(clicked_space)

    DrawingHelper.draw_all_the_things(game_state, screen, EndTurn, NewTurn, Move, Attack, MovementHelper)
    clock.tick(60)

pygame.quit()
