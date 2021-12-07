import pygame
from sprites.background import Background
from sprites.floor import Floor
from sprites.wall import Wall
from sprites.block import Block
from sprites.top import Top

class Level:
    def __init__(self, level_map, cell_size):
        self.level = level_map
        self.cell_size = cell_size
        self.block = None
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.tops = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()
        self.active_block = pygame.sprite.Group()
        self.locked_blocks = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(level_map)

    def _new_block(self):
        self.block = Block(150,self.cell_size)
        self.active_block.add(self.block)
        self.all_sprites.add(self.active_block)

    def _block_fall(self):
        if self._check_collision(self.block, self.floors) == [] and self._check_collision(self.block, self.locked_blocks) == []:
            self.block.rect.move_ip(0,1)
        else:
            self.block.remove(self.active_block)
            self.locked_blocks.add(self.block)
            self._new_block()

    def _block_move(self, direction):
        if direction == "left" and self.block.rect.x > self.cell_size:
            self.block.rect.move_ip(-self.block.rect.width, 0)
        if direction == "right" and self.block.rect.x < self.cell_size * 11 - self.block.rect.width:
            self.block.rect.move_ip(self.block.rect.width, 0)

    def _check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False)

    def _check_game_over(self):
        if self.block.rect.y <= self.cell_size and self._check_collision(self.block, self.locked_blocks) != []:
            return True
        return False

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
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 2:
                    self.walls.add(Wall(normalized_x, normalized_y))
                elif cell == 3:
                    self.tops.add(Top(normalized_x, normalized_y))

        self.all_sprites.add(
            self.backgrounds,
            self.floors,
            self.walls,
            self.tops,
            self.active_block,
            self.locked_blocks
        )
