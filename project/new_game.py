#  write a code in python that creat a Tik tak toe game

import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

bright_red = (200,0,0)
bright_green = (0,200,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Tik Tak Toe')

clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def game_intro():
    
        intro = True
    
        while intro:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
            gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf',115)
            TextSurf, TextRect = text_objects("Tik Tak Toe", largeText)
            TextRect.center = ((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
    
            button("GO!",150,450,100,50,green,bright_green,game_loop)
            button("Quit",550,450,100,50,red,bright_red,quitgame)
    
            pygame.display.update()
            clock.tick(15)

def game_loop():
    gameExit = False
    gameOver = False

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_display('Game over')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True

        gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()

