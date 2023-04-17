from constants import COUNT_BLOCKS


class Direction:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS


class Snake:
    def __init__(self):
        self.blocks = [SnakeBlock(9, 9)]
        self.score = 0

    def add_score(self):
        self.score += 1

