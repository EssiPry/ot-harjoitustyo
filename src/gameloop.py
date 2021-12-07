import pygame

class Gameloop:

    def __init__(self, clock, display, level, renderer):
        self._clock = clock
        self._display = display
        self._level = level
        self._renderer = renderer

    def start(self):
        self._level._new_block()
        while True:
            if self.event_handler() == False:
                break

            self._level._block_fall()
            self._renderer.render()
            self._clock.tick(45)

            if self._level._check_game_over():
                break

    def get_event(self):
        return pygame.event.get()

    def event_handler(self):
        for event in self.get_event():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._level._block_move("left")
                elif event.key == pygame.K_RIGHT:
                    self._level._block_move("right")
                elif event.key == pygame.K_UP:
                    #placeholder for rotate block
                    pass
                elif event.key == pygame.K_DOWN:
                    #placeholder for move block down
                    pass
        return True
