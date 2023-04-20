from constants import SIZE_BLOCK, MARGIN, HEADER_MARGIN, COUNT_BLOCKS, SCREEN
import random
import pygame
import os

food_images_path = os.path.join(r"C:\Users\79521\PycharmProjects\Snake\FoodImages")


class Food:
    foods_list = []

    def __init__(self, snake):
        self.snake = snake
        self.foods = {
            'bad_apple': pygame.transform.scale(
                pygame.image.load(os.path.join(food_images_path, "badApple.png")).convert_alpha(),
                (SIZE_BLOCK, SIZE_BLOCK)),
            'golden_apple': pygame.transform.scale(
                pygame.image.load(os.path.join(food_images_path, "goldenApple.png")).convert_alpha(),
                (SIZE_BLOCK, SIZE_BLOCK)),
            'storm': pygame.transform.scale(
                pygame.image.load(os.path.join(food_images_path, "storm.png")).convert_alpha(),
                (SIZE_BLOCK, SIZE_BLOCK)),
            'chest': pygame.transform.scale(
                pygame.image.load(os.path.join(food_images_path, "chest.png")).convert_alpha(),
                (SIZE_BLOCK, SIZE_BLOCK)),
            'bad_storm': pygame.transform.scale(
                pygame.image.load(os.path.join(food_images_path, "badStorm.png")).convert_alpha(),
                (SIZE_BLOCK, SIZE_BLOCK))
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
            self.foods_list.append((x, y, random.choice([key for key in self.foods.keys() if key != item])))

    def draw_food(self):
        for food in self.foods_list:
            x, y, item = food
            SCREEN.blit(self.foods[item],
                        (SIZE_BLOCK + y * SIZE_BLOCK + MARGIN * (y + 1),
                         HEADER_MARGIN + SIZE_BLOCK + x * SIZE_BLOCK + MARGIN * (x + 1)))

    def check_collision(self, x, y):
        for food in self.foods_list:
            fx, fy, item = food
            if fx == x and fy == y:
                if item == 'bad_apple':
                    self.snake.reduce_length()
                elif item == 'golden_apple':
                    self.snake.score += 1
                    self.snake.increase_length()
                elif item == 'storm':
                    self.snake.set_speed(2)
                    self.snake.increase_length()
                elif item == 'bad_storm':
                    self.snake.set_speed(-2)
                elif item == 'chest':
                    self.snake.score += 5
                    self.snake.increase_length()
                self.foods_list.remove(food)
                self.create_new_food()
                return True
        return False

    def create_new_food(self):
        while len(self.foods_list) < 3:
            x = random.randint(1, COUNT_BLOCKS - 1)
            y = random.randint(1, COUNT_BLOCKS - 1)
            if len(self.snake.blocks) == 1:
                item = "bad_apple"
            elif self.snake.speed <= 5:
                item = "bad_storm"
            else:
                item = None
            self.foods_list.append((x, y, random.choice([key for key in self.foods.keys() if key != item])))
