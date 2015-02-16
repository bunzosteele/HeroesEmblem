from Tile import *


class Void(Tile):
    Image = "images/Void.png"
    DefenseBoost = 0
    AccuracyPenalty = 0
    MovementCost = 9000
    Altitude = 9000

    def __init__(self, spawn):
        Tile.__init__(self, Void.Image, Void.DefenseBoost, Void.AccuracyPenalty, Void.MovementCost, Void.Altitude,
                      spawn)

    def draw(self, surface, x, y):
        super(Void, self).draw(surface, x, y)