import sys, pygame, os
from pygame.locals import *
from Units.Unit import *

class Footman(Unit):
	Image = "images/Footman.png"
	MaxHealth = 10
	AttackPower = 10
	Defense = 5
   
	def __init__(self, x , y, movement):
		Unit.__init__(self, Footman.Image, x, y, movement, Footman.MaxHealth, Footman.Defense)