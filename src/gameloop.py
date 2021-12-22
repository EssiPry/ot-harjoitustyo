from random import randint
from shape import Shape
from level import Level
from repositories.scorerepository import (
    score_repository as default_score_repository
)

class Gameloop():
    """Luokka joka ylläpitää pelisilmukkaa, yhdistää sovelluslogiikan
    ja käyttäjäsyötteet, sekä hallinnoi pelikentän piirtämistä.
    """

    def __init__(self, clock, renderer, event_handler):
        self._clock = clock
        self._level = None
        self._renderer = renderer
        self._event_handler = event_handler
        self._score_repository = default_score_repository

    def start_main_menu(self):
        while True:
            self._renderer.render_start()
            event = self._event_handler.main_menu_event_handler()
            if event == 'start':
                self.start_game_loop()
            elif event == 'high_score':
                self.start_high_score()
            self._clock.tick(1)

    def start_game_loop(self):
        self._level = Level()
        running = True
        cur_shape = Shape(randint(0, 6))
        self._level.add_shape_to_grid(cur_shape)
        self._renderer.render_game(self._level)

        while running:
            if self._level.check_game_over():
                self._score_repository.add_score_to_db('Minä', self._level.get_score())
                running = False
            if cur_shape.is_locked():
                cur_shape = Shape(randint(0, 6))
                self._level.increase_score('lock', 1)
            self._event_handler.game_event_handler(cur_shape, self._level)
            cur_shape.shape_fall(self._level)
            self._level.check_for_full_rows()
            self._level.add_shape_to_grid(cur_shape)
            self._renderer.render_game(self._level)
            self._clock.tick(3)
        self.start_game_over()

    def start_high_score(self):
        running = True
        while running:
            self._renderer.render_high_score()
            if self._event_handler.high_score_and_game_over_handler() is False:
                break
            self._clock.tick(1)

    def start_game_over(self):
        running = True
        while running:
            self._renderer.render_game_over()
            if self._event_handler.high_score_and_game_over_handler() is False:
                break
            self._clock.tick(1)
