class Level():
    """Luokka, joka avulla ylläpidetään palikoiden sijaintia pelikentällä ja
    joka laskee käynnissä olevan pelin pisteet ja poistettujen rivien määrän.
    """

    def __init__(self):
        """ Luokan konstruktori, joka luo uuden tyhjän pelikentän ja
        asettaa pistelaskurin ja poistettujen rivien määrän nollaan.
        """

        self._grid = [['.' for x in range(10)] for y in range(20)]
        self._score = 0
        self._lines_cleared = 0

    def add_shape_to_grid(self, shape):
        """ Lisää palikan matriisiin.
        """
        shape_coordinates = shape.get_current_coordinates()
        for pair in shape_coordinates:
            self._grid[pair[0]][pair[1]] = shape.get_name()

    def erase_shape_from_grid(self, shape):
        """ Poistaa palikan matriisista ja koordinaatit korvaa tyhjällä.
        """
        shape_coordinates = shape.get_current_coordinates()
        for pair in shape_coordinates:
            self._grid[pair[0]][pair[1]] = '.'

    def check_for_full_rows(self):
        """ Käy matriisin läpi ja tarkistaa onko pelikentällä täysiä vaakarivejä palikoita.
        Jos on niin kutsuu drop_row -metodia, joka poistaa täyden rivin ja pudottaa
        ylempänä olevia rivejä.

        Returns:
            [int]: täysien rivien lukumäärä
        """

        lines_deleted = 0
        row_number = 0
        for row in self._grid:
            for i in range(10):
                if row[i] == '.':
                    break
                if i == 9:
                    self.delete_and_drop_rows(row_number)
                    lines_deleted += 1
            row_number += 1
        self.increase_score('row', lines_deleted)
        self.increase_lines_cleared(lines_deleted)
        return lines_deleted

    def delete_and_drop_rows(self, row_number):
        """ Poistaa täyden rivin ja lisää uuden tyhjän rivin pelikentän ensimmäiseksi riviksi.

        Args:
            row_number (int): poistettavan rivin rivinumero
        """
        self._grid.pop(row_number)
        self._grid.insert(0, ['.' for x in range(10)])

    def check_game_over(self):
        """ Tarkistaa onko peli päättynyt eli onko ensimmäisellä rivillä lukittuja palikoita.

        Returns:
            True, jos ylärivillä on lukittuja palikoita, muussa tapauksessa False.
        """
        for i in range(9):
            if self._grid[0][i] in ['o', 'i', 't', 'j', 'l', 's', 'z']:
                return True
        return False

    def increase_score(self, kind, number_of_lines):
        """ Lisää pistelaskuriin pisteen jokaisesta lukitusta palikasta
        ja 5 pistettä jokaisesta poistetusta rivistä

        Args:
            kind (str): kertoo pistetyypin lukittu vai rivi
            number_of_lines (int): kierroksella poistettujen rivin lukumäärä
        """
        if kind == 'lock':
            self._score += 1
        elif kind == 'row':
            self._score += 5 * number_of_lines

    def increase_lines_cleared(self, number_of_lines):
        """ Kasvattaa poistettujen rivien määrää.

        Args:
            number_of_lines (int): kierroksella poistettujen rivien lukumäärä
        """
        self._lines_cleared += number_of_lines

    def get_grid(self):
        return self._grid

    def get_score(self):
        return self._score

    def get_lines_cleared(self):
        return self._lines_cleared
