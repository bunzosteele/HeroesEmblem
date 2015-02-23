import pygame
from pygame.locals import *
pygame.init()


class HealthBar:
    @staticmethod
    def draw_healthbar(surface, unit):
        health_percent = (float(unit.CurrentHealth)/unit.MaxHealth)
        health_color = pygame.Color('green')
        if health_percent < 0.6:
            health_percent = pygame.Color('yellow')
        elif health_percent < 0.3:
            health_percent = pygame.Color('red')

        pygame.draw.rect(surface, health_color, (unit.x, unit.y + unit.rect.height - 5, 30 * health_percent, 2))
