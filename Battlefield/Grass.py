from Tile import *


class Grass(Tile):
    Image = "images/grass.jpg"
    DefenseBoost = 0
    AccuracyPenalty = 0
    Solid = False

    def __init__(self):
        Tile.__init__(self, Grass.Image, Grass.DefenseBoost, Grass.AccuracyPenalty, Grass.Solid)

    def draw(self, surface, x, y):
        super(Grass, self).draw(surface, x, y)