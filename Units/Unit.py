import sys, pygame, os
from pygame.locals import *

class Unit(pygame.sprite.Sprite):
    dist = 31
    
    def __init__(self, x, y, team):
        pygame.sprite.Sprite.__init__(self)
        self.x = x * self.dist
        self.y = y * self.dist
        self.tapped = False
        self.team = team
        self.CurrentHealth = self.MaxHealth
        self.image = pygame.image.load(self.Image)
        self.rect = self.image.get_rect()


    def draw(self, surface, animation_state):
        image_attributes = self.Image.split("-")
        if self.tapped:
            image_attributes[2] = "1"
        else:
            image_attributes[2] = str(animation_state)
        self.image = pygame.image.load("-".join(image_attributes))

        if self.tapped:
            self.image.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)

        surface.blit(self.image, (self.x, self.y))
    
    def movement_clac(self):
        self.temp_movement -= 1

    def reset_movement(self):
        self.temp_movement = self.movement

    def get_location(self):
        current_space = (self.x/self.dist, self.y/self.dist)
        return current_space

    def get_team(self):
        return self.team

    def get_movement(self):
        return self.Movement

    def get_minimum_range(self):
        return self.MinimumRange

    def get_maximum_range(self):
        return self.MaximumRange

    def tap(self):
        self.tapped = True

    def untap(self):
        self.tapped = False

    def deal_damage(self, damage):
        self.CurrentHealth -= damage

