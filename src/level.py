import pygame
from sprites.background import Background
from sprites.wall import Wall
from sprites.block import Block
from sprites.top import Top

class Level:
    def __init__(self, level_map, cell_size):
        self.level = level_map
        self.cell_size = cell_size
        self.block = None
        self.walls = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(level_map)

    def _new_block(self):
        self.block = Block(150,30)
        self.blocks.add(self.block)
        self.all_sprites.add(self.block)

    def _block_fall(self):
        if self.block.rect.y < self.cell_size * 20 - self.block.rect.height:
            self.block.rect.move_ip(0,1)

    def _block_move(self, direction):
        if direction == "left" and self.block.rect.x > self.cell_size:
            self.block.rect.move_ip(-self.block.rect.width, 0)
        if direction == "right" and self.block.rect.x < self.cell_size * 11 - self.block.rect.width:
            self.block.rect.move_ip(self.block.rect.width, 0)

    def _initialize_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.backgrounds.add(Background(normalized_x, normalized_y))
                elif cell == 1:
                    self.walls.add(Wall(normalized_x, normalized_y))

        self.all_sprites.add(
            self.backgrounds,
            self.walls,
            self.blocks
        )
