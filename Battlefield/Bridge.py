from Tile import *


class Bridge(Tile):
    Image = "images/Bridge.png"
    DefenseBoost = 0
    AccuracyPenalty = 0
    MovementCost = 1
    Altitude = 1

    def __init__(self, spawn):
        Tile.__init__(self, Bridge.Image, Bridge.DefenseBoost, Bridge.AccuracyPenalty,
                      Bridge.MovementCost, Bridge.Altitude, spawn)

    def draw(self, surface, x, y):
        super(Bridge, self).draw(surface, x, y)