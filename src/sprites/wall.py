import pygame
from image_loader import load_image

class Wall(pygame.sprite.Sprite):

    def __init__(self, x_coordinate=0, y_coordinate=0):
        super().__init__()

        self.image = load_image("wall.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
