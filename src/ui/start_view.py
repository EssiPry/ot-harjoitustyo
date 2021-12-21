import pygame


class StartView:
    """Luokka joka piirtää pelin aloitusnäkymän.
    """

    def __init__(self, display, block_size):
        self._display = display
        self._b_size = block_size

    def draw_start_game(self):
        self._display.fill((0,0,0))
        font = pygame.font.SysFont('helvetica', 25)
        press_enter = font.render('Press enter to', 1, (255, 255, 255))
        to_start = font.render('start the game', 1, (255, 255, 255))
        self._display.blit(
            press_enter, (self._b_size*7, self._b_size*5))
        self._display.blit(
            to_start, (self._b_size*7, self._b_size*6.5))
        pygame.display.update()
