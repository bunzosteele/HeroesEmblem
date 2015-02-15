import pygame, os


class Tile(pygame.sprite.Sprite):
    Size = 32

    def __init__(self, image, defenseBoost, accuracyPenalty, movementCost, altitude, spawn):
        self.defenseBoost = defenseBoost
        self.accuracyPenalty = accuracyPenalty
        self.image = pygame.image.load(self.resource_path(image))
        self.rect = self.image.get_rect()
        self.movementCost = movementCost
        self.altitude = altitude
        self.spawn = spawn

    def draw(self, surface, x, y):
        surface.blit(self.image, (x * Tile.Size, y * Tile.Size))

    def resource_path(self, relative):
        return os.path.join(
            os.environ.get(
                "_MEIPASS2",
                os.path.abspath(".")
            ),
            relative
        )