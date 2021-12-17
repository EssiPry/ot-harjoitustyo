from level import Level


shape_names = ['O', 'I', 'T']
SHAPE_COORDINATES = [[(0, 0), (0, 1), (1, 0), (1, 1)],
                     [(0, 0), (1, 0), (2, 0), (3, 0)],
                     [(0, 0), (0, 1), (0, 2), (1, 1)]]

shapes = {
0 : [[(0, 0), (0, 1), (1, 0), (1, 1)]],
1 : [[(0, 0), (1, 0), (2, 0), (3, 0)], [(3,0), (3,1), (3,2), (3,3,)]],
2 : [[(0, 0), (0, 1), (0, 2), (1, 1)], []]
}


class Shape:
    def __init__(self, list_index):
        self._name = shape_names[list_index]
        self._row = 0
        self._col = 4
        self._list_index = list_index
        self._rotation = 0
        self._locked = False

    def get_current_coordinates(self):
        """ Apumetodi, joka palauttaa palikan sen hetken koordinaatit
        pelikentällä listana.

        Returns:
            [list]: palikan koordinaatit
        """
        current_coordinates = []
        for coordinates in shapes[self._list_index][self._rotation]:
            row = coordinates[0] + self._row
            col = coordinates[1] + self._col
            current_coordinates.append([row, col])
        return current_coordinates

    def shape_can_be_moved(self, level):
        """ Tarkistaa voiko palikka liikkua haluttuun suuntaan pelikentällä vai
        meneekö palikka ruudukon yli tai törmääkö se lukittuun palikkaan.

        Args:
            level (obj): pelikenttä

        Returns:
            True jos palikka voi liikkua, False jos palikka menee ruudukon yli tai törmää toiseen palikkaan.
        """
        current_coordinates = self.get_current_coordinates()
        grid = level.get_grid()
        for pair in current_coordinates:
            if pair[1] < 0 or pair[1] > 9:
                return False
            if pair[0] > 19:
                return False
            if grid[pair[0]][pair[1]] != '.' and grid[pair[0]][pair[1]] != self._name:
                return False
        return True

    def shape_fall(self, level):
        """ Siirtää palikkaa alas pelikentällä yhden rivin kerrallaan
        kunnes palikka törmää joko pelikentän pohjaan tai toiseen palikkaan.

        Args:
            level (obj): pelikenttä
        """
        level.erase_shape_from_grid(self)
        self._row += 1
        if not self.shape_can_be_moved(level):
            self._row -= 1
            self.lock_shape()

    def move_shape(self, direction, level):
        """ Liikuttaa palikkaa pelikentällä käyttäjäsyötteen mukaiseen suuntaan yhden sarakkeen
        tai rivin kerrallaan. Tarkistaa tuleeko uusissa koordinaateissa törmäyksiä, jos tulee
        niin palauttaa palikan takaisin alkuperäisiin koordinaatteiihin.

        Args:
            direction (str): käyttäjäsyötteestä saatu suunta
            level (obj): pelikenttä
        """
        if not self._locked:
            level.erase_shape_from_grid(self)
            if direction == "left":
                self._col -= 1
                if not self.shape_can_be_moved(level):
                    self._col += 1
            if direction == "right":
                self._col += 1
                if not self.shape_can_be_moved(level):
                    self._col -= 1
            if direction == "down":
                # placeholder for moving down quicker
                pass

    def rotate_shape(self, level):
        level.erase_shape_from_grid(self)
        if self._name == 'O':
            pass
        if self._name == 'I':
            if self._rotation == 1:
                self._rotation = 0
                if not self.shape_can_be_moved(level):
                    self._rotation = 1
            else:
                self._rotation += 1
                if not self.shape_can_be_moved(level):
                    self._rotation = 0

    def lock_shape(self):
        """ Lukitsee palikan ja muuttaa palikan nimen pieneksi alkukirjaimeksi.
        """
        self._name = self._name.lower()
        self._locked = True

    def is_locked(self):
        return self._locked
