from AIHelper import *
import UI.Buttons
from MovementHelper import *
from DrawingHelper import *


def run(screen, game_state):
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 500)
    end_turn = UI.Buttons.Button("End Turn")
    new_turn = UI.Buttons.Button("New Turn")
    move = UI.Buttons.Button("Move")
    ability = UI.Buttons.Button("Ability")
    attack = UI.Buttons.Button("Attack")
    inventory = UI.Buttons.Button("Inventory")

    while game_state.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state.running = False
            elif game_state.is_player_defeated():
                return game_state.get_survivors()
            elif event.type == pygame.USEREVENT:
                game_state.cycle_animation()
                if game_state.is_ai_tick():
                    if game_state.ending_ai_turn:
                        game_state.end_turn()
                    else:
                        game_state.ending_ai_turn = not AIHelper.play_turn(game_state)
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if game_state.between_turns and game_state.current_player != 0:
                    pass
                elif game_state.between_turns and game_state.current_player == 0 and new_turn.pressed(pos):
                    if new_turn.pressed(pos):
                        game_state.start_new_turn()
                elif end_turn.pressed(pos) and not game_state.between_turns:
                    game_state.end_turn()
                elif move.pressed(pos):
                    if game_state.selected is not None and game_state.can_selected_unit_move():
                        game_state.toggle_moving()
                elif attack.pressed(pos):
                    if game_state.can_selected_unit_attack():
                        game_state.toggle_attacking()
                elif ability.pressed(pos):
                    if game_state.can_selected_unit_use_ability():
                        game_state.toggle_ability()
                else:
                    clicked_space = (pos[0] / Tile.Size, pos[1] / Tile.Size)
                    if game_state.is_click_in_bounds(clicked_space):
                        if game_state.is_unit_using_ability():
                            game_state.attempt_to_use_ability(clicked_space)
                        elif game_state.is_clicking_selected_unit(clicked_space):
                            game_state.deselect_unit()
                        elif game_state.is_clicking_own_unit(clicked_space):
                            game_state.attempt_to_select_unit(clicked_space)
                        elif game_state.is_unit_moving():
                            game_state.attempt_to_move_unit(clicked_space)
                        elif game_state.is_unit_attacking():
                            game_state.attempt_to_attack(clicked_space)
                        else:
                            game_state.attempt_to_select_unit(clicked_space)

        DrawingHelper.draw_all_the_things(game_state, screen, end_turn, new_turn, move, attack, ability, inventory,
                                          MovementHelper)
        clock.tick(60)

    return None
    pygame.quit()
