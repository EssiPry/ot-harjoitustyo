import pygame


class StartView:
    """Luokka joka piirtää pelin aloitusnäkymän.
    """

    def __init__(self, display, block_size):
        self._display = display
        self._b_size = block_size

    def draw_start_game(self):
        self._display.fill((0, 0, 0))
        self.display_text(25, 'Press enter to', 7, 5)
        self.display_text(25, 'start the game', 7, 6)
        self.display_text(25, 'Press space to', 7, 9)
        self.display_text(25, 'view high scores', 6.6, 10)

    def display_text(self, font_size, text, d_x, d_y):
        font = pygame.font.SysFont('helvetica', font_size)
        to_be_displayed = font.render(text, 1, (255, 255, 255))
        self._display.blit(
            to_be_displayed, (self._b_size*d_x, self._b_size*d_y))
        pygame.display.update()
