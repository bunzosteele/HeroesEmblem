from random import randint
from Units.Archer import Archer
from Units.Footman import Footman
from Units.Knight import Knight
from Units.Mage import Mage


class UnitGenerator():
    def __init__(self):
        pass

    @staticmethod
    def generate_units():
        return [Archer(4, 4, 0), Footman(2, 4, 0), Knight(4, 3, 0), Mage(2, 3, 0), Archer(4, 4, 0), Footman(2, 4, 0),
                Knight(4, 3, 0), Mage(2, 3, 0)]