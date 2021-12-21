import unittest
from shape import Shape
from level import Level


class TestShape(unittest.TestCase):
    def setUp(self):
        self.test_shape = Shape(2) # T
        self.test_level = Level()

    def test_shape_ctor(self):
        self.assertEqual(self.test_shape._name, 'T')
        self.assertEqual(self.test_shape._row, 0)
        self.assertEqual(self.test_shape._col, 4)
        self.assertEqual(self.test_shape._list_index, 2)
        self.assertFalse(self.test_shape._locked)

    def test_get_current_coordinates(self):
        self.assertEqual(self.test_shape.get_current_coordinates(), [
                         [0, 5], [1, 4], [1, 5], [1, 6]])

    def test_shape_can_be_moved(self):
        self.test_shape._col = -1
        self.assertFalse(self.test_shape.shape_can_be_moved(self.test_level))
        self.test_shape._col = 10
        self.assertFalse(self.test_shape.shape_can_be_moved(self.test_level))
        self.test_shape._col = 4
        self.test_shape._row = 20
        self.assertFalse(self.test_shape.shape_can_be_moved(self.test_level))
        self.test_level._grid[18][4] = 'L'
        self.test_shape._row = 17
        self.assertFalse(self.test_shape.shape_can_be_moved(self.test_level))

    def test_move_shape_left(self):
        self.test_shape.move_shape('left', self.test_level)
        self.assertEqual(self.test_shape._col, 3)


    def test_move_shape_left_cannot_be_moved(self):
        self.test_shape._col = 0
        self.test_shape.move_shape('left', self.test_level)
        self.assertEqual(self.test_shape._col, 0)

    def test_move_shape_right(self):
        self.test_shape.move_shape('right', self.test_level)
        self.assertEqual(self.test_shape._col, 5)

    def test_move_shape_fall(self):
        self.test_shape.shape_fall(self.test_level)
        self.assertEqual(self.test_shape._row, 1)

    def test_rotate_shape(self):
        self.assertEqual(self.test_shape._rotation, 0)
        self.test_shape.rotate_shape(self.test_level)
        self.assertEqual(self.test_shape._rotation, 1)
        self.test_shape.rotate_shape(self.test_level)
        self.test_shape.rotate_shape(self.test_level)
        self.test_shape.rotate_shape(self.test_level)
        self.assertEqual(self.test_shape._rotation, 0)
        self.test_shape._name = 'O'
        self.test_shape.rotate_shape(self.test_level)
        self.assertEqual(self.test_shape._rotation, 0)

    def test_rotate_shape_counter_clockwise(self):
        self.assertEqual(self.test_shape._rotation, 0)
        self.test_shape.rotate_shape_counter_clockwise(self.test_level)
        self.assertEqual(self.test_shape._rotation, 3)
        self.test_shape.rotate_shape_counter_clockwise(self.test_level)
        self.assertEqual(self.test_shape._rotation, 2)

    def test_lock_shape(self):
        self.test_shape.lock_shape()
        self.assertTrue(self.test_shape._locked)
        self.assertEqual(self.test_shape._name, 't')

    def test_is_locked(self):
        self.assertFalse(self.test_shape.is_locked())

    def test_get_name(self):
        self.assertEqual(self.test_shape.get_name(), 'T')
