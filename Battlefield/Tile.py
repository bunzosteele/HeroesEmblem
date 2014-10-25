import sys, pygame, os
from pygame.locals import *

class Tile(pygame.sprite.Sprite):
	Size = 31
	
	def __init__(self, image, defenseBoost, accuracyPenalty):
		self.defenseBoost = defenseBoost
		self.accuracyPenalty = accuracyPenalty		
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		
	def draw(self, surface, x, y):
		surface.blit(self.image, (x * Tile.Size, y * Tile.Size))