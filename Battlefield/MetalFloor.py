from Tile import *


class MetalFloor(Tile):
    Image = "images/MetalFloor.png"
    DefenseBoost = 0
    AccuracyPenalty = 0
    MovementCost = 1
    Altitude = 1

    def __init__(self, spawn):
        Tile.__init__(self, MetalFloor.Image, MetalFloor.DefenseBoost, MetalFloor.AccuracyPenalty,
                      MetalFloor.MovementCost, MetalFloor.Altitude, spawn)

    def draw(self, surface, x, y):
        super(MetalFloor, self).draw(surface, x, y)