import pygame
from shape import Shape

class Level():

    def __init__(self, block_size):
        self.matrix = [['.' for x in range(10)] for y in range(20)]
        self.block_size = block_size

    def print_matrix(self):
        for row in self.matrix:
            print(row)
        print()

    def show_shape_in_matrix(self, shape):
        for pair in shape.coordinates:
            self.matrix[pair[0]][pair[1]] = shape.name

    def check_for_full_rows(self):
        row_counter = 0
        row_no = []
        for row in self.matrix:
            for i in range(10):
                if row[i] == '.':
                    print("not a full row")
                    break
                elif i == 9:
                    print("yay whole row")
                    row_no.append(row_counter)
            row_counter += 1
            print(row_no)

    def delete_row(self):
        pass

    def add_text(self):
        pass

    def help_test_check_rows(self):
        for i in range(10):
            self.matrix[5][i] = 'T'

    def check_game_over(self):
        for i in range(9):
            if self.matrix[0][i] == 'B':
                return True
        return False

    def draw_level(self, display):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                block = self.matrix[y][x]
                normalized_y = y * self.block_size
                normalized_x = x * self.block_size
                if block == '.':
                    pygame.draw.rect(display, (0,0,0), pygame.Rect(normalized_x, normalized_y, self.block_size, self.block_size))
                elif block == 'B':
                    pygame.draw.rect(display, (145, 69, 182), pygame.Rect(normalized_x, normalized_y, self.block_size, self.block_size))
                elif block == 'O':
                    pygame.draw.rect(display, (255, 86, 119), pygame.Rect(normalized_x, normalized_y, self.block_size, self.block_size))

        pygame.display.update()
