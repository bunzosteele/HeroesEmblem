from Tile import *


class BridgeTop(Tile):
    Image = "images/BridgeTop.png"
    DefenseBoost = 0
    AccuracyPenalty = 0
    MovementCost = 1
    Altitude = 1

    def __init__(self, spawn):
        Tile.__init__(self, BridgeTop.Image, BridgeTop.DefenseBoost, BridgeTop.AccuracyPenalty,
                      BridgeTop.MovementCost, BridgeTop.Altitude, spawn)

    def draw(self, surface, x, y):
        super(BridgeTop, self).draw(surface, x, y)