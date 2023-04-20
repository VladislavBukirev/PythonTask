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
        self.x = random.randint(1, COUNT_BLOCKS - 1)
        self.y = random.randint(1, COUNT_BLOCKS - 1)
        self.item = random.choice(list(self.foods.keys()))
        self.foods_list.append(self)

    def draw_food(self):
        SCREEN.blit(self.foods[self.item],
                    (SIZE_BLOCK + self.y * SIZE_BLOCK + MARGIN * (self.y + 1),
                     HEADER_MARGIN + SIZE_BLOCK + self.x * SIZE_BLOCK + MARGIN * (self.x + 1)))

    def check_collision(self, x, y):
        if self.x == x and self.y == y:
            if self.item == 'bad_apple':
                self.snake.reduce_length()
                self.snake.reduce_length()
            elif self.item == 'golden_apple':
                self.snake.score += 1
            elif self.item == 'storm':
                self.snake.set_speed(2)
            elif self.item == 'bad_storm':
                self.snake.set_speed(-2)
            elif self.item == 'chest':
                self.snake.score += 5
            self.create_new_food()
            return True
        return False

    def create_new_food(self):
        self.x = random.randint(1, COUNT_BLOCKS - 1)
        self.y = random.randint(1, COUNT_BLOCKS - 1)
        self.item = random.choice(list(self.foods.keys()))
        self.foods_list.append(self)
