import os
from TileBuilder import TileBuilder


class Battlefield():
    Width = 16
    Height = 9

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
                    if key != '':
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

    def get_enemy_spawn_count(self):
        count = 0
        for x in range(0, Battlefield.Width):
            for y in range(0, Battlefield.Height):
                if self.get_tile(x, y).spawn == '*':
                    count += 1
        return count




