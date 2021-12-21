import pygame


class GameOverView:
    """Luokka, joka piirtää pelin lopetusnäkymän.
    """
    def __init__(self, display, block_size):
        self._display = display
        self._b_size = block_size

    def show_game_over(self):
        pygame.draw.rect(self._display, (0, 0, 0), pygame.Rect(
            self._b_size*3, self._b_size*4, self._b_size*6, self._b_size*4))
        pygame.draw.rect(self._display, (255, 0, 0), pygame.Rect(
            self._b_size*3, self._b_size*4, self._b_size*6, self._b_size*4), 4)
        font = pygame.font.SysFont('helvetica', 25)
        game_text = font.render('Game', 1, (255, 255, 255))
        over_text = font.render('Over', 1, (255, 255, 255))
        self._display.blit(
            game_text, (self._b_size*4.7, self._b_size*5))
        self._display.blit(over_text, (self._b_size*4.9, self._b_size*6))
        pygame.display.update()
