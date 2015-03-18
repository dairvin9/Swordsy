import pygame, sys
import math
from pygame.locals import *

class Player(object):
    right = False
    left = False
    up = False
    down = False

    x = 10
    y = 10

    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def set_false(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        return

def handle_movements(self):
    if self.right == True:
        self.x +=5
    if self.left == True:
        self.x -=5
    if self.down == True:
        self.y +=5
    if self.up == True:
        self.y -=5
    return    

    
def handle_keys_p1(event, p1):
    if (event.key == K_d):#keys_pressed[K_d]:#(pygame.key.get_pressed()[pygame.K_d]):#(event.key == K_d)and(K_d.get_pressed()):
        p1.right = True
        p1.left = False
    if (event.key == K_a):
        p1.left = True
        p1.right = False

    if (event.key == K_w):
        p1.up = True
        p1.down = False
        
    if (event.key == K_s):
        p1.down = True
        p1.up = False    
    return

def handle_keys_p2(event, p2):
    if (event.key == K_RIGHT):
        p2.right = True
        p2.left = False
    if (event.key == K_LEFT):
        p2.left = True
        p2.right = False

    if (event.key == K_UP):
        p2.up = True
        p2.down = False
        
    if (event.key == K_DOWN):
        p2.down = True
        p2.up = False    
    return
