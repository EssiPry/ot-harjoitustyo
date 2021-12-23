import pygame
from event_queue import EventQueue
from gameloop import Gameloop
from renderer import Renderer

BLOCK_SIZE = 25


def main():
    display = pygame.display.set_mode((BLOCK_SIZE*20, BLOCK_SIZE*22))
    pygame.display.set_caption("Tetris-ish")
    pygame.display.update()

    pygame.init()

    clock = pygame.time.Clock()

    event_queue = EventQueue()
    renderer = Renderer(display, BLOCK_SIZE)
    gameloop = Gameloop(clock, event_queue, renderer)
    gameloop.start_main_menu()


if __name__ == "__main__":
    main()
