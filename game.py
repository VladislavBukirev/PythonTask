import pygame
import sys

from constants import SIZE_BLOCK, MARGIN, HEADER_MARGIN, COUNT_BLOCKS, FRAME_COLOR, HEADER_COLOR, SNAKE_COLOR, BACKGROUND_COLOR, BLACK, screen, size
from snake import Snake
from food import Food
from snake import Direction
from snake import SnakeBlock


def draw_block(color, row, column):
    pygame.draw.rect(screen, color,
                     [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                      HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                      SIZE_BLOCK, SIZE_BLOCK])


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.timer = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food(self.snake)
        self.heart_image = pygame.image.load('heart.png').convert_alpha()
        self.heart_image = pygame.transform.scale(self.heart_image,
                                                  (20, 20))
        self.heart_rect = self.heart_image.get_rect()
        self.heart_rect.topright = (size[0] - 10, 10)


    def process_movement_key(self, event):
        if event.key == pygame.K_UP:
            self.snake.direction = Direction.UP
        elif event.key == pygame.K_DOWN:
            self.snake.direction = Direction.DOWN
        elif event.key == pygame.K_RIGHT:
            self.snake.direction = Direction.RIGHT
        elif event.key == pygame.K_LEFT:
            self.snake.direction = Direction.LEFT

    def draw_scores_table(self):
        font_score = pygame.font.SysFont('Times New Roman', 32)
        text_score = font_score.render(f'Score: {self.snake.score}', True, BLACK)
        score_rect = text_score.get_rect()
        score_rect.center = (size[0] // 2, 30)
        screen.blit(text_score, score_rect.topleft)

        for i in range(self.snake.lives):
            screen.blit(self.heart_image,
                        (self.heart_rect.right - (i + 1) * self.heart_rect.width, self.heart_rect.top))

    def draw_map(self):
        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):
                draw_block(BACKGROUND_COLOR, row, column)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.process_movement_key(event)

            self.draw_map()

            head = self.snake.blocks[-1]

            for block in self.snake.blocks:
                draw_block(SNAKE_COLOR, block.x, block.y)

            self.food.draw_food()
            if self.food.check_collision(self.snake.blocks[-1].x, self.snake.blocks[-1].y):
                self.snake.blocks.append(SnakeBlock(self.snake.blocks[-1].x, self.snake.blocks[-1].y))

            new_head = SnakeBlock(head.x + self.snake.direction[0], head.y + self.snake.direction[1])
            if not new_head.is_inside() or any(
                    block != head and block.x == new_head.x and block.y == new_head.y for block in self.snake.blocks):
                self.snake.lives -= 1
                if self.snake.lives == 0:
                    pygame.quit()
                    sys.exit()
            self.snake.blocks.append(new_head)
            self.snake.blocks.pop(0)

            self.draw_scores_table()
            pygame.display.flip()
            self.timer.tick(self.snake.speed)

