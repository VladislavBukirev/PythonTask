from constants import SIZE_BLOCK, MARGIN, HEADER_MARGIN, COUNT_BLOCKS, screen
from snake import Snake
import random
import pygame


class Food:
    foods = []

    def __init__(self, snake):
        self.x = random.randint(1, COUNT_BLOCKS - 1)
        self.y = random.randint(1, COUNT_BLOCKS - 1)
        self.apple = pygame.image.load("apple.png").convert_alpha()
        self.apple = pygame.transform.scale(self.apple, (SIZE_BLOCK, SIZE_BLOCK))
        self.golden_apple = pygame.image.load("goldenApple.png").convert_alpha()
        self.golden_apple = pygame.transform.scale(self.golden_apple, (SIZE_BLOCK, SIZE_BLOCK))
        self.item = random.choice([self.apple, self.golden_apple])
        self.snake = snake
        self.foods.append(self)

    def draw_food(self):
        for food in self.foods:
            screen.blit(food.item,
                        (SIZE_BLOCK + food.y * SIZE_BLOCK + MARGIN * (food.y + 1),
                         HEADER_MARGIN + SIZE_BLOCK + food.x * SIZE_BLOCK + MARGIN * (food.x + 1)))

    def check_collision(self, x, y):
        for food in self.foods:
            if food.x == x and food.y == y:
                if food.item == self.golden_apple:
                    self.snake.add_score(3)
                else:
                    self.snake.add_score(1)
                self.foods.remove(food)
                self.create_new_food()
                return 1
        return 0

    def create_new_food(self):
        self.x = random.randint(1, COUNT_BLOCKS - 1)
        self.y = random.randint(1, COUNT_BLOCKS - 1)
        self.item = random.choice([self.apple, self.golden_apple])
        self.foods.append(self)
