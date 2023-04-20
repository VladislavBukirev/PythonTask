import pygame
import sys
import os

from constants import SIZE_BLOCK, MARGIN, HEADER_MARGIN, COUNT_BLOCKS, FRAME_COLOR, HEADER_COLOR, SNAKE_COLOR, BACKGROUND_COLOR, BLACK, SCREEN, SIZE
from snake import Snake
from food import Food
from snake import Direction
from snake import SnakeBlock
from levels import Levels


def draw_block(color, row, column):
    pygame.draw.rect(SCREEN, color,
                     [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                      HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                      SIZE_BLOCK, SIZE_BLOCK])


level1 = Levels(1, 5)
level2 = Levels(2, 10, obstacles=[(2, 2), (2, 3), (2, 4), (2, 5)])
level3 = Levels(3, 15, obstacles=[(2, 2), (2, 3), (2, 4), (2, 5), (15, 12), (15, 13), (15, 14), (15, 15)])
Levels_list = [level1, level2, level3]


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.timer = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food(self.snake)
        self.level = level1

    def draw_lives(self):
        path_to_image = os.path.join(r"C:\Users\79521\PycharmProjects\Snake\FoodImages")
        heart_image = pygame.transform.scale(
                pygame.image.load(os.path.join(path_to_image, "heart.png")).convert_alpha(),
                (20, 20))
        heart_rect = heart_image.get_rect()
        heart_rect.topleft = (50, 10)
        for i in range(self.snake.lives):
            SCREEN.blit(heart_image,
                        (heart_rect.right - (i + 1) * heart_rect.width, heart_rect.top))

    def process_movement_key(self, event):
        if event.key == pygame.K_UP and self.snake.direction != Direction.DOWN:
            self.snake.direction = Direction.UP
        elif event.key == pygame.K_DOWN and self.snake.direction != Direction.UP:
            self.snake.direction = Direction.DOWN
        elif event.key == pygame.K_RIGHT and self.snake.direction != Direction.LEFT:
            self.snake.direction = Direction.RIGHT
        elif event.key == pygame.K_LEFT and self.snake.direction != Direction.RIGHT:
            self.snake.direction = Direction.LEFT

    def draw_scores_table(self):
        font_score = pygame.font.SysFont('Times New Roman', 32)
        text_score = font_score.render(f'Score: {self.snake.score}', True, BLACK)
        score_rect = text_score.get_rect()
        score_rect.center = (SIZE[0] // 2, 30)
        SCREEN.blit(text_score, score_rect.topleft)

    def draw_snake_length(self):
        printed_length = pygame.font.SysFont("Times New Roman", 16)
        text_length = printed_length.render(f'Length: {len(self.snake.blocks)}', True, BLACK)
        len_rect = text_length.get_rect()
        len_rect.bottomright = (SIZE[0] - 10, HEADER_MARGIN - 5)
        SCREEN.blit(text_length, len_rect)

    def check_collision(self):
        head = self.snake.blocks[-1]
        new_head = SnakeBlock(head.x + self.snake.direction[0], head.y + self.snake.direction[1])
        if any(new_head.x == block[0] and new_head.y == block[1] for block in self.level.obstacles) or \
                not new_head.is_inside() or \
                any(block != head and block.x == new_head.x and block.y == new_head.y for block in self.snake.blocks):
            self.snake.lives -= 1
            if self.snake.lives == 0:
                pygame.quit()
                sys.exit()

    def draw_level(self):
        font_level = pygame.font.SysFont('Times New Roman', 16)
        font_condition = pygame.font.SysFont('Times New Roman', 16)
        text_level = font_level.render(f'Level: {self.level.number}', True, BLACK)
        text_condition = font_condition.render(f'Condition for next level: {self.level.length}', True, BLACK)
        level_rect = text_level.get_rect()
        condition_rect = text_condition.get_rect()
        level_rect.center = (40, 20)
        condition_rect.center = (95, 40)
        SCREEN.blit(text_level, level_rect.bottomleft)
        SCREEN.blit(text_condition, condition_rect.bottomleft)

    def switch_level(self):
        index = Levels_list.index(self.level)
        if index < len(Levels_list) - 1:
            self.level = Levels_list[index + 1]
        else:
            pygame.quit()
            sys.exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.process_movement_key(event)

            self.level.draw_level()

            head = self.snake.blocks[-1]
            new_head = SnakeBlock(head.x + self.snake.direction[0], head.y + self.snake.direction[1])

            for block in self.snake.blocks:
                draw_block(SNAKE_COLOR, block.x, block.y)

            self.check_collision()
            self.food.draw_food()

            self.food.check_collision(self.snake.blocks[-1].x, self.snake.blocks[-1].y)

            self.snake.blocks.append(new_head)
            self.snake.reduce_length()

            if len(self.snake.blocks) == self.level.length:
                self.switch_level()

            self.draw_level()
            self.draw_lives()
            self.draw_scores_table()
            self.draw_snake_length()
            pygame.display.flip()
            self.timer.tick(self.snake.speed)
