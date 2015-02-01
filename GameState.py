from Units.Unit import *
from Battlefield.Tile import *
from MovementHelper import *
from CombatHelper import *


class GameState:

    def __init__(self, battlefield, button_height, status_width, units):
        self.running = True
        self.current_player = 0
        self.between_turns = True
        self.animation_state = 1
        self.tapped_units = []
        self.previously_moved = None
        self.selected = None
        self.moving = False
        self.attacking = False
        self.turn_count = 1
        self.battlefield = battlefield
        self.button_height = button_height
        self.button_width = (battlefield.width() * Tile.Size + status_width) / 3
        self.status_width = status_width
        self.units = units

    def get_window_height(self):
        return self.battlefield.height() * Tile.Size + self.button_height

    def get_window_width(self):
        return self.battlefield.width() * Tile.Size + self.status_width

    def get_selected_unit(self):
        return self.units[self.selected]

    def can_selected_unit_attack(self):
        return self.selected is not None \
            and CombatHelper.can_attack(self.get_selected_unit(), self.battlefield, self.units, self.current_player)

    def toggle_attacking(self):
        self.moving = False
        self.attacking = not self.attacking
        if not self.attacking and self.previously_moved == self.get_selected_unit():
            self.tapped_units.append(self.get_selected_unit())
            self.selected = None
            self.previously_moved = None

    def is_clicking_selected_unit(self, clicked_space):
        return self.selected is not None and self.get_selected_unit().get_location() == clicked_space

    def is_clicking_own_unit(self, clicked_space):
        return self.selected is not None and self.get_clicked_tile_and_unit(clicked_space)[1] is not None \
            and self.get_clicked_tile_and_unit(clicked_space)[1].get_team() == self.current_player

    def is_unit_moving(self):
        return self.selected is not None and self.moving

    def is_unit_attacking(self):
        return self.selected is not None and self.attacking

    def is_owned_unit_selected(self):
        return self.selected is not None and self.get_selected_unit().get_team() == self.current_player

    def cycle_animation(self):
        if self.animation_state == 3:
            self.animation_state = 1
        else:
            self.animation_state += 1

    def start_new_turn(self):
        self.between_turns = False
        self.tapped_units = []
        self.previously_moved = None

    def end_turn(self):
        self.moving = False
        self.cycle_current_player()
        if self.current_player == 0:
            self.turn_count += 1
        self.between_turns = True
        self.selected = None

    def cycle_current_player(self):
        if self.current_player == 0:
             self.current_player = 1
        elif self.current_player == 1:
            self.current_player = 0

    def deselect_unit(self):
        if self.previously_moved is not None:
            self.tapped_units.append(self.get_selected_unit())
            self.previously_moved = None
        self.selected = None
        self.moving = False
        self.attacking = False

    def attempt_to_select_unit(self, clicked_space):
        selection = self.get_clicked_tile_and_unit(clicked_space)[1]
        if selection is not None and selection not in self.tapped_units:
            self.selected = self.units.index(selection)
        else:
            self.selected = None
        self.moving = False
        self.attacking = False

    def attempt_to_move_unit(self, clicked_space):
        moving_unit = self.get_selected_unit()
        current_location = moving_unit.get_location()
        new_selected = MovementHelper.click_movement(self.units, self.battlefield, moving_unit, clicked_space)
        new_location = moving_unit.get_location()
        self.moving = False
        can_unit_attack = CombatHelper.can_attack(moving_unit, self.battlefield, self.units, self.current_player)
        if can_unit_attack:
            self.attacking = can_unit_attack
            self.previously_moved = moving_unit
        else:
            self.selected = new_selected
        if self.selected is None and current_location != new_location:
            self.tapped_units.append(moving_unit)

    def attempt_to_attack(self, clicked_space):
        #TODO IMPLEMENT ATTACKING
        attacking_unit = self.get_selected_unit()
        self.moving = False
        self.attacking = not self.attacking
        if attacking_unit == self.previously_moved:
            self.tapped_units.append(attacking_unit)
            self.previously_moved = None
        self.selected = None

    def get_clicked_tile_and_unit(self, clicked_space):
        unit = None
        for u in self.units:
            if u.x / Tile.Size == clicked_space[0] and u.y / Tile.Size == clicked_space[1]:
                unit = u
        tile = self.battlefield.tiles[clicked_space[1]][clicked_space[0]]
        return tile, unit





