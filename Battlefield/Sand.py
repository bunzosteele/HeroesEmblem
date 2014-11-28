from Tile import *


class Sand(Tile):
    Image = "images/sand.png"
    DefenseBoost = -1
    AccuracyPenalty = -1
    MovementCost = 3

    def __init__(self):
        Tile.__init__(self, Sand.Image, Sand.DefenseBoost, Sand.AccuracyPenalty, Sand.MovementCost)

    def draw(self, surface, x, y):
        super(Sand, self).draw(surface, x, y)