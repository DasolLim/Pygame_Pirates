import pygame,random
from main import bg_rect

class GameObject(pygame.sprite.Sprite):
    def __init__(self,img_path,health,damage,speed,centerX,centerY):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.center = (centerX,centerY)
        self.health = health
        self.damage = damage
        self.speed = speed
    def update(self):
        self.rect.x = self.rect.x + self.speed[0]
        self.rect.y = self.rect.y + self.speed[1]
    def collision(self):
        #code collision for general gameobject i.e. detect when they hit the boundaries
        hitBoundary = False
        
class Player(GameObject):
    def __init__(self,img_path,health,damage,speed,kill_counter,coins):
        self.kill_counter = kill_counter
        self.coins = coins
        super().__init__(self,img_path,health,damage,speed,bg_rect.centerx,bg_rect.centery)

class Mob(GameObject):
    def __init__(self,img_path,health,damage,speed):
        random_side = random.choice([-1,1])

        # Deciding whether the mob will spawn the left or right
        if random_side == -1: # Left
            rand_x = 50
        else: # Right
            rand_x = bg_rect.right-50

        # Spawn mob at random y value
        rand_y = random.randint(50,bg_rect.bottom - 50)

        super().__init__(self,img_path,health,damage,speed, rand_x,rand_y)

class Boss(GameObject):
    def __init__(self,img_path,health,damage,speed,shield):
        self.shield = shield
        super().__init__(self,img_path,health,damage,speed)

    def __tracker__(self, playerCord):
        # Input code here to track player movement
        playerCord=0
    

    def __dash__(self, playerCord):
        # Input code here to perform the boss dash towards the playerCord
        playerCord=0
    
    def __mobSpawner__(self):
        # Input code here for boss to spawn mobs around him
        x=0



    # def update(self):
    #     self.rect = self.rect.move(self.rand_xd*self.speed,self.rand_yd*self.speed)

    #     # Edge Collision detection, if collided, bounce off edge
    #     if (self.rect.left < 140) or (self.rect.right > 1140):
    #         self.rand_xd *= -1 # Change direction for x
    #     if (self.rect.top < 0) or (self.rect.bottom > 666):
    #         self.rand_yd *= -1 # Change direction for y
