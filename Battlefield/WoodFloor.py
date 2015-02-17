from Tile import *


class WoodFloor(Tile):
    Image = "images/WoodFloor.png"
    DefenseBoost = 0
    AccuracyPenalty = 0
    MovementCost = 1
    Altitude = 1

    def __init__(self, spawn):
        Tile.__init__(self, WoodFloor.Image, WoodFloor.DefenseBoost, WoodFloor.AccuracyPenalty,
                      WoodFloor.MovementCost, WoodFloor.Altitude, spawn)

    def draw(self, surface, x, y):
        super(WoodFloor, self).draw(surface, x, y)