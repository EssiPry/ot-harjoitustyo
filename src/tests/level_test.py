import unittest
from level import Level
from shape import Shape


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.test_level = Level()
        self.test_shape = Shape(1)  # testataan palikkaa I

    def test_level_ctor(self):
        self.assertEqual(len(self.test_level._grid), 20)
        self.assertEqual(self.test_level._score, 0)

    def test_add_shape_to_grid(self):
        self.test_level.add_shape_to_grid(self.test_shape)
        self.assertEqual(self.test_level._grid[1][4], 'I')
        self.assertEqual(self.test_level._grid[1][5], 'I')
        self.assertEqual(self.test_level._grid[1][6], 'I')
        self.assertEqual(self.test_level._grid[1][7], 'I')

    def test_erase_shape_from_grid(self):
        self.test_level.add_shape_to_grid(self.test_shape)
        self.assertEqual(self.test_level._grid[1][4], 'I')
        self.test_level.erase_shape_from_grid(self.test_shape)
        self.assertEqual(self.test_level._grid[0][4], '.')

    def test_check_for_full_rows(self):
        for i in range(10):
            self.test_level._grid[5][i] = 't'
            self.test_level._grid[6][i] = 't'
        self.assertEqual(self.test_level.check_for_full_rows(), 2)

    def test_check_for_full_rows_none(self):
        self.assertEqual(self.test_level.check_for_full_rows(), 0)
        self.test_level._grid[3][2] = 't'
        self.assertEqual(self.test_level.check_for_full_rows(), 0)

    def test_delete_and_drop_rows(self):
        self.test_level._grid[5][1] = 'T'
        self.test_level._grid[0][0] = 'T'
        self.test_level.delete_and_drop_rows(5)
        self.assertEqual(self.test_level._grid[5][1], '.')
        self.assertEqual(self.test_level._grid[1][0], 'T')
        self.assertEqual(self.test_level._grid[0][0], '.')

    def test_check_game_over(self):
        self.assertFalse(self.test_level.check_game_over())
        for letter in ['o', 'i', 't', 'j', 'l', 's', 'z']:
            print(letter)
            self.test_level._grid[0][5] = letter
            self.assertTrue(self.test_level.check_game_over())

    def test_check_game_over_not_game_over(self):
        self.assertFalse(self.test_level.check_game_over())
        self.test_level._grid[0][5] = 'T'
        self.assertFalse(self.test_level.check_game_over())

    def test_increase_score(self):
        self.test_level.increase_score('row', 2)
        self.assertEqual(self.test_level._score, 10)
        self.test_level.increase_score('block', 5)
        self.assertEqual(self.test_level._score, 11)

    def test_get_score(self):
        self.assertEqual(self.test_level.get_score(), 0)
        self.test_level.increase_score('row', 5)
        self.assertEqual(self.test_level.get_score(), 25)
