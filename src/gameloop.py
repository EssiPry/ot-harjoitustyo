import pygame
from shape import Shape


class Gameloop():
    """Luokka joka huolehtii pelisilmukasta, eli käyttäjän syötteiden
    lukemisesta, peli kentän päivittämisestä syötteiden perusteella ja
    uuden näkymän piirtämisestä.
    """

    def __init__(self, clock, display, level):
        self._clock = clock
        self._display = display
        self._level = level

    def start(self):
        shape = Shape()
        self._level.add_shape_in_matrix(shape)
        self._level.draw_level(self._display)

        while True:
            if self._level.check_game_over():
                print("Game over")
                break
            if self.event_handler(shape) is False:
                break
            if shape.locked:
                shape = Shape()
            shape.shape_fall(self._level)
            self._level.check_for_full_rows()
            self._level.add_shape_in_matrix(shape)
            # self._level.print_matrix()
            self._level.draw_level(self._display)
            self._clock.tick(5)

    def get_event(self):
        return pygame.event.get()

    def event_handler(self, shape):
        for event in self.get_event():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    shape.move_shape('left', self._level)
                elif event.key == pygame.K_RIGHT:
                    shape.move_shape('right', self._level)
                elif event.key == pygame.K_UP:
                    # placeholder for rotate block
                    pass
                elif event.key == pygame.K_DOWN:
                    # placeholder for move block down
                    pass
        return True
