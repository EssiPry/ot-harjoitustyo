import pygame
from ui.game_view import GameView
from ui.start_view import StartView
from gameloop import Gameloop
from level import Level

BLOCK_SIZE = 25

def main():
    display = pygame.display.set_mode((BLOCK_SIZE*20, BLOCK_SIZE*22))
    pygame.display.set_caption("One block-tetris")
    pygame.display.update()

    pygame.init()

    level = Level(BLOCK_SIZE)
    clock = pygame.time.Clock()
    startview = StartView(display, BLOCK_SIZE)
    startview.start_screen()
    gameview = GameView(display, level, BLOCK_SIZE)
    gameloop = Gameloop(clock, display, level, gameview)
    gameloop.start()

if __name__ == "__main__":
    main()
