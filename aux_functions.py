import pygame, sys
import math
from pygame.locals import *

class Player(object):
    right = False
    left = False
    up = False
    down = False

    extended = 0
    frozen = 0

    image = "none"
    
    x = 10
    y = 10

    sharp = {}
    vul = {}

    lose = False
    
    
    #vulnerable = {n:{},nl:{},e{},el{}} #E is for extended, n is for normal
    
    
    def __init__(self, x, y,str):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.x = x
        self.y = y
        self.image = str
        #   self.mask = pygame.mask.from_surface(self.img)

   # def get_intersections:
        

    def set_regions(self,attacker):
        self.sharp = {'n':Rect(self.x + 82,self.y + 2,96-82,15-2),'nl':Rect(self.x + 21,self.y + 2, 31- 21, 17- 2),'e':Rect(self.x + 111-30,self.y + 20, 125 - 111,31 - 20),'el':Rect(self.x + 8,self.y + 19,18 - 8,34-19)} #E is for eself.xtended, n is for normal
        self.vul = {'nh':Rect(self.x + 25,self.y + 6,52-25,33-6),'nlh':Rect(66+self.x,5+self.y,93-66,32-5),'eh':Rect(28+self.x,4+self.y,54-28,30-4),'elh':Rect(self.x + 65 - 30,self.y+5,93-65,33-5)}
        attacker.sharp = {'n':Rect(attacker.x + 82,attacker.y + 2,96-82,15-2),'nl':Rect(attacker.x + 21,attacker.y + 2, 31- 21, 17- 2),'e':Rect(attacker.x + 111-30,attacker.y + 20, 125 - 111,31 - 20),'el':Rect(attacker.x + 8,attacker.y + 19,18 - 8,34-19)} #E is for eattacker.xtended, n is for normal
        attacker.vul = {'nh':Rect(attacker.x + 25,attacker.y + 6,52-25,33-6),'nlh':Rect(66+attacker.x,5+attacker.y,93-66,32-5),'eh':Rect(28+attacker.x,4+attacker.y,54-28,30-4),'elh':Rect(attacker.x + 65 - 30,attacker.y+5,93-65,33-5)}
       #sharp = {'n':(x + 82,y + 2,96-82,15-2),'nl':(x + 21,y + 2, 31- 21, 17- 2),'e':(x + 111-30,y + 20, 125 - 111,31 - 20),'el':(x + 8,y + 19,18 - 8,34-19)} #E is for extended, n is for normal
       #vul = {'nh':(x + 25,y + 6,52-25,33-6),'nlh':(66+x,5+y,93-66,32-5),'eh':(28+x,4+y,54-28,30-4),'elh':(x + 65 - 30,y+5,93-65,33-5)}
        
        #if (self.extended != 0):
         #      if (p2.sharp['n']).collide(vul['n']):
          #          print("Collision!")
        if   (self.extended != 0) and (attacker.extended != 0) and (self.right)  and (attacker.right):
            print("possible")
            if (attacker.sharp['e']).colliderect(self.vul['eh']):
                self.lose = True
        elif (self.extended != 0) and (attacker.extended != 0) and (self.right)  and (attacker.right == False):
            if (attacker.sharp['el']).colliderect(self.vul['eh']):
                self.lose = True
        elif (self.extended != 0) and (attacker.extended != 0) and not(self.right) and (attacker.right):
            if (attacker.sharp['e']).colliderect(self.vul['elh']):
                self.lose = True
        elif (self.extended != 0) and (attacker.extended != 0) and not(self.right) and not(attacker.right):
            if (attacker.sharp['el']).colliderect(self.vul['elh']):
                self.lose = True
        elif (self.extended != 0) and (attacker.extended == 0) and (self.right)  and (attacker.right):
            if (attacker.sharp['n']).colliderect(self.vul['eh']):
                self.lose = True
        elif (self.extended != 0) and (attacker.extended == 0) and (self.right)  and not(attacker.right):
            if (attacker.sharp['n']).colliderect(self.vul['eh']):
                self.lose = True
        elif (self.extended != 0) and (attacker.extended == 0) and not(self.right) and (attacker.right):
            if (attacker.sharp['n']).colliderect(self.vul['elh']):
                self.lose = True
        elif (self.extended != 0) and (attacker.extended == 0) and not(self.right) and not(attacker.right):
            if (attacker.sharp['el']).colliderect(self.vul['elh']):
                self.lose = True
        elif (self.extended == 0) and (attacker.extended != 0) and (self.right)  and (attacker.right):
            if (attacker.sharp['e']).colliderect(self.vul['nh']):
                self.lose = True
        elif (self.extended == 0) and (attacker.extended != 0) and (self.right)  and not(attacker.right):
            if (attacker.sharp['el']).colliderect(self.vul['nh']):
                self.lose = True
        elif (self.extended == 0) and (attacker.extended != 0) and not(self.right) and (attacker.right):
            if (attacker.sharp['e']).colliderect(self.vul['nlh']):
                self.lose = True
        elif (self.extended == 0) and (attacker.extended != 0) and not(self.right) and not(attacker.right):
            if (attacker.sharp['el']).colliderect(self.vul['nlh']):
                self.lose = True
        elif (self.extended == 0) and (attacker.extended == 0) and (self.right)  and (attacker.right):
            if (attacker.sharp['n']).colliderect(self.vul['nh']):
                self.lose = True
        elif (self.extended == 0) and (attacker.extended == 0) and (self.right)  and not(attacker.right):
            if (attacker.sharp['nl']).colliderect(self.vul['nh']):
                self.lose = True
        elif (self.extended == 0) and (attacker.extended == 0) and not(self.right) and (attacker.right):
            if (attacker.sharp['n']).colliderect(self.vul['nlh']):
                self.lose = True
        elif (self.extended == 0) and (attacker.extended == 0) and not(self.right) and not(attacker.right):
            if (attacker.sharp['nl']).colliderect(self.vul['nlh']):
                self.lose = True
        return
                
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

def handle_keys(p1, p2,innertlx,innertly,innertrx,innerlly,SPRITE_WIDTH,SPRITE_HEIGHT):
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]and p2.x >= innertlx:
        p2.left = True
        p2.right = False
        p2.image = "left"
        
    if keys[K_RIGHT] and p2.x <= innertrx - SPRITE_WIDTH+15:
        p2.right = True
        p2.left = False
        p2.image = "right"
        
    if keys[K_UP] and p2.y >= innertly:
        p2.up = True
        p2.down = False

    if keys[K_DOWN] and p2.y <= innerlly - SPRITE_HEIGHT:
        p2.down = True
        p2.up = False 

    if keys[K_a]and p1.x >= innertlx:
        p1.left = True
        p1.right = False
        p1.image = "left"

    if keys[K_d] and p1.x <= innertrx - SPRITE_WIDTH+15:
        p1.right = True
        p1.left = False
        p1.image = "right"

    if keys[K_w]and p1.y >= innertly:
        p1.up = True
        p1.down = False

    if keys[K_s] and p2.y <= innerlly - SPRITE_HEIGHT:
        p1.down = True
        p1.up = False

    if keys[K_RSHIFT]:
        p2.extended = 7
        
        

    if keys[K_e]:
        p1.extended = 7
        
        
    return
        
def handle_keys_p1(event, p1):
    if (event.key == K_d):
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
