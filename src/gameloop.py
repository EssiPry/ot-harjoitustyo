from random import randint
import pygame
from shape import Shape
from repositories.scorerepository import (
    score_repository as default_score_repository
)


class Gameloop():
    """Luokka joka huolehtii pelisilmukasta, eli käyttäjän syötteiden
    lukemisesta, peli kentän päivittämisestä syötteiden perusteella ja
    uuden näkymän piirtämisestä.
    """

    def __init__(self, clock, display, level, view):
        self._clock = clock
        self._display = display
        self._level = level
        self._view = view
        self._score_repository = default_score_repository

    def start(self):
        cur_shape = Shape(randint(0, 6))
        self._level.increase_score('block', 1)
        self._level.add_shape_to_grid(cur_shape)
        self._view.draw_game_view()

        while True:
            if self._level.check_game_over():
                print("Game over")
                self._score_repository.add_score_to_db(self._level.get_score())
                print(self._score_repository.get_top_three())
                break
            if self.event_handler(cur_shape) is False:
                break
            if cur_shape.is_locked():
                cur_shape = Shape(randint(0, 6))
                self._level.increase_score('block', 1)
            cur_shape.shape_fall(self._level)
            self._level.check_for_full_rows()
            self._level.add_shape_to_grid(cur_shape)
            self._view.draw_game_view()
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
                    shape.rotate_shape(self._level)
                elif event.key == pygame.K_DOWN:
                    # placeholder for move block down
                    pass
        return True
