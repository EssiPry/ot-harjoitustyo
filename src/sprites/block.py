import pygame
from image_loader import load_image

class Block(pygame.sprite.Sprite):

    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()

        self.name = "placeholder"
        self.image = load_image("block.png")
        self.rect = self.image.get_rect()

        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
        self.rotation = "placeholder"
