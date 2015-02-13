import os
from TileBuilder import TileBuilder


class Battlefield():
    def __init__(self, tiles):
        self.tiles = tiles

    def draw(self, screen):
        column = 0
        while column < len(self.tiles):
            row = 0
            while row < len(self.tiles[column]):
                self.tiles[column][row].draw(screen, row, column)
                row += 1
            column += 1

    @staticmethod
    def build(input_file):
        with open(Battlefield.resource_path(input_file), "r") as blueprint:
            row = blueprint.readline().replace("\n", "").split(' ')
            battlefield = []
            i = 0
            while row != ['']:
                tileRow = []
                for key in row:
                    tileRow.append(TileBuilder.build(key))
                battlefield.append(tileRow)
                row = blueprint.readline().replace("\n", "").split(' ')
                i += 1
            return battlefield

    @staticmethod
    def resource_path(relative):
        return os.path.join(
            os.environ.get(
                "_MEIPASS2",
                os.path.abspath(".")
            ),
            relative
        )

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def width(self):
        return len(self.tiles[0])

    def height(self):
        return len(self.tiles)



