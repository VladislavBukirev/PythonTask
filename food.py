from constants import SIZE_BLOCK, MARGIN, HEADER_MARGIN, COUNT_BLOCKS, screen
import random
import pygame


class Food:
    def __init__(self):
        self.x = random.randint(1, COUNT_BLOCKS - 1)
        self.y = random.randint(1, COUNT_BLOCKS - 1)
        self.apple = pygame.image.load("apple.png").convert_alpha()
        self.apple = pygame.transform.scale(self.apple, (SIZE_BLOCK, SIZE_BLOCK))
        self.golden_apple = pygame.image.load("goldenApple.png").convert_alpha()
        self.golden_apple = pygame.transform.scale(self.golden_apple, (SIZE_BLOCK, SIZE_BLOCK))
        self.item = random.choice([self.apple, self.golden_apple])

    def draw_food(self):
        screen.blit(self.item,
                    (SIZE_BLOCK + self.y * SIZE_BLOCK + MARGIN * (self.y + 1),
                     HEADER_MARGIN + SIZE_BLOCK + self.x * SIZE_BLOCK + MARGIN * (self.x + 1)))

    def check_collision(self, x, y):
        if self.x == x and self.y == y:
            if self.item == self.golden_apple:
                return 2
            else:
                return 1
        return 0
