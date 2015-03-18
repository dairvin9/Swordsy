import pygame, sys
import math
from pygame.locals import *
from drawing_functions import *
pygame.init()


FPS = 30    # frames per second setting
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

ARENA_WIDTH = 800
ARENA_HEIGHT = 500

ARENA_RCx = (WINDOW_WIDTH-ARENA_WIDTH)/2 #Right corner of the arena (xvalue)
ARENA_RCy = (WINDOW_HEIGHT-ARENA_HEIGHT)/2 #Right corner of the arena (yvalue)

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 0)   # set up the window
pygame.display.set_caption('Animation')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
p1Img = pygame.image.load('crappysprite1.png')

length = 100
p1x = 10
p1y = 10

factory = math.sin(40)
factorx = math.cos(40)
line_width = 2

p1right = False
p1left = False
p1up = False
p1down = False

#pygame.key.set_repeat(0,500)
pygame.key.set_repeat(10,10)

while True:
# the main game loop

    DISPLAYSURF.fill(BLACK)
    #pygame.draw.rect(DISPLAYSURF, WHITE, (12,12,100,100))#THis works but is currently unwanted
    #draw_arena(DISPLAYSURF,WHITE,ARENA_WIDTH,ARENA_HEIGHT,ARENA_RCx,ARENA_RCy,factorx,factory,line_width)   #THE SECOND VARIABLE CAN BE ANY COLOR
    pygame.draw.line(DISPLAYSURF, WHITE, (ARENA_RCx, ARENA_RCy), (ARENA_RCx + ARENA_WIDTH, ARENA_RCy ), line_width) #TOP LINE
    pygame.draw.line(DISPLAYSURF, WHITE, (ARENA_RCx, ARENA_RCy + ARENA_HEIGHT), (ARENA_RCx + ARENA_WIDTH, ARENA_RCy + ARENA_HEIGHT ), line_width) #BOTTOM LINE
    pygame.draw.line(DISPLAYSURF, WHITE, (ARENA_RCx, ARENA_RCy), (ARENA_RCx , ARENA_RCy +ARENA_HEIGHT), line_width) #LEFT LINE
    pygame.draw.line(DISPLAYSURF, WHITE, (ARENA_RCx + ARENA_WIDTH, ARENA_RCy + ARENA_HEIGHT), (ARENA_RCx + ARENA_WIDTH, ARENA_RCy ), line_width) #RIGHT LINE
    
    pygame.draw.line(DISPLAYSURF, WHITE, (ARENA_RCx, ARENA_RCy), (ARENA_RCx + length*-factorx, ARENA_RCy + length*factory), line_width)      #UPPER LEFT DIAG
    pygame.draw.line(DISPLAYSURF, WHITE, (ARENA_RCx+ARENA_WIDTH, ARENA_RCy), (ARENA_RCx + ARENA_WIDTH + length*factorx, ARENA_RCy + length*factory), line_width) #UPPER RIGHT DIAG
    pygame.draw.line(DISPLAYSURF, WHITE, (ARENA_RCx, ARENA_RCy+ ARENA_HEIGHT), (ARENA_RCx + length*-factorx, ARENA_RCy + ARENA_HEIGHT+ length*-factory), line_width)#LOWER RIGHT DIAG
    pygame.draw.line(DISPLAYSURF, WHITE, (ARENA_RCx+ARENA_WIDTH, ARENA_RCy + ARENA_HEIGHT), (ARENA_RCx + ARENA_WIDTH + length*factorx, ARENA_RCy+ ARENA_HEIGHT + length*-factory), line_width)

    pygame.draw.line(DISPLAYSURF, WHITE, (ARENA_RCx + ARENA_WIDTH + length*factorx, ARENA_RCy + length*factory), (ARENA_RCx + length*-factorx, ARENA_RCy + length*factory), line_width)      #UPPER LEFT DIAG
    pygame.draw.line(DISPLAYSURF, WHITE, (ARENA_RCx + ARENA_WIDTH + length*factorx, ARENA_RCy+ ARENA_HEIGHT + length*-factory), (ARENA_RCx + ARENA_WIDTH + length*factorx, ARENA_RCy + length*factory), line_width) #UPPER RIGHT DIAG
    pygame.draw.line(DISPLAYSURF, WHITE, (ARENA_RCx + ARENA_WIDTH + length*factorx, ARENA_RCy+ ARENA_HEIGHT + length*-factory), (ARENA_RCx + length*-factorx, ARENA_RCy + ARENA_HEIGHT+ length*-factory), line_width)#LOWER RIGHT DIAG
    pygame.draw.line(DISPLAYSURF, WHITE, (ARENA_RCx + length*-factorx, ARENA_RCy + length*factory), (ARENA_RCx + length*-factorx, ARENA_RCy + ARENA_HEIGHT- length*factory), line_width)

    
     #pygame.draw.rect(DISPLAYSURF, WHITE, (ARENA_RCx + length*-factorx, ARENA_RCy + length*factory,ARENA_RCx + length*-factorx + ARENA_WIDTH, ARENA_RCy + length*factory))#Inner arena box
    
    #if direction = 8:

    DISPLAYSURF.blit(p1Img, (p1x, p1y))

    for event in pygame.event.get():

        #keyUpEvents= pygame.event.get(KEYUP)
        #if len(keyUpEvents) == 0:
         #    right = False
        if event.type == KEYDOWN:
            keys_pressed = pygame.key.get_pressed()
            if (event.key == K_d):#keys_pressed[K_d]:#(pygame.key.get_pressed()[pygame.K_d]):#(event.key == K_d)and(K_d.get_pressed()):
                p1right = True
                p1left = False
            if (event.key == K_a):
                p1left = True
                p1right = False

            if (event.key == K_w):
                p1up = True
                p1down = False

            if (event.key == K_s):
                p1down = True
                p1up = False    

        if event.type == QUIT:                          #Exits program
            pygame.quit()
            sys.exit()

        if p1right == True:
            p1x +=5
        if p1left == True:
            p1x -=5
        if p1down == True:
            p1y +=5
        if p1up == True:
            p1y -=5    
    p1up = False
    p1down = False
    p1left = False
    p1right = False
    pygame.display.update()
    fpsClock.tick(FPS)

