import unittest
from level import Level
from shape import Shape


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.test_level = Level()
        self.test_shape = Shape(1)  # testataan I

    def test_level_ctor(self):
        self.assertEqual(len(self.test_level._grid), 20)
        self.assertEqual(self.test_level._score, 0)

    def test_add_shape_to_grid(self):
        self.test_level.add_shape_to_grid(self.test_shape)
        self.assertEqual(self.test_level._grid[0][4], 'I')
        self.assertEqual(self.test_level._grid[1][4], 'I')
        self.assertEqual(self.test_level._grid[2][4], 'I')
        self.assertEqual(self.test_level._grid[3][4], 'I')

    def test_erase_shape_from_grid(self):
        self.test_level.add_shape_to_grid(self.test_shape)
        self.assertEqual(self.test_level._grid[0][4], 'I')
        self.test_level.erase_shape_from_grid(self.test_shape)
        self.assertEqual(self.test_level._grid[0][4], '.')

    def test_check_for_full_rows(self):
        for i in range(10):
            self.test_level._grid[5][i] = 't'
            self.test_level._grid[6][i] = 't'
        self.test_level._grid[3][2] = 't'
        self.assertEqual(self.test_level.check_for_full_rows(), 2)

    def test_check_game_over(self):
        self.assertFalse(self.test_level.check_game_over())
        self.test_level._grid[0][5] = 'i'
        self.assertTrue(self.test_level.check_game_over())

    def test_increase_score(self):
        self.test_level.increase_score(2)
        self.assertEqual(self.test_level._score, 10)
