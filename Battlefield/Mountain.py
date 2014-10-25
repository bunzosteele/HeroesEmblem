from Tile import *


class Mountain(Tile):
    Image = "images/mountain.png"
    DefenseBoost = 2
    AccuracyPenalty = 10
    Solid = False

    def __init__(self):
     Tile.__init__(self, Mountain.Image, Mountain.DefenseBoost, Mountain.AccuracyPenalty, Mountain.Solid)

    def draw(self, surface, x, y):
        super(Mountain, self).draw(surface, x, y)