from DrawingHelper import DrawingHelper
import UI.Buttons
from Units.Mage import *


def run(screen, shop_state):
    running = True
    buy_button = UI.Buttons.Button("Buy")
    complete_button = UI.Buttons.Button("Complete")
    pygame.time.set_timer(pygame.USEREVENT, 500)
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                shop_state.cycle_animation()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if complete_button.pressed(pos) and len(shop_state.roster) > 0:
                    return shop_state.finalize()
                elif buy_button.pressed(pos) and shop_state.is_stock_selected():
                    if shop_state.is_draft:
                        shop_state.draft_unit()
                    else:
                        #Buy Items
                        pass
                else:
                    shop_state.selected = shop_state.try_select(pos)

        DrawingHelper.draw_all_the_things(shop_state, screen, buy_button, complete_button)
        pygame.display.update()
        clock.tick(60)