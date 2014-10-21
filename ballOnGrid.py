import sys, pygame, os
from pygame.locals import *

class Ball(pygame.sprite.Sprite):

    image = pygame.image.load("blue_ball.bmp")
    x = 0
    y = 0
    dist = 31
    
    def __inti__(self):
        """ The constructor of the class """
        pygame.sprite.Sprite.__init__(self)
        self.dist = dist

        Ball.image = image
        Ball.x = x
        Ball.y = y

        self.image = Ball.image
        self.rect = self.image.get_rect()
        

    def move_up(self):
        if self.y - self.dist >= 0:
            self.y -= self.dist # move up

    def move_down(self):
        if self.y + self.dist <= 600 - self.dist:
            self.y += self.dist # move down

    def move_right(self):
        if self.x + self.dist <= 900 - self.dist:
            self.x += self.dist # move up

    def move_left(self):
        if self.x - self.dist >= 0:
            self.x -= self.dist # move down

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))

pygame.init()

screen_size = width, height = 900,590
wid = 900/31
hght = 600/31

backround_color = 255, 255, 255
grid_color = 0, 0, 0
running = True

screen = pygame.display.set_mode(screen_size)
ball = Ball()
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP: 
                ball.move_up() 
            if event.key == pygame.K_DOWN: 
                ball.move_down()
            if event.key == pygame.K_LEFT: 
                ball.move_left() 
            if event.key == pygame.K_RIGHT: 
                ball.move_right()

    screen.fill(backround_color)
    ball.draw(screen)

    for i in range(1, wid):
        pygame.draw.line (screen, grid_color, (31*i,0), (31*i,600), 1)

    for j in range(1, hght):
        pygame.draw.line (screen, grid_color, (0, 31*j), (900, 31*j), 1)
    
    pygame.display.update()

    clock.tick(60)

pygame.quit()
