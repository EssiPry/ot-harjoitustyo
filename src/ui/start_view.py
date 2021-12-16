import sys
import pygame

class StartView:
    """Luokka joka piirtää pelin aloitusnäkymän.
    """

    def __init__(self, display, b_size):
        self.display = display
        self.b_size = b_size

    def show_start_game(self):
        font = pygame.font.SysFont('arial', 25)
        press = font.render('Press enter to', 1, (255, 255, 255))
        to_start = font.render('start the game', 1, (255, 255, 255))
        self.display.blit(
            press, (self.b_size*7, self.b_size*5))
        self.display.blit(
            to_start, (self.b_size*7, self.b_size*6.5))
        pygame.display.update()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 'start'

    def start_screen(self):
        while True:
            self.show_start_game()
            if self.event_handler() == 'start':
                break
