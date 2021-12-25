import pygame
from gameloop.clock import Clock
from gameloop.event_queue import EventQueue
from gameloop.gameloop import Gameloop
from gameloop.renderer import Renderer

BLOCK_SIZE = 30


def main():
    display = pygame.display.set_mode((BLOCK_SIZE*20, BLOCK_SIZE*22))
    pygame.display.set_caption("Tetris-ish")
    pygame.display.update()

    pygame.init()

    clock = Clock()
    event_queue = EventQueue()
    renderer = Renderer(display, BLOCK_SIZE)
    gameloop = Gameloop(clock, event_queue, renderer)

    gameloop.start_main_menu()


if __name__ == "__main__":
    main()
