from constants import SIZE_BLOCK, MARGIN, HEADER_MARGIN, COUNT_BLOCKS, screen
import random
import pygame


class Food:
    foods = []

    def __init__(self, snake):
        self.snake = snake
        self.bad_apple = pygame.image.load("badApple.png").convert_alpha()
        self.golden_apple = pygame.image.load("goldenApple.png").convert_alpha()
        self.storm = pygame.image.load("storm.png").convert_alpha()
        self.chest = pygame.image.load("chest.png").convert_alpha()
        self.bad_storm = pygame.image.load("badStorm.png").convert_alpha()
        self.x = random.randint(1, COUNT_BLOCKS - 1)
        self.y = random.randint(1, COUNT_BLOCKS - 1)
        self.bad_apple = pygame.transform.scale(self.bad_apple, (SIZE_BLOCK, SIZE_BLOCK))
        self.golden_apple = pygame.transform.scale(self.golden_apple, (SIZE_BLOCK, SIZE_BLOCK))
        self.storm = pygame.transform.scale(self.storm, (SIZE_BLOCK, SIZE_BLOCK))
        self.chest = pygame.transform.scale(self.chest, (SIZE_BLOCK, SIZE_BLOCK))
        self.bad_storm = pygame.transform.scale(self.bad_storm, (SIZE_BLOCK, SIZE_BLOCK))
        self.item = random.choice([self.bad_apple, self.golden_apple, self.storm, self.chest, self.bad_storm])
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
                    self.snake.add_score(1)
                elif food.item == self.bad_apple:
                    self.snake.add_score(1)
                elif food.item == self.storm:
                    self.snake.set_speed(2)
                elif food.item == self.bad_storm:
                    self.snake.set_speed(-2)
                elif food.item == self.chest:
                    self.snake.add_score(10)
                self.foods.remove(food)
                self.create_new_food()
                return 1
        return 0

    def create_new_food(self):
        self.x = random.randint(1, COUNT_BLOCKS - 1)
        self.y = random.randint(1, COUNT_BLOCKS - 1)
        self.item = random.choice([self.bad_apple, self.golden_apple, self.storm, self.chest, self.bad_storm])
        self.foods.append(self)
