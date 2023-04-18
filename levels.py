
import pygame
from constants import SIZE_BLOCK, MARGIN, HEADER_MARGIN, COUNT_BLOCKS, FRAME_COLOR, HEADER_COLOR, SNAKE_COLOR, BACKGROUND_COLOR, BLACK, screen, size


def draw_block(color, row, column):
    pygame.draw.rect(screen, color,
                     [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                      HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                      SIZE_BLOCK, SIZE_BLOCK])


def draw_map():
    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            draw_block(BACKGROUND_COLOR, row, column)


class Levels:
    def __init__(self, number, length):
        self.number = number
        self.length = length

