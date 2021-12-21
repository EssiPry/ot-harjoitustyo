import sys
import pygame

class EventHandler:
    """ Luokka, joka käsittelee käyttäjältä tulevan syötteen.
    """

    def __init__(self):
        pass

    def main_menu_event_handler(self):
        for event in self.get_event():
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
        for event in self.get_event():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False

    def game_event_handler(self, shape, level):
        for event in self.get_event():
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
                    # placeholder for rotate shape counter clockwise
                    pass
        return True

    def get_event(self):
        return pygame.event.get()
