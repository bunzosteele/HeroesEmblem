import pygame
from Battlefield.Tile import Tile
from Battlefield.Battlefield import Battlefield
from UnitGenerator import *
import math


class ShopState:
    def __init__(self, starting_units, button_height, difficulty, gold, max_enemies):
        self.is_draft = True
        self.roster = starting_units
        if self.is_draft:
            self.stock = UnitGenerator.generate_units()
        else:
            pass
        self.window_width = int(math.floor((Tile.Size * Battlefield.Width) * 1.25))
        self.window_height = (Tile.Size * Battlefield.Height) + button_height
        self.button_height = button_height
        self.button_width = self.window_width / 5
        self.shop_width = self.window_width - (self.button_width * 2)
        self.shop_height = self.window_height - self.button_height
        self.selected = None
        self.animation_state = 1
        self.pedestals = ShopState.build_pedestals(self.shop_width, self.shop_height, self.button_width)
        self.roster_offset = self.button_width + (self.pedestals[0].size[0] / 4) - 5
        self.difficulty = difficulty
        self.selected_position = None
        self.gold = gold
        self.gold_spent = 0
        self.max_enemies = max_enemies

    def is_stock_selected(self):
        return self.selected is not None and self.selected in self.stock

    def can_shop(self):
        can_afford = False
        for item in self.stock:
            if item.Cost <= self.gold:
                can_afford = True
        return len(self.roster) <= 7 and can_afford

    def can_buy_selected(self):
        return len(self.roster) <= 7 and self.selected.Cost <= self.gold

    def try_select(self, pos):
        if self.get_at_pedestal(pos) is not None:
            return self.get_at_pedestal(pos)
        if self.get_from_roster is not None:
            return self.get_from_roster(pos)
        return None

    def get_at_pedestal(self, pos):
        i = 0
        for pedestal in self.pedestals:
            if pedestal.topleft[0] < pos[0] < pedestal.bottomright[0] and pedestal.topleft[1] < pos[1] < \
                    pedestal.bottomright[1]:
                return self.stock[i]
            i += 1
        return None

    def get_from_roster(self, pos):
        if pos[1] < self.shop_height or pos[0] < self.button_width or pos[0] > self.window_width - self.button_width:
            return None
        i = (pos[0] - self.roster_offset) / self.pedestals[0].size[0]
        if len(self.roster) > i:
            return self.roster[i]
        else:
            return None

    def draft_unit(self):
        if self.can_buy_selected():
            self.roster.append(self.selected)
            self.gold -= self.selected.Cost
            self.gold_spent += self.selected.Cost
            self.selected = None
            self.stock = UnitGenerator.generate_units()

    def cycle_animation(self):
        if self.animation_state == 3:
            self.animation_state = 1
        else:
            self.animation_state += 1

    @staticmethod
    def build_pedestals(shop_width, shop_height, button_width):
        pedestal_size = shop_width / 8
        x_offset = button_width + (pedestal_size / 2)
        y_offset = shop_height / 5
        pedestals = []
        for i in range(0, 8):
            if i < 4:
                pedestals.append(pygame.Rect(x_offset, y_offset, pedestal_size, pedestal_size))
            else:
                if i == 4:
                    x_offset = button_width + (pedestal_size / 2)
                pedestals.append(pygame.Rect(x_offset, y_offset * 3, pedestal_size, pedestal_size))
            x_offset += 2 * pedestal_size

        return pedestals

    def finalize(self):
        self.roster.extend(UnitGenerator.generate_enemies(self.difficulty, self.max_enemies))
        return self.roster, self.gold_spent