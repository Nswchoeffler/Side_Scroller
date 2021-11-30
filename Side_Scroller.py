#imports
import pygame, sys
from pygame.locals import*
import random, time

#initialize programs
pygame.init()
fire = False

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
displaysurf = pygame.display.set_mode((Screen_width,Screen_height))
displaysurf.fill(white)
pygame.display.set_caption("nick's side scroller")


#fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

#player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (45,550)
        
    def move(self):    
        pressed_keys=pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_a]:
                self.rect.move_ip (-5,0)
        if self.rect.right < Screen_width:
            if pressed_keys[K_d]:
                self.rect.move_ip(5,0)
    def fire(self):
        pressed_keys=pygame.key.get_pressed()
        if pressed_keys[K_w]:
            self.fire = True

        
#enemy class
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,Screen_width-40),0)

    def move(self):
        self.rect.move_ip(0,5)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40,Screen_width-40),0)

player = Player()
E1 = enemy()
E2 =enemy()
#creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(E1)
all_sprites.add(E2)



#game loop
while True:
    
    

    #adds background
    displaysurf.fill(white)
    
    for entity in all_sprites:
        displaysurf.blit(entity.image,entity.rect)
        entity.move()



    #quit the game correctly
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #fire
    if player.fire == True:
        displaysurf.blit(game_over,(30,250))
    #collision
    if pygame.sprite.spritecollideany(player, enemies):
        time.sleep(0.5)

        displaysurf.fill(red)
        displaysurf.blit(game_over,(30,250))



        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    Clock.tick(FPS)

