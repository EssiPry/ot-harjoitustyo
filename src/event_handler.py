import sys
import pygame

from event_queue import EventQueue


class EventHandler:
    """ Luokka, joka käsittelee käyttäjältä tulevan syötteen.
    """

    def __init__(self):
        self._event_queue = EventQueue()

    def main_menu_event_handler(self):
        """Aloitusvalikon käyttäjäsyötteen käsittelijä

        Returns:
            [str]: seuraavan näkymän nimen
        """
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 'start'
                elif event.key == pygame.K_SPACE:
                    return 'high_score'
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def high_score_and_game_over_handler(self):
        """ Tulosnäkymän ja Game Over -näkymän
        käyttäjänsyötteen käsittelijä.

        Returns:
            [Bool]: palauttaa Falsen, joka lopettaa silmukan ja palauttaa
            pelin takaisin aloitusnäkymään
        """
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False

    def game_event_handler(self, shape, level):
        """ Pelin aikaisen käyttäjäsyötteen käsittelijä.

        Args:
            shape (obj): putoava palikka
            level (obj): pelikenttä

        """
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    shape.move_shape('left', level)
                elif event.key == pygame.K_RIGHT:
                    shape.move_shape('right', level)
                elif event.key == pygame.K_UP:
                    shape.rotate_shape(level)
                elif event.key == pygame.K_DOWN:
                    shape.rotate_shape_counter_clockwise(level)
