import pygame


class GameOverView:
    """Luokka, joka piirtää pelin lopetusnäkymän.
    """

    def __init__(self, display, block_size):
        self._display = display
        self._b_size = block_size

    def draw_game_over(self):
        pygame.draw.rect(self._display, (0, 0, 0), pygame.Rect(
            self._b_size*2, self._b_size*4, self._b_size*8, self._b_size*7))
        pygame.draw.rect(self._display, (255, 0, 0), pygame.Rect(
            self._b_size*2, self._b_size*4, self._b_size*8, self._b_size*7), 4)
        self.display_text(30, 'GAME OVER', 3, 5)
        self.display_text(20,'Press space to' , 4, 7)
        self.display_text(20, 'return to the', 4.2, 8)
        self.display_text(20, 'main menu', 4.3, 9)
        pygame.display.flip()

    def display_text(self, font_size, text, d_x, d_y):
        font = pygame.font.SysFont('helvetica', font_size)
        to_be_displayed = font.render(text, 1, (255, 255, 255))
        self._display.blit(
            to_be_displayed, (self._b_size*d_x, self._b_size*d_y))
        pygame.display.update()
