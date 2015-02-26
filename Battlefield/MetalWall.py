from Tile import *


class MetalWall(Tile):
    Image = "images/MetalWall.png"
    DefenseBoost = 0
    AccuracyPenalty = 0
    MovementCost = 1000
    Altitude = 5

    def __init__(self, spawn):
        Tile.__init__(self, MetalWall.Image, MetalWall.DefenseBoost, MetalWall.AccuracyPenalty, MetalWall.MovementCost,
                      MetalWall.Altitude, spawn)

    def draw(self, surface, x, y):
        super(MetalWall, self).draw(surface, x, y)