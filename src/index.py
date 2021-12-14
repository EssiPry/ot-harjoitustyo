import pygame
from level import Level
from gameloop import Gameloop

BLOCK_SIZE = 25


def main():
    display = pygame.display.set_mode((BLOCK_SIZE*10, BLOCK_SIZE*20))
    pygame.display.set_caption("dying on the inside 2.0")
    pygame.display.update()

    pygame.init()

    level = Level(BLOCK_SIZE)
    clock = pygame.time.Clock()
    gameloop = Gameloop(clock, display, level)

    gameloop.start()


if __name__ == "__main__":
    main()
