from Tile import *


class BridgeBot(Tile):
    Image = "images/BridgeBot.png"
    DefenseBoost = 0
    AccuracyPenalty = 0
    MovementCost = 1
    Altitude = 1

    def __init__(self, spawn):
        Tile.__init__(self, BridgeBot.Image, BridgeBot.DefenseBoost, BridgeBot.AccuracyPenalty,
                      BridgeBot.MovementCost, BridgeBot.Altitude, spawn)

    def draw(self, surface, x, y):
        super(BridgeBot, self).draw(surface, x, y)