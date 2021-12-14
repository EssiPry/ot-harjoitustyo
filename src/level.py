import pygame


class Level():
    """Luokka, joka avulla ylläpidetään pelikenttää.
    """

    def __init__(self, block_size):
        """ Luokan konstruktori, joka luo uuden pelikentän.

        Args:
            block_size:
        """
        self.matrix = [['.' for x in range(10)] for y in range(20)]
        self.block_size = block_size

    def print_matrix(self):
        for row in self.matrix:
            print(row)
        print()

    def add_shape_in_matrix(self, shape):
        for pair in shape.coordinates:
            self.matrix[pair[0]][pair[1]] = shape.name

    def erase_shape_from_matrix(self, shape):
        for pair in shape.coordinates:
            self.matrix[pair[0]][pair[1]] = '.'

    def check_for_full_rows(self):
        row_counter = 0
        row_no = []
        for row in self.matrix:
            for i in range(10):
                if row[i] == '.':
                    break
                elif i == 9:
                    print("yay whole row")
                    row_no.append(row_counter)
            row_counter += 1
        return row_no

    def delete_row(self):
        pass

    def add_text(self):
        pass

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
                    pygame.draw.rect(display, (0, 0, 0), pygame.Rect(
                        normalized_x, normalized_y, self.block_size, self.block_size))
                elif block == 'B':
                    pygame.draw.rect(display, (145, 69, 182), pygame.Rect(
                        normalized_x, normalized_y, self.block_size, self.block_size))
                elif block in ['O', 'I']:
                    pygame.draw.rect(display, (255, 86, 119), pygame.Rect(
                        normalized_x, normalized_y, self.block_size, self.block_size))

        pygame.display.update()
