import random

#shapes = ['O', 'I']
#shape_coordinates = [[[0, 4],[0, 5],[1, 4],[1, 5]], [[1,2],[2,2],[3,2],[4,2]]]


class Shape():

    def __init__(self):
        self.name = 'I'
        # list of coordinates: [y-coordinate, x-coordinate]
        self.coordinates = [[0, 4], [1, 4], [2, 4], [3, 4]]
        self.rotation = 0
        self.colour = (145, 69, 182)
        self.locked = False

    def get_new_shape(self):
        return random.randint(0, 1)

    def shape_fall(self, level):
        self.erase_shape_from_matrix(level)
        for i in range(len(self.coordinates)):
            self.coordinates[i][0] = self.coordinates[i][0] + 1
        if not self.check_no_collisions(level):
            self.lock_shape()
            for j in range(len(self.coordinates)):
                self.coordinates[j][0] = self.coordinates[j][0] - 1

    def check_no_collisions(self, level):
        for pair in self.coordinates:
            if pair[1] < 0 or pair[1] > 9:
                return False
            if pair[0] > 19:
                return False
            if level.matrix[pair[0]][pair[1]] != '.' and level.matrix[pair[0]][pair[1]] != self.name:
                return False
        return True

    def move_shape(self, direction, level):
        self.erase_shape_from_matrix(level)
        if direction == "left":
            for i in range(len(self.coordinates)):
                self.coordinates[i][1] = self.coordinates[i][1] - 1
            if not self.check_no_collisions(level):
                for i in range(len(self.coordinates)):
                    self.coordinates[i][1] = self.coordinates[i][1] + 1
        if direction == "right":
            for i in range(len(self.coordinates)):
                self.coordinates[i][1] = self.coordinates[i][1] + 1
            if not self.check_no_collisions(level):
                for i in range(len(self.coordinates)):
                    self.coordinates[i][1] = self.coordinates[i][1] - 1
        if direction == "down":
            # placeholder for moving down quicker
            pass

    def erase_shape_from_matrix(self, level):
        for pair in self.coordinates:
            level.matrix[pair[0]][pair[1]] = '.'

    def lock_shape(self):
        self.name = 'B'
        self.locked = True
