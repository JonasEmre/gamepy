import pygame
import sys
from settings import *
from tiles import Tile

pygame.init()
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
test_tile = pygame.sprite.Group(Tile((100, 100), 200))

if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((120, 120, 120))
        test_tile.draw(screen)
        pygame.display.update()
        clock.tick(60)
