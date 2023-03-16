import pygame,random

bg_img = pygame.image.load('backgroundimage.png')
bg_img = pygame.transform.scale(bg_img, (1280, 780))
bg_rect = bg_img.get_rect()

class GameObject(pygame.sprite.Sprite):
    def __init__(self,img_path,health,damage,centerX,centerY):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.center = (centerX,centerY)
        self.health = health
        self.damage = damage
        
class Player(GameObject):
    def __init__(self,img_path,health,damage,kill_counter,coins):
        self.kill_counter = kill_counter
        self.coins = coins
        super().__init__(img_path,health,damage,bg_rect.centerx,bg_rect.centery)

    def collision(self):
        if self.rect.left < bg_rect.left:
            self.rect.left = bg_rect.left
        if self.rect.right > bg_rect.right:
            self.rect.right = bg_rect.right
        if self.rect.top < bg_rect.top:
            self.rect.top = bg_rect.top
        if self.rect.bottom > 528:
            self.rect.bottom = 528

class Mob(GameObject):
    def __init__(self,img_path,health,damage,speed):
        self.speed = speed
        random_side = random.choice([-1,1])

        # Deciding whether the mob will spawn the left or right
        if random_side == -1: # Left
            rand_x = 50
        else: # Right
            rand_x = bg_rect.right-50

        # Spawn mob at random y value
        rand_y = random.randint(50,528 - 50)

        super().__init__(img_path,health,damage, rand_x,rand_y)
    def update(self):
        self.rect.x = self.rect.x + self.speed[0]
        self.rect.y = self.rect.y + self.speed[1]
        
    def collision(self):
        if self.rect.left < bg_rect.left:
            self.rect.left = bg_rect.left
            self.speed[0] *= -1
        if self.rect.right > bg_rect.right:
            self.rect.right = bg_rect.right
            self.speed[0] *= -1
        if self.rect.top < bg_rect.top:
            self.rect.top = bg_rect.top
            self.speed[1] *= -1
        if self.rect.bottom > 528:
            self.rect.bottom = 528
            self.speed[1] *= -1

class Boss(GameObject):
    def __init__(self,img_path,health,damage,shield):
        self.shield = shield
        super().__init__(img_path,health,damage)

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
