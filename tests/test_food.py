from unittest import TestCase, main
import random

from scripts.food import Food, GoldenApple, BadApple, Storm, BadStorm, Chest, Fruit
from scripts.snake import Snake
from scripts.snake import SnakeBlock


class TestFood(TestCase):
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

    def test_collision_with_golden_apple(self):
        current_len = len(self.snake.blocks)
        current_score = self.snake.score
        GoldenApple.on_collision(Fruit, self.snake)
        self.assertEqual(len(self.snake.blocks), current_len + 1)
        self.assertEqual(self.snake.score, current_score + 1)

    def test_collision_with_bad_apple(self):
        current_len = len(self.snake.blocks)
        BadApple.on_collision(Fruit, self.snake)
        self.assertEqual(len(self.snake.blocks), current_len - 1)

    def test_collision_with_storm(self):
        current_len = len(self.snake.blocks)
        current_speed = self.snake.speed
        Storm.on_collision(Fruit, self.snake)
        self.assertEqual(len(self.snake.blocks), current_len + 1)
        self.assertEqual(self.snake.speed, current_speed + 2)

    def test_collision_with_bad_storm(self):
        current_speed = self.snake.speed
        BadStorm.on_collision(Fruit, self.snake)
        self.assertEqual(self.snake.speed, current_speed - 2)

    def test_collision_with_chest(self):
        current_score = self.snake.score
        Chest.on_collision(Fruit, self.snake)
        self.assertEqual(self.snake.score, current_score + 5)

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


if __name__ == "__main__":
    main()
