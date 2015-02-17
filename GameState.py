import math
from MovementHelper import *
from CombatHelper import *


class GameState:

    def __init__(self, battlefield, button_height, units):
        self.running = True
        self.current_player = 0
        self.between_turns = True
        self.animation_state = 1
        self.tapped_units = []
        self.selected = None
        self.moving = False
        self.attacking = False
        self.turn_count = 1
        self.battlefield = battlefield
        self.button_height = button_height
        self.button_width = int(math.floor(((battlefield.width() * Tile.Size) * 1.25) / 5))
        self.units = units
        self.spawn_units()

    def get_window_height(self):
        return self.battlefield.height() * Tile.Size + self.button_height

    def get_window_width(self):
        return self.battlefield.width() * Tile.Size + self.button_width

    def get_selected_unit(self):
        return self.selected

    def can_selected_unit_move(self):
        return not self.selected.has_moved

    def can_selected_unit_attack(self):
        return self.selected is not None \
            and not self.selected.has_attacked \
            and CombatHelper.can_attack(self.selected, self.battlefield, self.units, self.current_player)

    def toggle_attacking(self):
        self.moving = False
        self.attacking = not self.attacking

    def is_clicking_selected_unit(self, clicked_space):
        return self.selected is not None and self.selected.get_location() == clicked_space

    def is_clicking_own_unit(self, clicked_space):
        return self.selected is not None and self.get_clicked_tile_and_unit(clicked_space)[1] is not None \
            and self.get_clicked_tile_and_unit(clicked_space)[1].get_team() == self.current_player

    def is_unit_moving(self):
        return self.selected is not None and self.moving

    def is_unit_attacking(self):
        return self.selected is not None and self.attacking

    def is_owned_unit_selected(self):
        return self.selected is not None and self.selected.get_team() == self.current_player

    def is_click_in_bounds(self, clicked_space):
        return clicked_space[0] < self.battlefield.width() and clicked_space[1] < self.battlefield.height()

    def cycle_animation(self):
        if self.animation_state == 3:
            self.animation_state = 1
        else:
            self.animation_state += 1

    def start_new_turn(self):
        self.between_turns = False
        self.tapped_units = []
        for u in self.units:
            u.has_attacked = False
            u.has_moved = False

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
        self.selected = None
        self.moving = False
        self.attacking = False

    def attempt_to_select_unit(self, clicked_space):
        selection = self.get_clicked_tile_and_unit(clicked_space)[1]
        if selection is not None:
            self.selected = selection
        else:
            self.selected = None
        self.moving = False
        self.attacking = False

    def attempt_to_move_unit(self, clicked_space):
        current_location = self.selected.get_location()
        MovementHelper.click_movement(self.units, self.battlefield, self.selected, clicked_space)
        new_location = self.selected.get_location()
        self.moving = False
        if current_location != new_location:
            self.selected.has_moved = True
            if self.selected.has_attacked or not CombatHelper.can_attack(self.selected, self.battlefield, self.units, self.current_player):
                self.tapped_units.append(self.selected)

    def attempt_to_attack(self, clicked_space):
        target_tile, target_unit = self.get_clicked_tile_and_unit(clicked_space)
        if target_unit is None or target_unit.get_team() == self.current_player:
                self.moving = False
                self.attacking = not self.attacking
        elif CombatHelper.can_attack_targets(self.selected, self.battlefield, [target_unit]):
            damage = CombatHelper.attack(target_tile, target_unit, self)
            target_unit.selected_target()
            target_unit.incoming_damage(damage)
            self.selected.has_attacked = True
            if target_unit.CurrentHealth <= 0:
                self.units.remove(target_unit)
                self.selected.experience += target_unit.MaxHealth
                self.selected.calculate_level()
            if self.selected.has_moved:
                self.tapped_units.append(self.selected)
        self.attacking = False

    def get_clicked_tile_and_unit(self, clicked_space):
        unit = None
        for u in self.units:
            if u.x / Tile.Size == clicked_space[0] and u.y / Tile.Size == clicked_space[1]:
                unit = u
        tile = self.battlefield.tiles[clicked_space[1]][clicked_space[0]]
        return tile, unit

    def spawn_units(self):
        player_one_units = []
        player_two_units = []
        for unit in self.units:
            if unit.get_team() == 0:
                player_one_units.append(unit)
            if unit.get_team() == 1:
                player_two_units.append(unit)

        player_one_spawns = []
        player_two_spawns = []
        for x in range(0, 15):
            for y in range(0, 8):
                tile = self.battlefield.tiles[y][x]
                if tile.spawn is not None:
                    if tile.spawn == '*':
                        player_two_spawns.append((x, y))
                    else:
                        player_one_spawns.append((x, y, tile.spawn))
        player_one_spawns = sorted(player_one_spawns, key=lambda tile: int(tile[2]))
        i = 0
        for unit in player_one_units:
            unit.x = player_one_spawns[i][0] * Tile.Size
            unit.y = player_one_spawns[i][1] * Tile.Size
            i += 1

        for unit in player_two_units:
            spawn = randint(0, len(player_two_spawns) - 1)
            unit.x = player_two_spawns[spawn][0] * Tile.Size
            unit.y = player_two_spawns[spawn][1] * Tile.Size
            player_two_spawns.remove(player_two_spawns[spawn])

    def is_player_defeated(self):
        players = []
        for unit in self.units:
            if unit.get_team() not in players:
                players.append(unit.get_team())

        return len(players) <= 1






