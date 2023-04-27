
import pygame
from constants \
    import SIZE_BLOCK, MARGIN, HEADER_MARGIN, COUNT_BLOCKS,\
    FRAME_COLOR, HEADER_COLOR, BACKGROUND_COLOR, BLACK, SCREEN, SIZE


def draw_block(color, row, column):
    pygame.draw.rect(SCREEN, color,
                     [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                      HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                      SIZE_BLOCK, SIZE_BLOCK])


class Levels:
    def __init__(self, number, length, obstacles=None):
        self.number = number
        self.length = length
        self.obstacles = obstacles or []

    def draw_level(self):
        SCREEN.fill(FRAME_COLOR)
        pygame.draw.rect(SCREEN, HEADER_COLOR, [0, 0, SIZE[0], HEADER_MARGIN])

        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):
                if (row, column) in self.obstacles:
                    draw_block(BLACK, row, column)
                else:
                    draw_block(BACKGROUND_COLOR, row, column)
