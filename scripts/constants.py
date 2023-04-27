import pygame
import os
file_path = os.path.abspath(__file__)

FOOD_IMAGE_PATH = os.path.abspath(os.path.join(os.path.dirname(file_path), '..', 'FoodImages'))
SIZE_BLOCK = 20
FRAME_COLOR = (42, 128, 100)
HEADER_COLOR = (0, 204, 153)
SNAKE_COLOR = (177, 86, 15)
BACKGROUND_COLOR = (111, 232, 220)
BLACK = (0, 0, 0)
COUNT_BLOCKS = 20
HEADER_MARGIN = 70
MARGIN = 1
SIZE = [SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * SIZE_BLOCK + HEADER_MARGIN]
SCREEN = pygame.display.set_mode(SIZE)