from Wall import Wall
from Grass import Grass
from Mountain import Mountain


class TileBuilder():

    @staticmethod
    def build(key):
        if key == "G":
            return Grass()
        if key == "M":
            return Mountain()
        if key == "W":
            return Wall()