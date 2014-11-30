from Tile import *


class Wall(Tile):
    Image = "images/wall.png"
    DefenseBoost = 0
    AccuracyPenalty = 0
    MovementCost = 1000
    Altitude = 1

    def __init__(self):
        Tile.__init__(self, Wall.Image, Wall.DefenseBoost, Wall.AccuracyPenalty, Wall.MovementCost, Wall.Altitude)

    def draw(self, surface, x, y):
        super(Wall, self).draw(surface, x, y)