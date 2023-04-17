from constants import SIZE_BLOCK, MARGIN, HEADER_MARGIN, COUNT_BLOCKS, screen
import random
import pygame


class Food:
    def __init__(self):
        self.x = random.randint(1, COUNT_BLOCKS - 1)
        self.y = random.randint(1, COUNT_BLOCKS - 1)
        self.image = pygame.image.load("apple.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (SIZE_BLOCK, SIZE_BLOCK))

    def draw_food(self):
        screen.blit(self.image,
                    (SIZE_BLOCK + self.y * SIZE_BLOCK + MARGIN * (self.y + 1),
                     HEADER_MARGIN + SIZE_BLOCK + self.x * SIZE_BLOCK + MARGIN * (self.x + 1)))

    def check_collision(self, x, y):
        return self.x == x and self.y == y