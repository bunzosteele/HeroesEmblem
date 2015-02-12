import UI.Buttons
from MovementHelper import *
from DrawingHelper import *


def run(screen, game_state):
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 500)
    EndTurn = UI.Buttons.Button("End Turn")
    NewTurn = UI.Buttons.Button("NewTurn")
    Move = UI.Buttons.Button("Move")
    Abilities = UI.Buttons.Button("Abilities")
    Attack = UI.Buttons.Button("Attack")
    Inventory = UI.Buttons.Button("Inventory")

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

        DrawingHelper.draw_all_the_things(game_state, screen, EndTurn, NewTurn, Move, Attack, Abilities, Inventory,
                                          MovementHelper)
        clock.tick(60)

    pygame.quit()
