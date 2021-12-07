import pygame
from gameloop import Gameloop
from level import Level
from renderer import Renderer

LEVEL_MAP = [[3,3,3,3,3,3,3,3,3,3,3,3],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,0,0,0,2],
             [1,1,1,1,1,1,1,1,1,1,1,1],
             ]

CELL_SIZE = 30

def main():
    level_map = LEVEL_MAP
    level_height = CELL_SIZE * len(level_map)
    level_width = CELL_SIZE * len(level_map[1])

    display = pygame.display.set_mode((level_width, level_height))
    pygame.display.set_caption("Block-tris")

    pygame.init()

    level = Level(level_map, CELL_SIZE)
    clock = pygame.time.Clock()
    renderer = Renderer(display, level)
    gameloop = Gameloop(clock, display, level, renderer)

    #level._new_block()
    #renderer.render()

    gameloop.start()

    print('game over, much sad')

if __name__== "__main__":
    main()
