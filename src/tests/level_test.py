import unittest
from level import Level
from shape import Shape


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.test_level = Level(30)
        self.test_shape = Shape()

    def test_level_ctor(self):
        self.assertEqual(len(self.test_level.matrix), 20)
        self.assertEqual(self.test_level.block_size, 30)

    def test_add_shape_in_matrix(self):
        self.test_level.add_shape_in_matrix(self.test_shape)
        self.assertEqual(self.test_level.matrix[0][4], 'I')
        self.assertEqual(self.test_level.matrix[1][4], 'I')
        self.assertEqual(self.test_level.matrix[2][4], 'I')
        self.assertEqual(self.test_level.matrix[3][4], 'I')

    def test_erase_shape_from_matrix(self):
        self.test_level.add_shape_in_matrix(self.test_shape)
        self.assertEqual(self.test_level.matrix[0][4], 'I')
        self.test_level.erase_shape_from_matrix(self.test_shape)
        self.assertEqual(self.test_level.matrix[0][4], '.')

    def test_check_for_full_rows(self):
        for i in range(10):
            self.test_level.matrix[5][i] = 'T'
        self.assertEqual(self.test_level.check_for_full_rows(), [5])

    def test_check_game_over(self):
        self.assertFalse(self.test_level.check_game_over())
        self.test_level.matrix[0][5] = 'B'
        self.assertTrue(self.test_level.check_game_over())
