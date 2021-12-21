import pygame
from gameloop import Gameloop
from ui.event_handler import EventHandler

BLOCK_SIZE = 25


def main():
    display = pygame.display.set_mode((BLOCK_SIZE*20, BLOCK_SIZE*22))
    pygame.display.set_caption("Tetris-ish")
    pygame.display.update()

    pygame.init()

    clock = pygame.time.Clock()
    event_handler = EventHandler()
    gameloop = Gameloop(clock, display, BLOCK_SIZE, event_handler)
    gameloop.start_main_menu()


if __name__ == "__main__":
    main()
