import unittest
from scripts.game import Game
from scripts.snake import SnakeBlock


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_check_collision_obstacle(self):
        self.game.level.obstacles = [(10, 9)]
        self.game.snake.direction = [1, 0]
        self.game.check_collision()
        self.assertEqual(self.game.snake.lives, 2)

    def test_check_collision_wall(self):
        self.game.snake.blocks[-1].x = 0
        self.game.snake.direction = [-1, 0]
        self.game.check_collision()
        self.assertEqual(self.game.snake.lives, 2)

    def test_check_collision_self(self):
        self.game.snake.blocks = [SnakeBlock(9, 9), SnakeBlock(9, 8), SnakeBlock(9, 7)]
        self.game.snake.direction = [0, 1]
        self.game.check_collision()
        self.assertEqual(self.game.snake.lives, 2)

    def test_check_collision_no_collision(self):
        self.game.snake.direction = [1, 0]
        self.game.check_collision()
        self.assertEqual(self.game.snake.lives, 3)
