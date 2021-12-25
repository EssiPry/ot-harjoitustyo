import sys
from random import randint
import pygame
from game_logic.shape import Shape
from game_logic.level import Level
from repositories.scorerepository import (
    score_repository as default_score_repository
)


class Gameloop():
    """Luokka joka ylläpitää pelisilmukkaa, yhdistää sovelluslogiikan
    ja käyttäjäsyötteet, sekä hallinnoi pelikentän piirtämistä.
    """

    def __init__(self, clock, event_queue, renderer):
        """Luokan konstruktori

        Args:
            clock (obj): [description]
            event_queue (obj): [description]
            renderer (obj): [description]
        """
        self._clock = clock
        self._event_queue = event_queue
        self._level = None
        self._renderer = renderer
        self._score_repository = default_score_repository

    def start_main_menu(self):
        """ Näyttää päävalikon, siirtyy muihin käyttöliittymän osiin käyttäjsyötteellä.
        """
        self._view = 'menu'
        while True:
            self._renderer.render_start()
            event = self._view = self.event_handler('StartView', 'shape')
            if event == 'game':
                self.start_game_loop()
            elif event == 'high_score':
                self.start_high_score()
            self._clock.tick(1)

    def start_game_loop(self):
        """ Aloitaa pelin, pyörittää pelisilmukkaa, liikuttaa palikaa käyttäjäsyötteellä.
        """
        self._level = Level()
        running = True
        cur_shape = Shape(randint(0, 6))
        self._level.add_shape_to_grid(cur_shape)
        self._renderer.render_game(self._level)

        while running:
            if self._level.check_game_over():
                running = False
            if cur_shape.is_locked():
                cur_shape = Shape(randint(0, 6))
                self._level.increase_score('lock', 1)
            self.event_handler('GameView', cur_shape)
            cur_shape.move_shape('down', self._level)
            self._level.check_for_full_rows()
            self._level.add_shape_to_grid(cur_shape)
            self._renderer.render_game(self._level)
            self._clock.tick(3)
        self.start_game_over()

    def start_high_score(self):
        """ Näyttää tulosvalikon, siirtyy takaisin päävalikkoon käyttäjäsyötteellä.
        """
        while True:
            self._renderer.render_high_score()
            if self.event_handler('HighScoreView', 'shape') is False:
                break
            self._clock.tick(1)

    def start_game_over(self):
        """Näyttää pelin lopetuksen, tallentaa tuloksen tietokantaan.
        Siirtyy takaisin päävalikkoon käyttäjäsyötteellä.
        """
        self._score_repository.add_score_to_db(self._level.get_score())
        while True:
            self._renderer.render_game_over()
            if self.event_handler('HighScoreView', 'shape') is False:
                break
            self._clock.tick(1)

    def event_handler(self, view, shape):
        """ Pelaajasyötteen käsittelijä.

        Args:
            view (str): aktiivisen näkymän nimi, joka määrittää
            kulloinkin käytössä olevat syötevaihtoehdot.
            shape (obj): aktiivinen palikka, jota voi liikuttaa

        Returns:
            [bool]: tulos- ja pelin loppunäkymässa palauttaa False,
            kun käyttäjä painaa välilyöntiä, jolloin peli palautuu
            päävalikkoon.

        """

        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if view == 'StartView':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return 'game'
                    if event.key == pygame.K_SPACE:
                        return 'high_score'

            if view in ['HighScoreView', 'GameOverView']:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return False

            if view == 'GameView':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        shape.move_shape('left', self._level)
                    elif event.key == pygame.K_RIGHT:
                        shape.move_shape('right', self._level)
                    elif event.key == pygame.K_UP:
                        shape.rotate_shape(self._level)
                    elif event.key == pygame.K_DOWN:
                        shape.move_shape('down', self._level)
