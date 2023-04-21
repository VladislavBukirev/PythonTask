import unittest

from constants import COUNT_BLOCKS
from snake import Snake, SnakeBlock


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_add_score(self):
        self.snake.add_score(10)
        self.assertEqual(self.snake.score, 10)

    def test_set_speed(self):
        self.snake.set_speed(1)
        self.assertEqual(self.snake.speed, 6)

    def test_increase_length(self):
        original_length = len(self.snake.blocks)
        self.snake.increase_length()
        new_length = len(self.snake.blocks)
        self.assertEqual(new_length, original_length + 1)

    def test_reduce_length(self):
        original_length = len(self.snake.blocks)
        self.snake.reduce_length()
        new_length = len(self.snake.blocks)
        self.assertEqual(new_length, original_length - 1)

    def test_is_inside(self):
        block = SnakeBlock(9, 9)
        self.assertTrue(block.is_inside())

        block = SnakeBlock(12, 2)
        self.assertTrue(block.is_inside())

        block = SnakeBlock(0, -1)
        self.assertFalse(block.is_inside())

        block = SnakeBlock(COUNT_BLOCKS, 0)
        self.assertFalse(block.is_inside())

        block = SnakeBlock(0, COUNT_BLOCKS)
        self.assertFalse(block.is_inside())
