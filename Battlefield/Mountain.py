from Tile import *


class Mountain(Tile):
    Image = "images/Mountain.png"
    DefenseBoost = 2
    AccuracyPenalty = 10
    MovementCost = 2
    Altitude = 2

    def __init__(self, spawn):
        Tile.__init__(self, Mountain.Image, Mountain.DefenseBoost, Mountain.AccuracyPenalty, Mountain.MovementCost,
                      Mountain.Altitude, spawn)

    def draw(self, surface, x, y):
        super(Mountain, self).draw(surface, x, y)