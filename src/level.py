import pygame

class Level():
    """Luokka, joka avulla ylläpidetään palikoiden sijaintia pelikentällä.
    """

    def __init__(self, block_size):
        """ Luokan konstruktori, joka luo uuden pelikentän.

        Args:
            block_size (int): pelikentän yksittäisen ruudun sivun pituus
        """

        self.matrix = [['.' for x in range(10)] for y in range(20)]
        self.block_size = block_size

    def print_matrix(self):
        """ Piirtää matriisin terminaalissa. Debuggaukseen, poistunee varsinaisesta versiosta.
        """
        for row in self.matrix:
            print(row)
        print()

    def add_shape_in_matrix(self, shape):
        """ Lisää palikan koordinaattien paikalle palikan nimen matriisissa.
        """
        for pair in shape.coordinates:
            self.matrix[pair[0]][pair[1]] = shape.name

    def erase_shape_from_matrix(self, shape):
        """ Poistaa palikan nimen palikan koordinaateista matriisista.
        """
        for pair in shape.coordinates:
            self.matrix[pair[0]][pair[1]] = '.'

    def check_for_full_rows(self):
        """ Käy matriisin läpi ja tarkistaa onko pelikentällä täysiä vaakarivejä palikoita.
        Jos on niin kutsuu drop_row -metodia, joka poistaa täyden rivin ja pudottaa ylempänä olevia rivejä.
        """
        rows_deleted = 0
        row_number = 0
        for row in self.matrix:
            for i in range(10):
                if row[i] == '.':
                    break
                if i == 9:
                    self.delete_and_drop_rows(row_number)
                    rows_deleted +=1
            row_number += 1
        return rows_deleted

    def delete_and_drop_rows(self, row_number):
        """ Poistaa rivin ja lisää uuden tyhjän rivin pelikentän ensimmäiseksi riviksi.

        Args:
            row_number (int): poistettavan rivin rivinumero
        """
        self.matrix.pop(row_number)
        self.matrix.insert(0, ['.' for x in range(10)])

    def check_game_over(self):
        """ Tarkistaa onko peli päättynyt.

        Returns:
            True, jos ylärivillä on lukittuja palikoita, muussa tapauksessa False.
        """
        for i in range(9):
            if self.matrix[0][i] in ['o', 'i']:
                return True
        return False

    def draw_level(self, display):
        """ Käy läpi matriisin ja piirtää sen mukaan pelikentän ja palikat pygameen.
        """
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                block = self.matrix[y][x]
                normalized_y = y * self.block_size
                normalized_x = x * self.block_size
                if block == '.':
                    pygame.draw.rect(display, (0, 0, 0), pygame.Rect(
                        normalized_x, normalized_y, self.block_size, self.block_size))
                elif block in ['o', 'i']:
                    pygame.draw.rect(display, (145, 69, 182), pygame.Rect(
                        normalized_x, normalized_y, self.block_size, self.block_size))
                elif block in ['O', 'I']:
                    pygame.draw.rect(display, (255, 86, 119), pygame.Rect(
                        normalized_x, normalized_y, self.block_size, self.block_size))

        pygame.display.update()
