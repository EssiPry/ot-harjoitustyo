import unittest
from level import Level
from shape import Shape


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.test_level = Level(30)
        self.test_shape = Shape()

    def test_level_ctor(self):
        self.assertEqual(len(self.test_level.grid), 20)
        self.assertEqual(self.test_level.block_size, 30)

    def test_add_shape_to_grid(self):
        self.test_level.add_shape_to_grid(self.test_shape)
        self.assertEqual(self.test_level.grid[0][4], 'I')
        self.assertEqual(self.test_level.grid[1][4], 'I')
        self.assertEqual(self.test_level.grid[2][4], 'I')
        self.assertEqual(self.test_level.grid[3][4], 'I')

    def test_erase_shape_from_grid(self):
        self.test_level.add_shape_to_grid(self.test_shape)
        self.assertEqual(self.test_level.grid[0][4], 'I')
        self.test_level.erase_shape_from_grid(self.test_shape)
        self.assertEqual(self.test_level.grid[0][4], '.')

    def test_check_for_full_rows(self):
        for i in range(10):
            self.test_level.grid[5][i] = 't'
            self.test_level.grid[6][i] = 't'
        self.test_level.grid[3][2] = 't'
        self.assertEqual(self.test_level.check_for_full_rows(), 2)

    def test_check_game_over(self):
        self.assertFalse(self.test_level.check_game_over())
        self.test_level.grid[0][5] = 'i'
        self.assertTrue(self.test_level.check_game_over())
