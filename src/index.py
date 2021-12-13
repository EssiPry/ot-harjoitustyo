import pygame
from level import Level
from shape import Shape

BLOCK_SIZE = 25


def main():
    display = pygame.display.set_mode((BLOCK_SIZE*22, BLOCK_SIZE*22))
    pygame.display.set_caption("dying on the inside 2.0")
    pygame.display.update()

    pygame.init()

    level = Level()
    shape = Shape()
    shape.move_shape('right', level)
    level.show_shape_in_matrix(shape)
    level.print_matrix()


    for i in range(250):
        if level.check_game_over():
            print('Game Over')
            break
        if shape.locked:
            shape = Shape()
        shape.shape_fall(level)
        level.show_shape_in_matrix(shape)
        level.print_matrix()

if __name__ == "__main__":
    main()
