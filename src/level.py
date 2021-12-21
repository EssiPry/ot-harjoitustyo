class Level():
    """Luokka, joka avulla ylläpidetään palikoiden sijaintia pelikentällä ja
    joka laskee käynnissä olevan pelin pisteet.
    """

    def __init__(self):
        """ Luokan konstruktori, joka luo uuden tyhjän pelikentän ja
        asettaa pistelaskurin ja poistettujen rivien määrän nollaan.
        """

        self._grid = [['.' for x in range(10)] for y in range(20)]
        self._score = 0
        self._lines_removed = 0

    def print_grid(self):
        """ Piirtää matriisin terminaalissa. Debuggaukseen.
        """
        for row in self._grid:
            print(row)
        print()

    def add_shape_to_grid(self, shape):
        """ Lisää palikan koordinaattien paikalle palikan nimen matriisissa.
        """
        shape_coordinates = shape.get_current_coordinates()
        for pair in shape_coordinates:
            self._grid[pair[0]][pair[1]] = shape.get_name()

    def erase_shape_from_grid(self, shape):
        """ Poistaa palikan nimen palikan koordinaateista matriisista.
        """
        shape_coordinates = shape.get_current_coordinates()
        for pair in shape_coordinates:
            self._grid[pair[0]][pair[1]] = '.'

    def check_for_full_rows(self):
        """ Käy matriisin läpi ja tarkistaa onko pelikentällä täysiä vaakarivejä palikoita.
        Jos on niin kutsuu drop_row -metodia, joka poistaa täyden rivin ja pudottaa
        ylempänä olevia rivejä.
        """
        rows_deleted = 0
        row_number = 0
        for row in self._grid:
            for i in range(10):
                if row[i] == '.':
                    break
                if i == 9:
                    self.delete_and_drop_rows(row_number)
                    rows_deleted += 1
            row_number += 1
        self.increase_score('row', rows_deleted)
        return rows_deleted

    def delete_and_drop_rows(self, row_number):
        """ Poistaa rivin ja lisää uuden tyhjän rivin pelikentän ensimmäiseksi riviksi.

        Args:
            row_number (int): poistettavan rivin rivinumero
        """
        self._grid.pop(row_number)
        self._grid.insert(0, ['.' for x in range(10)])
        self._lines_removed += 1

    def check_game_over(self):
        """ Tarkistaa onko peli päättynyt.

        Returns:
            True, jos ylärivillä on lukittuja palikoita, muussa tapauksessa False.
        """
        for i in range(9):
            if self._grid[0][i] in ['o', 'i', 't', 'j', 'l', 's', 'z']:
                return True
        return False

    def increase_score(self, kind, number_rows):
        """lisää pistelaskuriin pisteen jokaisesta lukitusta palikasta
        ja 5 pistettä jokaisesta poistetusta rivistä

        Args:
            type (str): lukitseminen vai rivipisteet
            rows (int): kierroksella poistettujen rivin lkm
        """
        if kind == 'lock':
            self._score += 1
        elif kind == 'row':
            self._score += 5 * number_rows

    def get_grid(self):
        return self._grid

    def get_score(self):
        return self._score

    def get_lines_removed(self):
        return self._lines_removed
