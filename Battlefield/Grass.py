from Tile import *


class Grass(Tile):
    Image = "images/grass.jpg"
    DefenseBoost = 0
    AccuracyPenalty = 0
    MovementCost = 1
    Altitude = 1

    def __init__(self, spawn):
        Tile.__init__(self, Grass.Image, Grass.DefenseBoost, Grass.AccuracyPenalty, Grass.MovementCost, Grass.Altitude,
                      spawn)

    def draw(self, surface, x, y):
        super(Grass, self).draw(surface, x, y)