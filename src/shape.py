SHAPES = ['O', 'I']
START_COORDINATES = [[[0, 0], [0, 1], [1, 0], [1, 1]],
                     [[0, 4], [1, 4], [2, 4], [3, 4]]]
COLOURS = [(45, 114, 143), (201, 93, 99)]


class Shape():
    """Luokka, joka luo, liikuttaa ja lukitsee palikoita pelissä.
    """

    def __init__(self):
        """ Luokan konstruktori, joka luo uuden tetris-palikan.
        """
        self.name = 'I'
        self.row = 0
        self.col = 4
        self.coordinates = [[0, 4], [1, 4], [2, 4], [3, 4]]
        self.rotation = 0
        self.locked = False

    def shape_fall(self, level):
        """ Siirtää palikkaa alas pelikentällä yhden rivin kerrallaan
        kunnes palikka törmää joko pelikentän pohjaan tai toiseen palikkaan.

        Args:
            level (obj): pelikenttä
        """
        level.erase_shape_from_grid(self)
        for i in range(len(self.coordinates)):
            self.coordinates[i][0] = self.coordinates[i][0] + 1
        if not self.check_no_collision(level):
            self.lock_shape()
            for j in range(len(self.coordinates)):
                self.coordinates[j][0] = self.coordinates[j][0] - 1

    def check_no_collision(self, level):
        """ Tarkistaa törmääkö palikka muihin palikoihin pelikentällä ja
        ettei palikka mene pelikentän laitojen yli.

        Args:
            level (obj): pelikenttä

        Returns:
            True, jos palikka ei törmää mihinkään, False jos palikka törmää.
        """
        for pair in self.coordinates:
            if pair[1] < 0 or pair[1] > 9:
                return False
            if pair[0] > 19:
                return False
            if level.grid[pair[0]][pair[1]] != '.' and level.grid[pair[0]][pair[1]] != self.name:
                return False
        return True

    def move_shape(self, direction, level):
        """ Liikuttaa palikkaa pelikentällä käyttäjäsyötteen mukaiseen suuntaan yhden sarakkeen
        tai rivin kerrallaan. Tarkistaa tuleeko uusissa koordinaateissa törmäyksiä, jos tulee
        niin palauttaa palikan takaisin.

        Args:
            direction (str): käyttäjäsyötteestä saatu suunta
            level (obj): pelikenttä
        """
        if not self.locked:
            level.erase_shape_from_grid(self)
            if direction == "left":
                for i in range(len(self.coordinates)):
                    self.coordinates[i][1] = self.coordinates[i][1] - 1
                if not self.check_no_collision(level):
                    for i in range(len(self.coordinates)):
                        self.coordinates[i][1] = self.coordinates[i][1] + 1
            if direction == "right":
                for i in range(len(self.coordinates)):
                    self.coordinates[i][1] = self.coordinates[i][1] + 1
                if not self.check_no_collision(level):
                    for i in range(len(self.coordinates)):
                        self.coordinates[i][1] = self.coordinates[i][1] - 1
            if direction == "down":
                # placeholder for moving down quicker
                pass

    def rotate_shape(self):
        pass

    def lock_shape(self):
        self.name = self.name.lower()
        self.locked = True
