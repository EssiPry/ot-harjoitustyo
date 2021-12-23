import pygame


class GameView:
    """Luokka joka piirtää pelin aikaisen näkymän.
    """

    def __init__(self, display, level, block_size):
        self.display = display
        self.level = level
        self.b_size = block_size

    def draw_level_grid(self):
        grid = self.level.get_grid()
        pygame.Surface.fill(self.display, (0, 0, 0))
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                block = grid[row][col]
                normalized_y = self.b_size + row * self.b_size
                normalized_x = self.b_size + col * self.b_size
                if block == '.':
                    pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(
                        normalized_x, normalized_y, self.b_size, self.b_size))
                elif block in ['o', 'O']:
                    pygame.draw.rect(self.display, (0, 0, 255), pygame.Rect(
                        normalized_x, normalized_y, self.b_size, self.b_size))
                elif block in ['i', 'I']:
                    pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(
                        normalized_x, normalized_y, self.b_size, self.b_size))
                elif block in ['t', 'T']:
                    pygame.draw.rect(self.display, (153, 76, 0), pygame.Rect(
                        normalized_x, normalized_y, self.b_size, self.b_size))
                elif block in ['j', 'J']:
                    pygame.draw.rect(self.display, (255, 128, 0), pygame.Rect(
                        normalized_x, normalized_y, self.b_size, self.b_size))
                elif block in ['l', 'L']:
                    pygame.draw.rect(self.display, (255, 0, 255), pygame.Rect(
                        normalized_x, normalized_y, self.b_size, self.b_size))
                elif block in ['s', 'S']:
                    pygame.draw.rect(self.display, (0, 255, 0), pygame.Rect(
                        normalized_x, normalized_y, self.b_size, self.b_size))
                elif block in ['z', 'Z']:
                    pygame.draw.rect(self.display, (0, 255, 255), pygame.Rect(
                        normalized_x, normalized_y, self.b_size, self.b_size))

        pygame.display.update()

    def draw_edges_to_level(self):
        pygame.draw.line(self.display, (255, 255, 255), [
                         self.b_size, self.b_size], [self.b_size*11, self.b_size], 1)
        pygame.draw.line(self.display, (255, 255, 255), [
                         self.b_size, self.b_size], [self.b_size, self.b_size*21], 1)
        pygame.draw.line(self.display, (255, 255, 255), [
                         self.b_size*11, self.b_size], [self.b_size*11, self.b_size*21], 1)
        pygame.draw.line(self.display, (255, 255, 255), [
                         self.b_size, self.b_size*21], [self.b_size*11, self.b_size*21], 1)
        pygame.display.update()

    def show_score_card(self):
        self.empty_score_card()
        pygame.draw.rect(self.display, (255, 255, 255,), pygame.Rect(
            self.b_size*13, self.b_size, self.b_size*6, self.b_size*5.5), 1)
        font = pygame.font.SysFont('helvetica', 20)
        score_text = font.render('Score:', 1, (255, 255, 255))
        score = font.render(f'{self.level.get_score()}', 1, (255, 255, 255))
        self.display.blit(
            score_text, (self.b_size*13.5, self.b_size*1.5))
        self.display.blit(score, (self.b_size*13.5, self.b_size*2.5))
        lines_text = font.render('Lines cleared:', 1, (255, 255, 255))
        lines = font.render(f'{self.level.get_lines_cleared()}', 1, (255, 255, 255))
        self.display.blit(
            lines_text, (self.b_size*13.5, self.b_size*4))
        self.display.blit(lines, (self.b_size*13.5, self.b_size*5))
        pygame.display.update()

    def empty_score_card(self):
        pygame.draw.rect(self.display, (0, 0, 0,), pygame.Rect(
            self.b_size*13, self.b_size, self.b_size*6, self.b_size*5.5))
        pygame.display.update()

    def draw_game_view(self):
        self.draw_level_grid()
        self.draw_edges_to_level()
        self.show_score_card()
