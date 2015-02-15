from random import randint
from Units.Archer import Archer
from Units.Footman import Footman
from Units.Knight import Knight
from Units.Mage import Mage
from Units.Priest import Priest
from Units.Spearman import Spearman


class UnitGenerator():
    def __init__(self):
        pass

    @staticmethod
    def generate_units():
        return [Archer(0), Footman(0), Knight(0), Mage(0), Archer(0), Footman(0),
                Spearman(0), Priest(0)]

    @staticmethod
    def generate_enemies(difficulty):
        return [Archer(1), Footman(1), Knight(1), Mage(1), Archer(1), Footman(1),
                Spearman(1), Priest(1)]