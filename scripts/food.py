from scripts.constants import SIZE_BLOCK, MARGIN, HEADER_MARGIN, COUNT_BLOCKS, SCREEN
from scripts.constants import FOOD_IMAGE_PATH
import random
import pygame
import os.path
import pygame.mixer as mixer


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
        self.occupied_coords = []

        for i in range(3):
            x, y = self.generate_new_coord()
            item = None
            if len(self.snake.blocks) <= 3:
                item = "bad_apple"
            elif self.snake.speed <= 5:
                item = "bad_storm"
            self.foods_list.append((x, y, random.choice([key for key in self.foods if key != item])))
            self.occupied_coords.append((x, y))

        mixer.init()
        self.eat_sound = pygame.mixer.Sound("musicForEatingFruit.mp3")

    def generate_new_coord(self):
        while True:
            x = random.randint(1, COUNT_BLOCKS - 1)
            y = random.randint(1, COUNT_BLOCKS - 1)
            if (x, y) not in self.occupied_coords:
                return x, y

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
                self.eat_sound.play()
                return True
        return False

    def create_new_food(self):
        available_foods = list(self.foods.keys())
        if len(self.snake.blocks) <= 3:
            available_foods.remove("bad_apple")
        elif self.snake.speed <= 5:
            available_foods = [t for t in available_foods if t != "bad_storm"]
        while len(self.foods_list) < 3:
            x, y = self.generate_new_coord()
            item = random.choice(available_foods)
            self.foods_list.append((x, y, item))
            self.occupied_coords.append((x, y))
