from Tile import *


class Mountain(Tile):
    Image = "images/mountain.png"
    DefenseBoost = 2
    AccuracyPenalty = 10
    MovementCost = 2

    def __init__(self):
     Tile.__init__(self, Mountain.Image, Mountain.DefenseBoost, Mountain.AccuracyPenalty, Mountain.MovementCost)

    def draw(self, surface, x, y):
        super(Mountain, self).draw(surface, x, y)