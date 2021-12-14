import unittest
from shape import Shape
from level import Level


class TestShape(unittest.TestCase):
    def setUp(self):
        self.test_shape = Shape()
        self.test_level = Level(25)

    def test_shape_ctor(self):
        self.assertEqual(self.test_shape.name, 'I')
        self.assertEqual(self.test_shape.coordinates, [
                         [0, 4], [1, 4], [2, 4], [3, 4]])
        self.assertEqual(self.test_shape.rotation, 0)
        self.assertEqual(self.test_shape.colour, (145, 69, 182))
        self.assertFalse(self.test_shape.locked)

    def test_move_shape_left(self):
        self.test_shape.move_shape('left', self.test_level)
        self.assertEqual(self.test_shape.coordinates, [
                         [0, 3], [1, 3], [2, 3], [3, 3]])

    def test_move_shape_right(self):
        self.test_shape.move_shape('right', self.test_level)
        self.assertEqual(self.test_shape.coordinates, [
                         [0, 5], [1, 5], [2, 5], [3, 5]])

    def test_check_no_collisions(self):
        self.assertTrue(self.test_shape.check_no_collision(self.test_level))

    def test_check_no_collision_when_there_is_a_collision(self):
        self.test_shape.coordinates = [[17, 4], [18, 4], [19, 4], [20, 4]]
        self.assertFalse(self.test_shape.check_no_collision(self.test_level))

    def test_lock_shape(self):
        self.test_shape.lock_shape()
        self.assertTrue(self.test_shape.locked)
        self.assertEqual(self.test_shape.name, 'B')
