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
    def build(inputfile):
        with open(inputfile, "r") as blueprint:
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

    def getTile(self, x, y):
        return self.tiles[y][x]

    def width(self):
        return len(self.tiles[0])

    def height(self):
        return len(self.tiles)



