#imports
import pygame, sys
from pygame.locals import*
import random, time

#initialize programs
pygame.init()

#FPS assigning
FPS= 60 
Clock = pygame.time.Clock()

#colors
blue= (0,0,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

#screen set up
Screen_width = 600
Screen_height = 600

#display surf

background = pygame.image.load('background_side_scroller.png')
displaysurf = pygame.display.set_mode((Screen_width,Screen_height))
displaysurf.fill(white)
pygame.display.set_caption("nick's side scroller")


#fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

#player class
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player1_pro.png")
        self.rect = self.image.get_rect()
        self.rect.center = (80,80)
        self.rect.move_ip(0,330)
    def move(self):    
        pressed_keys=pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_a]:
                self.rect.move_ip (-5,0)
        if self.rect.right < Screen_width:
            if pressed_keys[K_d]:
                self.rect.move_ip(5,0)

    def jump(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_w]:
            self.rect.move_ip(0,-5)
    def attack(self):
        pressed_keys = pygame.key.get_pressed
        
#enemy class

#player and enemy 
P1= player()
#E1= enemy()

#creating Sprites Groups
#enemies = pygame.sprite.Group()
#enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
#all_sprites.add(E1)
#game loop
while True:
    #adds background
    
    displaysurf.blit(background,(0,0))
    

    for entity in all_sprites:
        displaysurf.blit(entity.image,entity.rect)
        entity.move()




    #quit the game correctly
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
        
        #time.sleep(2)
        #pygame.quit()
        #sys.exit()


    pygame.display.update()
    Clock.tick(FPS)

