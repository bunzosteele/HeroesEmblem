from Tile import *


class Forest(Tile):
    Image = "images/Forest.png"
    DefenseBoost = 2
    AccuracyPenalty = 15
    MovementCost = 2
    Altitude = 1

    def __init__(self, spawn):
        Tile.__init__(self, Forest.Image, Forest.DefenseBoost, Forest.AccuracyPenalty, Forest.MovementCost,
                      Forest.Altitude, spawn)

    def draw(self, surface, x, y):
        super(Forest, self).draw(surface, x, y)