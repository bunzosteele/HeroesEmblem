import sys, pygame, os
from pygame.locals import *

class Battlefield():
    
	def __init__(self, tiles):
		self.tiles = tiles
	
	def draw(self, screen):
		column = 0
		while column < len(self.tiles):
			row = 0
			while row < len(self.tiles[column]):
				self.tiles[column][row].draw(screen, row, column)
				row = row + 1
			column = column + 1