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

    def test_create_bad_storm_when_speed_low(self):
        snake = Snake()
        snake.set_speed(5)
        food_manager = Food(snake)
        food_manager.create_new_food()
        for i in range(10):
            for food in food_manager.foods_list:
                self.assertTrue(food[2] != "bad_storm")

    def test_create_bad_storm_when_speed_high(self):
        snake = Snake()
        snake.set_speed(10)
        food_manager = Food(snake)
        food_manager.create_new_food()
        flag = False
        for i in range(10):
            for food in food_manager.foods_list:
                if food[2] == "bad_storm":
                    flag = True
        self.assertTrue(flag)

    def test_create_new_food(self):
        snake = self.snake
        snake.blocks.append(SnakeBlock(9, 9))
        snake.set_speed(3)
        food_manager = Food(snake)
        food_manager.create_new_food()
        available_foods = [food[2] for food in food_manager.foods_list]
        for bad_food_type in ["bad_apple", "bad_storm"]:
            self.assertNotIn(bad_food_type, available_foods)


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
