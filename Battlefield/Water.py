from Tile import *


class Water(Tile):
    Image = "images/water.png"
    DefenseBoost = 1
    AccuracyPenalty = 0
    MovementCost = 5

    def __init__(self):
        Tile.__init__(self, Water.Image, Water.DefenseBoost, Water.AccuracyPenalty, Water.MovementCost)

    def draw(self, surface, x, y):
        super(Water, self).draw(surface, x, y)