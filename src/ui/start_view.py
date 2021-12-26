import pygame


class StartView:
    """Luokka joka piirtää pelin aloitusnäkymän.
    """

    def __init__(self, display, block_size):
        self._display = display
        self._b_size = block_size

    def draw_start_game(self):
        self._display.fill((0, 0, 0))
        self.display_text(45, 'TETRIS', 7, 2.5)
        self.display_text(25, 'Press enter to', 7, 6)
        self.display_text(25, 'start the game', 7, 7)
        self.display_text(25, 'Press space to', 7, 10)
        self.display_text(25, 'view high scores', 6.6, 11)
        self.draw_shapes()


    def display_text(self, font_size, text, d_x, d_y):
        font = pygame.font.SysFont('helvetica', font_size)
        to_be_displayed = font.render(text, 1, (255, 255, 255))
        self._display.blit(
            to_be_displayed, (self._b_size*d_x, self._b_size*d_y))
        pygame.display.update()

    def draw_shapes(self):
        grid = [[0,'z',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'s',0],
                ['z','z','l',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'s','s'],
                ['z','z','l',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'t','s'],
                ['z','z','l','l',0,0,0,0,0,0,0,0,0,0,0,0,0,'t','t','i'],
                ['z','l','l','o','o',0,0,0,0,0,0,0,0,0,0,'j','l','s','t','i'],
                ['o','o','l','o','o',0,0,0,0,0,0,0,0,0,0,'j','l','s','s','i'],
                ['o','o','l','i','i','i','i',0,0,0,0,0,0,0,'j','j','l','l','s','i'],
                ]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                block = grid[row][col]
                normalized_y = self._b_size*15 + row * self._b_size
                normalized_x = col * self._b_size
                if block == '.':
                    pygame.draw.rect(self._display, (0, 0, 0), pygame.Rect(
                        normalized_x, normalized_y, self._b_size, self._b_size))
                elif block in ['o', 'O']:
                    pygame.draw.rect(self._display, (0, 0, 255), pygame.Rect(
                        normalized_x, normalized_y, self._b_size, self._b_size))
                elif block in ['i', 'I']:
                    pygame.draw.rect(self._display, (255, 0, 0), pygame.Rect(
                        normalized_x, normalized_y, self._b_size, self._b_size))
                elif block in ['t', 'T']:
                    pygame.draw.rect(self._display, (153, 76, 0), pygame.Rect(
                        normalized_x, normalized_y, self._b_size, self._b_size))
                elif block in ['j', 'J']:
                    pygame.draw.rect(self._display, (255, 128, 0), pygame.Rect(
                        normalized_x, normalized_y, self._b_size, self._b_size))
                elif block in ['l', 'L']:
                    pygame.draw.rect(self._display, (255, 0, 255), pygame.Rect(
                        normalized_x, normalized_y, self._b_size, self._b_size))
                elif block in ['s', 'S']:
                    pygame.draw.rect(self._display, (0, 255, 0), pygame.Rect(
                        normalized_x, normalized_y, self._b_size, self._b_size))
                elif block in ['z', 'Z']:
                    pygame.draw.rect(self._display, (0, 255, 255), pygame.Rect(
                        normalized_x, normalized_y, self._b_size, self._b_size))
        pygame.display.update()
