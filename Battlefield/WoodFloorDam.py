from Tile import *


class WoodFloorDam(Tile):
    Image = "images/WoodFloorDam1.png"
    DefenseBoost = 0
    AccuracyPenalty = 0
    MovementCost = 1
    Altitude = 1

    def __init__(self, spawn):
        Tile.__init__(self, WoodFloorDam.Image, WoodFloorDam.DefenseBoost, WoodFloorDam.AccuracyPenalty,
                      WoodFloorDam.MovementCost, WoodFloorDam.Altitude, spawn)

    def draw(self, surface, x, y):
        super(WoodFloorDam, self).draw(surface, x, y)