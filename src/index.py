import pygame
from level import Level
from sprites.block import Block

LEVEL_MAP = [[1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,1,1,1,1,1,1,1,1,1,1,1],
             ]

CELL_SIZE = 30

def main():
    level_map = LEVEL_MAP
    level_height = CELL_SIZE * len(level_map)
    level_width = CELL_SIZE * len(level_map[1])

    display = pygame.display.set_mode((level_width, level_height))
    pygame.display.set_caption("Block-Tetris")

    display.fill((0,0,0))

    pygame.init()

    level = Level(level_map, CELL_SIZE)
    level.all_sprites.draw(display)
    pygame.display.update()

    level._new_block()
    level.all_sprites.draw(display)

    clock = pygame.time.Clock()

    run = True

    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    level._block_move("left")
                elif event.key == pygame.K_RIGHT:
                    level._block_move("right")
                elif event.key == pygame.K_UP:
                    print('rotate')

        level._block_fall()
        level.all_sprites.draw(display)
        pygame.display.update()

        clock.tick(30)

    exit()

if __name__== "__main__":
    main()
