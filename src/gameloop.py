import pygame


class Gameloop():

    def __init__(self):
        pass

    def start(self):
        pass

    def get_events(self):
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
                    # placeholder for rotate block
                    pass
                elif event.key == pygame.K_DOWN:
                    # placeholder for move block down
                    pass
        return True

    def draw_level():
        pass
