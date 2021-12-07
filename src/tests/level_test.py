import unittest

from level import Level
from sprites.block import Block


LEVEL_MAP = [[3,3,3,3,3,3,3],
             [2,0,0,0,0,0,2],
             [2,0,0,0,0,0,2],
             [2,0,0,0,0,0,2],
             [2,0,0,0,0,0,2],
             [2,0,0,0,0,0,2],
             [2,0,0,0,0,0,2],
             [2,0,0,0,0,0,2],
             [2,0,0,0,0,0,2],
             [2,0,0,0,0,0,2],
             [2,0,0,0,0,0,2],
             [1,1,1,1,1,1,1]]

CELL_SIZE = 30

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.test_level = Level(LEVEL_MAP, CELL_SIZE)
        self.test_level.block = Block(CELL_SIZE*3, CELL_SIZE)

    def test_new_block_exists(self):
        self.test_level._new_block()
        self.assertIsNotNone(self.test_level.block)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_block_move_left(self):
        block = self.test_level.block
        self.assert_coordinates_equal(block, CELL_SIZE*3, CELL_SIZE)

        self.test_level._block_move("left")
        self.assert_coordinates_equal(block, CELL_SIZE*2, CELL_SIZE)

    def test_block_move_right(self):
        block = self.test_level.block
        self.assert_coordinates_equal(block, CELL_SIZE*3, CELL_SIZE)

        self.test_level._block_move("right")
        self.assert_coordinates_equal(block, CELL_SIZE*4, CELL_SIZE)
