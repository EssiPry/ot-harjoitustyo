import pygame
from image_loader import load_image

class Block(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.name = "placeholder"
        self.image = load_image("block.png")
        self.rect = self.image.get_rect()

        self.rect.y = y
        self.rect.x = x
        self.rotation = "placeholder"
