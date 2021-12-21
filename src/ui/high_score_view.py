import pygame
from repositories.scorerepository import (
    score_repository as default_score_repository
)


class HighScoreView:
    """Luokka, joka piirtää parhaat pisteet näkymän.
    """

    def __init__(self, display, block_size):
        self._display = display
        self._b_size = block_size
        self._score_repository = default_score_repository

    def fill_background(self):
        self._display.fill((0,0,0))

    def show_top_three(self):
        results = self._score_repository.get_top_three()
        font = pygame.font.SysFont('helvetica', 25)

        #high_score = font.render('HIGH SCORES:', 1, (255, 255, 255))
        #self._display.blit(high_score, (self._b_size*4.7, self._b_size*3))

        dy = 5
        for i in range(3):
            result = font.render(f'{i+1}. {results[i]}', 1, (255, 255, 255))
            self._display.blit(result, (self._b_size*4.7, self._b_size*dy))
            dy += 1.5
        pygame.display.update()

    def display_text(self, font_size, text, dy, dx):
        font = pygame.font.SysFont('helvetica', font_size)
        to_be_displayed = font.render(text, 1, (255, 255, 255))
        self._display.blit(
            to_be_displayed,(self._b_size*dy, self._b_size*dx))
        pygame.display.update()


    def draw_high_score_view(self):
        self.fill_background()
        self.display_text(25, 'HIGH SCORES:', 4.7, 3)
        self.show_top_three()
        self.display_text(18, 'Press space to return to the main menu', 4.7, 20)
