import pygame


class GameOverView:
    """Luokka, joka piirtää pelin lopetusnäkymän.
    """

    def __init__(self, display, block_size):
        self._display = display
        self._b_size = block_size

    def draw_game_over(self):
        pygame.draw.rect(self._display, (0, 0, 0), pygame.Rect(
            self._b_size*2.5, self._b_size*4, self._b_size*7, self._b_size*7))
        pygame.draw.rect(self._display, (255, 0, 0), pygame.Rect(
            self._b_size*2.5, self._b_size*4, self._b_size*7, self._b_size*7), 4)
        font_big = pygame.font.SysFont('helvetica', 25)
        game_over = font_big.render('GAME OVER', 1, (255, 255, 255))
        self._display.blit(
            game_over, (self._b_size*3.5, self._b_size*5))
        font_small = pygame.font.SysFont('helvetica', 18)
        press_space = font_small.render('Press space to', 1, (255, 255, 255))
        self._display.blit(press_space, (self._b_size*3.8, self._b_size*7))
        return_to = font_small.render('return to the', 1, (255, 255, 255))
        self._display.blit(return_to, (self._b_size*4.05, self._b_size*8))
        main_menu = font_small.render('main menu', 1, (255, 255, 255))
        self._display.blit(main_menu, (self._b_size*4.3, self._b_size*9))
        pygame.display.update()
