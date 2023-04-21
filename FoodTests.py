import unittest
import random

from food import Food, GoldenApple, BadApple, Storm, BadStorm, Chest
from snake import Snake


class TestFood(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()
        self.food = Food(self.snake)
        self.food.foods = {
            'golden_apple': GoldenApple(),
            'bad_apple': BadApple(),
            'storm': Storm(),
            'bad_storm': BadStorm(),
            'chest': Chest(),
            }

    def test_create_new_food(self):
        self.food.create_new_food()
        self.assertEqual(len(self.food.foods_list), 3)

    def test_check_collision(self):
        x, y, item = self.food.foods_list[0]
        collided = self.food.check_collision(x, y)
        self.assertTrue(collided)
        self.assertEqual(len(self.food.foods_list), 3)

    def test_not_collision(self):
        x, y, item = -1, -1, random.choice([key for key in self.food.foods])
        collided = self.food.check_collision(x, y)
        self.assertFalse(collided)
        self.assertEqual(len(self.food.foods_list), 3)
