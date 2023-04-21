from constants import COUNT_BLOCKS


class Direction:
    UP = [-1, 0]
    DOWN = [1, 0]
    LEFT = [0, -1]
    RIGHT = [0, 1]


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
        self.speed = 5
        self.direction = [0, 0]
        self.lives = 3
        self.should_reduce_len = False

    def add_score(self, score_value):
        self.score += score_value

    def set_speed(self, added_speed):
        self.speed += added_speed

    def increase_length(self):
        self.blocks.append(SnakeBlock(self.blocks[-1].x, self.blocks[-1].y))

    def reduce_length(self):
        self.blocks.pop(0)
