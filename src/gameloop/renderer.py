from ui.game_over_view import GameOverView
from ui.game_view import GameView
from ui.high_score_view import HighScoreView
from ui.start_view import StartView


class Renderer:
    """Luokka joka hallinnoi pelinäkymien piirtämistä.
    """

    def __init__(self, display, block_size):
        """Luokan konstruktori

        Args:
            display (obj): pygamen Surface-olio
            block_size (int): pelikentän ruudun sivun pituus
        """
        self._view = None
        self._display = display
        self._block_size = block_size

    def render_start(self):
        """ Luo StartView -olion ja piirtää päävalikon näkymän.
        """
        self._view = StartView(self._display, self._block_size)
        self._view.draw_start_game()

    def render_game(self, level):
        """ Luo GameView -olion ja piirtää pelin aikaisen näkymän.

        Args:
            level (obj): pelikenttä, jonka mukaan pelialue piirretään.
        """
        self._view = GameView(self._display, level, self._block_size)
        self._view.draw_game_view()

    def render_game_over(self):
        """ Luo GameOverView -olion ja piirtään pelin loppunäkymän.
        """
        self._view = GameOverView(self._display, self._block_size)
        self._view.draw_game_over()

    def render_high_score(self):
        """ Luo HighScoreView -olion ja piirtää tulosnäkymän.
        """
        self._view = HighScoreView(self._display, self._block_size)
        self._view.draw_high_score_view()
