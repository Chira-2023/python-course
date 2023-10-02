# create a watch window

import pygame
import random
import time

# initialize pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Snake Game")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# Snake
snake_img = []
snake_x = []
snake_y = []
snake_x_change = []

snake_img.append(pygame.image.load('snake.png'))
snake_x.append(400)
snake_y.append(300)
snake_x_change.append(0)

# Food
food_img = pygame.image.load('food.png')
food_x = random.randint(0, 800)
food_y = random.randint(0, 600)

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def snake(x, y, i):
    screen.blit(snake_img[i], (x, y))

# Game Loop
running = True
while running:
    
        # RGB - Red, Green, Blue
        screen.fill((0, 0, 0))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change[0] = -0.1
                if event.key == pygame.K_RIGHT:
                    snake_x_change[0] = 0.1
    
        snake_x[0] += snake_x_change[0]
    
        if snake_x[0] <= 0:
            snake_x[0] = 800
        elif snake_x[0] >= 800:
            snake_x[0] = 0
    
        # Collision
        if snake_x[0] == food_x and snake_y[0] == food_y:
            score_value += 1
            food_x = random.randint(0, 800)
            food_y = random.randint(0, 600)
    
        snake(snake_x[0], snake_y[0], 0)
        snake(snake_x[1], snake_y[1], 1)
        snake(snake_x[2], snake_y[2], 2)
        snake(snake_x[3], snake_y[3], 3)
        snake(snake_x[4], snake_y[4], 4)
        snake(snake_x[5], snake_y[5], 5)
        snake(snake_x[6], snake_y[6], 6)
        snake(snake_x[7], snake_y[7], 7)
        snake(snake_x[8], snake_y[8], 8)
        snake(snake_x[9], snake_y[9], 9)
    
        show_score(text_x, text_y)
    
        pygame.display.update()

# Path: snake_game.py
# create a watch window
