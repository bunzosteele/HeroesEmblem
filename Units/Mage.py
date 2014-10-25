import sys, pygame, os
from pygame.locals import *
from Units.Unit import *

class Mage(Unit):
	Image = "images/mage.jpg"
	MaxHealth = 8
	AttackPower = 13
	Defense = 3
   
	def __init__(self, x , y, movement):
		Unit.__init__(self, Mage.Image, x, y, movement, Mage.MaxHealth, Mage.Defense)