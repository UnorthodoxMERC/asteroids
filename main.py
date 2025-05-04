import pygame
from constants import *

def main():
    print('Starting Asteroids!')
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)


if __name__ == '__main__':
    main()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
while 1 == 1:
    pygame.Surface.fill(color=(0, 0, 0))
    pygame.display.flip(screen)