from ui.game_over_view import GameOverView
from ui.game_view import GameView
from ui.high_score_view import HighScoreView
from ui.start_view import StartView


class Renderer:
    def __init__(self, display, block_size):
        self._view = None
        self._display = display
        self._block_size = block_size

    def render_start(self):
        self._view = StartView(self._display, self._block_size)
        self._view.draw_start_game()

    def render_game(self, level):
        self._view = GameView(self._display, level, self._block_size)
        self._view.draw_game_view()

    def render_game_over(self):
        self._view = GameOverView(self._display, self._block_size)
        self._view.show_game_over()

    def render_high_score(self):
        self._view = HighScoreView(self._display, self._block_size)
        self._view.draw_high_score_view()
