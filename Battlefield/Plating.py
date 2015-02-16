from Tile import *


class Plating(Tile):
    Image = "images/Plating.png"
    DefenseBoost = 0
    AccuracyPenalty = 0
    MovementCost = 2
    Altitude = 1

    def __init__(self, spawn):
        Tile.__init__(self, Plating.Image, Plating.DefenseBoost, Plating.AccuracyPenalty, Plating.MovementCost,
                      Plating.Altitude, spawn)

    def draw(self, surface, x, y):
        super(Plating, self).draw(surface, x, y)