from constants import SIZE_BLOCK, MARGIN, HEADER_MARGIN, COUNT_BLOCKS, SCREEN
from constants import FOOD_IMAGE_PATH
import random
import pygame
import os.path


class Fruit:
    def __init__(self, image_path):
        self.image = pygame.transform.scale(
            pygame.image.load(image_path).convert_alpha(),
            (SIZE_BLOCK, SIZE_BLOCK))

    def on_collision(self, snake):
        pass


class GoldenApple(Fruit):
    def __init__(self):
        super().__init__(os.path.join(FOOD_IMAGE_PATH, "goldenApple.png"))

    def on_collision(self, snake):
        snake.score += 1
        snake.increase_length()


class BadApple(Fruit):
    def __init__(self):
        super().__init__(os.path.join(FOOD_IMAGE_PATH, "badApple.png"))

    def on_collision(self, snake):
        snake.reduce_length()


class Storm(Fruit):
    def __init__(self):
        super().__init__(os.path.join(FOOD_IMAGE_PATH, "storm.png"))

    def on_collision(self, snake):
        snake.set_speed(2)
        snake.increase_length()


class BadStorm(Fruit):
    def __init__(self):
        super().__init__(os.path.join(FOOD_IMAGE_PATH, "badStorm.png"))

    def on_collision(self, snake):
        snake.set_speed(-2)


class Chest(Fruit):
    def __init__(self):
        super().__init__(os.path.join(FOOD_IMAGE_PATH, "chest.png"))

    def on_collision(self, snake):
        snake.add_score(5)
        snake.increase_length()


class Food:
    foods_list = []

    def __init__(self, snake):
        self.snake = snake
        self.foods = {
            'golden_apple': GoldenApple(),
            'bad_apple': BadApple(),
            'storm': Storm(),
            'bad_storm': BadStorm(),
            'chest': Chest(),
        }
        self.foods_list = []
        for i in range(3):
            x = random.randint(1, COUNT_BLOCKS - 1)
            y = random.randint(1, COUNT_BLOCKS - 1)
            if len(self.snake.blocks) <= 3:
                item = "bad_apple"
            elif self.snake.speed <= 5:
                item = "bad_storm"
            else:
                item = None
            self.foods_list.append((x, y, random.choice([key for key in self.foods if key != item])))

    def draw_food(self):
        for food in self.foods_list:
            x, y, item = food
            SCREEN.blit(self.foods[item].image,
                        (SIZE_BLOCK + y * SIZE_BLOCK + MARGIN * (y + 1),
                         HEADER_MARGIN + SIZE_BLOCK + x * SIZE_BLOCK + MARGIN * (x + 1)))

    def check_collision(self, x, y):
        for food in self.foods_list:
            fx, fy, item = food
            if fx == x and fy == y:
                self.foods[item].on_collision(self.snake)
                self.foods_list.remove(food)
                self.create_new_food()
                return True
        return False

    def create_new_food(self):
        while len(self.foods_list) < 3:
            x = random.randint(1, COUNT_BLOCKS - 1)
            y = random.randint(1, COUNT_BLOCKS - 1)
            if len(self.snake.blocks) <= 3:
                item = "bad_apple"
            elif self.snake.speed <= 5:
                item = "bad_storm"
            else:
                item = None
            self.foods_list.append((x, y, random.choice([key for key in self.foods if key != item])))
