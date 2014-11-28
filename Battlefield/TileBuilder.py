from Wall import Wall
from Grass import Grass
from Mountain import Mountain
from Water import Water
from Sand import Sand


class TileBuilder():

    @staticmethod
    def build(key):
        if key == "G":
            return Grass()
        if key == "M":
            return Mountain()
        if key == "W":
            return Wall()
        if key == "~":
            return Water()
        if key == "S":
            return Sand()