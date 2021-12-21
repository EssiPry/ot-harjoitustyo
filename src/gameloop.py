from random import randint
from shape import Shape
from level import Level
from repositories.scorerepository import (
    score_repository as default_score_repository
)
from ui.game_over_view import GameOverView
from ui.game_view import GameView
from ui.high_score_view import HighScoreView
from ui.start_view import StartView


class Gameloop():
    """Luokka joka huolehtii pelisilmukasta, eli käyttäjän syötteiden
    lukemisesta, peli kentän päivittämisestä syötteiden perusteella ja
    uuden näkymän piirtämisestä.
    """

    def __init__(self, clock, display, block_size, event_handler):
        self._clock = clock
        self._display = display
        self._level = None
        self._block_size = block_size
        self._view = None
        self._event_handler = event_handler
        self._score_repository = default_score_repository

    def start_main_menu(self):
        while True:
            self._view = StartView(self._display, self._block_size)
            self._view.draw_start_game()
            event = self._event_handler.main_menu_event_handler()
            if event == 'start':
                self.start_loop()
            elif event == 'high_score':
                self.start_high_score()
            self._clock.tick(1)

    def start_loop(self):
        self._level = Level()
        self._view = GameView(self._display, self._level, self._block_size)
        running = True
        cur_shape = Shape(randint(0, 6))
        self._level.add_shape_to_grid(cur_shape)
        self._view.draw_game_view()

        while running:
            if self._level.check_game_over():
                self._score_repository.add_score_to_db(self._level.get_score())
                running = False
            self._event_handler.game_event_handler(cur_shape, self._level)
            if cur_shape.is_locked():
                cur_shape = Shape(randint(0, 6))
                self._level.increase_score('lock', 1)
            cur_shape.shape_fall(self._level)
            self._level.check_for_full_rows()
            self._level.add_shape_to_grid(cur_shape)
            self._view.draw_game_view()
            self._clock.tick(5)
        self.start_game_over()

    def start_high_score(self):
        self._view = HighScoreView(self._display, self._block_size)
        running = True
        while running:
            self._view.draw_high_score_view()
            if self._event_handler.high_score_and_game_over_handler() is False:
                break
            self._clock.tick(1)

    def start_game_over(self):
        self._view = GameOverView(self._display, self._block_size)
        running = True
        while running:
            self._view.show_game_over()
            if self._event_handler.high_score_and_game_over_handler() is False:
                break
            self._clock.tick(1)
