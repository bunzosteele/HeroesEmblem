import sys, pygame, os
from pygame.locals import *
from Tile import *

class Grass(Tile):
	Image = "images/grass.jpg"
	DefenseBoost = 0
	AccuracyPenalty = 0
   
	def __init__(self):
		Tile.__init__(self, Grass.Image, Grass.DefenseBoost, Grass.AccuracyPenalty)
	
	def draw(self, surface, x, y):
		super(Grass, self).draw(surface, x, y)