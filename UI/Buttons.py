# -*- coding: cp1252 -*-
#/usr/bin/env python
#Simon H. Larsen
#Buttons
#Project startet: d. 26. august 2012
import pygame
from pygame.locals import *
pygame.init()


class Button:

    def __init__(self, the_name):
        self.name = the_name
        self.rect = None

    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        if width is None:
            self.draw_button_no_border(surface, color, length, height, x, y)
        else:
            surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x,y, length, height)
        return surface

    @staticmethod
    def write_text(surface, text, text_color, length, height, x, y):
        font_size = int(length//len(text))
        my_font = pygame.font.SysFont("Calibri", font_size)
        my_text = my_font.render(text, 1, text_color)
        surface.blit(my_text, ((x+length/2) - my_text.get_width()/2, (y+height/2) - my_text.get_height()/2))
        return surface

    @staticmethod
    def draw_button(surface, color, length, height, x, y, width):
        for i in range(1,10):
            s = pygame.Surface((length+(i*2),height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x-i,y-i,length+i,height+i), width)
            surface.blit(s, (x-i,y-i))
        pygame.draw.rect(surface, color, (x,y,length,height), 0)
        pygame.draw.rect(surface, (190,190,190), (x,y,length,height), 1)
        return surface

    def draw_button_no_border(self, surface, color, length, height, x, y):
        pygame.draw.rect(surface, color, (x,y,length,height), 0)
        pygame.draw.rect(surface, (190,190,190), (x,y,length,height), 1)
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False
