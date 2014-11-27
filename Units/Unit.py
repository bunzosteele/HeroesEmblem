import sys, pygame, os
from pygame.locals import *

class Unit(pygame.sprite.Sprite):
    dist = 31
    
    def __init__(self, art, x , y, movement, health, attack, team):
        pygame.sprite.Sprite.__init__(self)
        self.dist = Unit.dist
        
        self.movement = movement
        self.temp_movement = movement
        self.x = x * self.dist
        self.y = y * self.dist
        self.team = team

        self.image = pygame.image.load(art)
        self.rect = self.image.get_rect()
        

    def move_up(self):
        if self.y - self.dist >= 0:
            self.y -= self.dist

    def move_down(self):
        if self.y + self.dist <= 600 - self.dist:
            self.y += self.dist

    def move_right(self):
        if self.x + self.dist <= 900 - self.dist:
            self.x += self.dist

    def move_left(self):
        if self.x - self.dist >= 0:
            self.x -= self.dist 

    def draw(self, surface):
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
        return self.movement
