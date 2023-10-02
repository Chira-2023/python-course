import pygame
import random

# initialize pygame
pygame.init()

# define game constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
SNAKE_SIZE = 10
APPLE_SIZE = 10
FONT_SIZE = 30
FPS = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# create game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# define game objects
class Snake:
    def __init__(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.dx = SNAKE_SIZE
        self.dy = 0
        self.length = 1
        self.body = [(self.x, self.y)]

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.body.insert(0, (self.x, self.y))
        if len(self.body) > self.length:
            self.body.pop()

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(window, GREEN, (x, y, SNAKE_SIZE, SNAKE_SIZE))

    def move_left(self):
        self.dx = -SNAKE_SIZE
        self.dy = 0

    def move_right(self):
        self.dx = SNAKE_SIZE
        self.dy = 0

    def move_up(self):
        self.dx = 0
        self.dy = -SNAKE_SIZE

    def move_down(self):
        self.dx = 0
        self.dy = SNAKE_SIZE

    def eat(self, apple):
        if self.x == apple.x and self.y == apple.y:
            self.length += 1
            return True
        return False

class Apple:
    def __init__(self):
        self.x = random.randint(0, WINDOW_WIDTH - APPLE_SIZE)
        self.y = random.randint(0, WINDOW_HEIGHT - APPLE_SIZE)

    def draw(self):
        pygame.draw.rect(window, RED, (self.x, self.y, APPLE_SIZE, APPLE_SIZE))

# define game functions
def draw_score(score):
    font = pygame.font.SysFont(None, FONT_SIZE)
    text = font.render(f"Score: {score}", True, WHITE)
    window.blit(text, (10, 10))

def draw_game_over():
    font = pygame.font.SysFont(None, FONT_SIZE)
    text = font.render("Game Over!", True, WHITE)
    window.blit(text, (WINDOW_WIDTH // 2 - FONT_SIZE, WINDOW_HEIGHT // 2 - FONT_SIZE))

def game_loop():
    # create game objects
    snake = Snake()
    apple = Apple()
    score = 0

    # game loop
    running = True
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.move_left()
                elif event.key == pygame.K_RIGHT:
                    snake.move_right()
                elif event.key == pygame.K_UP:
                    snake.move_up()
                elif event.key == pygame.K_DOWN:
                    snake.move_down()
