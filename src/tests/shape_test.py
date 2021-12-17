import unittest
from shape import Shape
from level import Level

SHAPES = ['O', 'I', 'T']
SHAPE_COORDINATES = [[(0, 0), (0, 1), (1, 0), (1, 1)],
                     [(0, 0), (1, 0), (2, 0), (3, 0)],
                     [(0, 0), (0, 1), (0, 2), (1, 1)]]


class TestShape(unittest.TestCase):
    def setUp(self):
        self.test_shape = Shape(2)
        self.test_level = Level()

    def test_shape_ctor(self):
        self.assertEqual(self.test_shape._name, 'T')
        self.assertEqual(self.test_shape._row, 0)
        self.assertEqual(self.test_shape._col, 4)
        self.assertEqual(self.test_shape._list_index, 2)
        self.assertFalse(self.test_shape._locked)

    def test_get_current_coordinates(self):
        self.assertEqual(self.test_shape.get_current_coordinates(), [
                         [0, 4], [0, 5], [0, 6], [1, 5]])

    def test_shape_can_be_moved(self):
        self.test_shape._col = -1
        self.assertFalse(self.test_shape.shape_can_be_moved(self.test_level))
        self.test_shape._col = 5
        self.test_shape._row = 20
        self.assertFalse(self.test_shape.shape_can_be_moved(self.test_level))

    def test_move_shape_left(self):
        self.test_shape.move_shape('left', self.test_level)
        self.assertEqual(self.test_shape._col, 3)

    def test_move_shape_right(self):
        self.test_shape.move_shape('right', self.test_level)
        self.assertEqual(self.test_shape._col, 5)

    def test_move_shape_fall(self):
        self.test_shape.shape_fall(self.test_level)
        self.assertEqual(self.test_shape._row, 1)

    def test_lock_shape(self):
        self.test_shape.lock_shape()
        self.assertTrue(self.test_shape._locked)
        self.assertEqual(self.test_shape._name, 't')
