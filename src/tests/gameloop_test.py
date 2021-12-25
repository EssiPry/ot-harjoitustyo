import unittest
import pygame

from gameloop.gameloop import Gameloop


class StubClock:
    def tick(self, fps):
        pass


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def render_start(self):
        pass

    def render_game(self):
        pass

    def render_high_score(self):
        pass


class TestGameloop(unittest.TestCase):

    def test_event_handler_start_view(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_SPACE)]
        gameloop = Gameloop(
            StubClock(),
            StubEventQueue(events),
            StubRenderer(),
        )
        self.assertEqual(gameloop.event_handler(
            'StartView', 'shape'), 'high_score')

        events = [StubEvent(pygame.KEYDOWN, pygame.K_RETURN)]
        gameloop = Gameloop(
            StubClock(),
            StubEventQueue(events),
            StubRenderer(),
        )
        self.assertEqual(gameloop.event_handler('StartView', 'shape'), 'game')

    def test_event_handler_high_score_view(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_SPACE)]
        gameloop = Gameloop(
            StubClock(),
            StubEventQueue(events),
            StubRenderer(),
        )
        self.assertFalse(gameloop.event_handler('HighScoreView', 'shape'))
