from Tile import *


class Wall(Tile):
    Image = "images/wall.png"
    DefenseBoost = 0
    AccuracyPenalty = 0
    Solid = True

    def __init__(self):
        Tile.__init__(self, Wall.Image, Wall.DefenseBoost, Wall.AccuracyPenalty, Wall.Solid)

    def draw(self, surface, x, y):
        super(Wall, self).draw(surface, x, y)