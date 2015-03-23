import math
from MovementHelper import *
from Units.Abilities.Teleport import *
from Units.Abilities.Scholar import *


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
        self.using_ability = False
        self.turn_count = 1
        self.battlefield = battlefield
        self.button_height = button_height
        self.button_width = int(math.floor(((battlefield.width() * Tile.Size) * 1.25) / 5))
        self.units = units
        self.spawn_units()
        self.ending_ai_turn = False

    def get_window_height(self):
        return self.battlefield.height() * Tile.Size + self.button_height

    def get_window_width(self):
        return self.battlefield.width() * Tile.Size + self.button_width

    def get_selected_unit(self):
        return self.selected

    def can_selected_unit_move(self):
        return not self.selected.distance_moved > 0 and self.selected.get_team() == self.current_player

    def can_selected_unit_attack(self):
        return self.selected is not None \
               and not self.selected.has_acted \
               and CombatHelper.can_attack(self.selected, self.battlefield, self.units, self.current_player)

    def can_selected_unit_use_ability(self):
        if self.selected is None:
            return False
        if self.using_ability:
            return True
        return not self.selected.has_acted \
               and (self.selected.Ability is not None
                    and self.selected.Ability.can_use_ability(self.selected, self))

    def can_selected_unit_act(self):
        return self.can_selected_unit_attack() or self.can_selected_unit_use_ability()

    def toggle_moving(self):
        self.attacking = False
        self.using_ability = False
        self.moving = not self.moving

    def toggle_attacking(self):
        self.moving = False
        self.using_ability = False
        self.attacking = not self.attacking

    def toggle_ability(self):
        Teleport.teleporting_unit = None
        self.moving = False
        self.attacking = False
        self.using_ability = not self.using_ability

    def is_clicking_selected_unit(self, clicked_space):
        return self.selected is not None and self.selected.get_location() == clicked_space

    def is_clicking_own_unit(self, clicked_space):
        return self.selected is not None and self.get_clicked_tile_and_unit(clicked_space)[1] is not None \
               and self.get_clicked_tile_and_unit(clicked_space)[1].get_team() == self.current_player

    def is_unit_moving(self):
        return self.selected is not None and self.moving

    def is_unit_attacking(self):
        return self.selected is not None and self.attacking

    def is_unit_using_ability(self):
        return self.selected is not None and self.using_ability

    def is_owned_unit_selected(self):
        return self.selected is not None and self.selected.get_team() == self.current_player

    def is_click_in_bounds(self, clicked_space):
        return clicked_space[0] < self.battlefield.width() and clicked_space[1] < self.battlefield.height()

    def is_ai_tick(self):
        return self.animation_state == 1 and self.between_turns and self.current_player != 0

    def cycle_animation(self):
        if self.animation_state == 3:
            self.animation_state = 1
        else:
            self.animation_state += 1

    def start_new_turn(self):
        self.between_turns = False

    def end_turn(self):
        self.moving = False
        for u in self.units:
            u.has_acted = False
            u.distance_moved = 0
            if u in self.tapped_units and u.get_team() == self.current_player:
                self.tapped_units.remove(u)
        self.cycle_current_player()
        if self.current_player == 0:
            self.turn_count += 1
        self.between_turns = True
        self.selected = None
        self.ending_ai_turn = False

    def cycle_current_player(self):
        if self.current_player == 0:
            self.current_player = 1
        elif self.current_player == 1:
            self.current_player = 0

    def deselect_unit(self):
        self.selected = None
        self.moving = False
        self.attacking = False
        self.using_ability = False
        Teleport.teleporting_unit = None

    def attempt_to_select_unit(self, clicked_space):
        selection = self.get_clicked_tile_and_unit(clicked_space)[1]
        if selection is not None and selection.is_dead is False:
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
            self.selected.distance_moved = abs(new_location[0] - current_location[0]) + abs(
                new_location[1] - current_location[1])
            if not self.can_selected_unit_act():
                self.tapped_units.append(self.selected)
            self.untap_affected_units()

    def attempt_to_attack(self, clicked_space):
        target_tile, target_unit = self.get_clicked_tile_and_unit(clicked_space)
        if target_unit is None or target_unit.get_team() == self.current_player or target_unit.is_dead:
            self.toggle_attacking()
        elif CombatHelper.can_attack_targets(self.selected, self.battlefield, [target_unit]):
            damage = CombatHelper.attack(target_tile, target_unit, self)
            target_unit.selected_target()
            if damage == "Missed":
                target_unit.incoming_effect(0, damage)
            elif damage == "Blocked":
                target_unit.incoming_effect(0, damage)
            else:
                target_unit.incoming_effect(damage, "Damage")
            self.selected.has_acted = True
            if target_unit.CurrentHealth <= 0:
                CombatHelper.kill_unit(target_unit, self)
            if self.selected.distance_moved > 0:
                self.tapped_units.append(self.selected)
        self.attacking = False

    def attempt_to_use_ability(self, clicked_space):
        target_tile, target_unit = self.get_clicked_tile_and_unit(clicked_space)
        ability = self.selected.Ability
        if not ability.is_valid_target(clicked_space, target_unit, self.selected, self) and not target_unit.is_dead:
            if Teleport.teleporting_unit is not None:
                Teleport.teleporting_unit = None
            else:
                self.toggle_ability()
            return
        else:
            if not ability.use_ability(clicked_space, target_unit, self.selected, self):
                return
            if self.selected.distance_moved > 0:
                self.tapped_units.append(self.selected)
        self.using_ability = False
        self.untap_affected_units()

    def untap_affected_units(self):
        for unit in self.tapped_units:
            if not unit.has_acted and unit.get_team() == self.current_player and \
                    (CombatHelper.can_attack(unit, self.battlefield, self.units, self.current_player)
                     or (unit.Ability is not None and unit.Ability.can_use_ability(unit, self))):
                self.tapped_units.remove(unit)

    def ai_attack(self, target_tile, target_unit):
        if target_unit is None or target_unit.get_team() == self.current_player:
            self.moving = False
            self.attacking = not self.attacking
        elif CombatHelper.can_attack_targets(self.selected, self.battlefield, [target_unit]):
            damage = CombatHelper.attack(target_tile, target_unit, self)
            target_unit.selected_target()
            if damage == "Missed":
                target_unit.incoming_effect(0, damage)
            elif damage == "Blocked":
                target_unit.incoming_effect(0, damage)
            else:
                target_unit.incoming_effect(damage, "Damage")
            self.selected.has_acted = True
            if target_unit.CurrentHealth <= 0:
                CombatHelper.kill_unit(target_unit, self)
            if self.selected.distance_moved > 0:
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
        for x in range(0, 16):
            for y in range(0, 9):
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

    def get_player_units(self):
        player_units = []
        for unit in self.units:
            if unit.get_team() == 0:
                player_units.append(unit)
        return player_units

    def get_survivors(self):
        for unit in self.units:
            unit.has_acted = False
            unit.distance_moved = 0
            unit.has_used_ability = False
            if unit.Ability == Scholar:
                Scholar.taught_units = []
        return self.units

    def clean_dead_units(self):
        for unit in self.units:
            if unit.is_dead and unit.animation_count > 50:
                self.units.remove(unit)

    def are_animations_playing(self):
        for unit in self.units:
            if unit.animation_count > 0 or unit.effect_quantity is not None:
                return True
        return False






