import pygame,random

bg_img = pygame.image.load('backgroundimage.png')
bg_img = pygame.transform.scale(bg_img, (1280, 780))
bg_rect = bg_img.get_rect()

class GameObject(pygame.sprite.Sprite):
    def __init__(self,img_path,health,damage,centerX,centerY):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.tempImage = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (centerX,centerY)
        self.health = health
        self.damage = damage
        
class Player(GameObject):
    def __init__(self,img_path,health,damage,kill_counter,coins):
        self.kill_counter = kill_counter
        self.coins = coins
        self.direction = 'r'
        #for attacking animation
        self.attackRightSprites = []
        self.attackLeftSprites = []
        self.attackRightSprites.append(pygame.image.load('Pirate/1_entity_000_ATTACK_000.png'))
        self.attackRightSprites.append(pygame.image.load('Pirate/1_entity_000_ATTACK_001.png'))
        self.attackRightSprites.append(pygame.image.load('Pirate/1_entity_000_ATTACK_002.png'))
        self.attackRightSprites.append(pygame.image.load('Pirate/1_entity_000_ATTACK_003.png'))
        self.attackRightSprites.append(pygame.image.load('Pirate/1_entity_000_ATTACK_004.png'))
        self.attackRightSprites.append(pygame.image.load('Pirate/1_entity_000_ATTACK_005.png'))
        self.attackRightSprites.append(pygame.image.load('Pirate/1_entity_000_ATTACK_006.png'))
        for attack in self.attackRightSprites:
            self.attackLeftSprites.append(pygame.transform.flip(attack,True,False))
        self.currentAttack = 0
        self.isAttacking = False
        #for walking animation
        self.walkingRightSprites = []
        self.walkingLeftSprites = []
        self.walkingRightSprites.append(pygame.image.load('Pirate/1_entity_000_WALK_000.png'))
        self.walkingRightSprites.append(pygame.image.load('Pirate/1_entity_000_WALK_001.png'))
        self.walkingRightSprites.append(pygame.image.load('Pirate/1_entity_000_WALK_002.png'))
        self.walkingRightSprites.append(pygame.image.load('Pirate/1_entity_000_WALK_003.png'))
        self.walkingRightSprites.append(pygame.image.load('Pirate/1_entity_000_WALK_004.png'))
        self.walkingRightSprites.append(pygame.image.load('Pirate/1_entity_000_WALK_005.png'))
        self.walkingRightSprites.append(pygame.image.load('Pirate/1_entity_000_WALK_006.png'))
        for walk in self.walkingRightSprites:
            self.walkingLeftSprites.append(pygame.transform.flip(walk,True,False))
        self.currentWalk = 0
        self.isWalking = False
        #for idle animation
        self.idleRightSprites = []
        self.idleLeftSprites = []
        self.idleRightSprites.append(pygame.image.load('Pirate/1_entity_000_IDLE_000.png'))
        self.idleRightSprites.append(pygame.image.load('Pirate/1_entity_000_IDLE_001.png'))
        self.idleRightSprites.append(pygame.image.load('Pirate/1_entity_000_IDLE_002.png'))
        self.idleRightSprites.append(pygame.image.load('Pirate/1_entity_000_IDLE_003.png'))
        self.idleRightSprites.append(pygame.image.load('Pirate/1_entity_000_IDLE_004.png'))
        self.idleRightSprites.append(pygame.image.load('Pirate/1_entity_000_IDLE_005.png'))
        self.idleRightSprites.append(pygame.image.load('Pirate/1_entity_000_IDLE_006.png'))
        for idle in self.idleRightSprites:
            self.idleLeftSprites.append(pygame.transform.flip(idle,True,False))
        self.currentIdle = 0
        #for hit animation
        self.hitRightSprites = []
        self.hitLeftSprites = []
        self.hitRightSprites.append(pygame.image.load('Pirate/1_entity_000_HURT_000.png'))
        self.hitRightSprites.append(pygame.image.load('Pirate/1_entity_000_HURT_001.png'))
        self.hitRightSprites.append(pygame.image.load('Pirate/1_entity_000_HURT_002.png'))
        self.hitRightSprites.append(pygame.image.load('Pirate/1_entity_000_HURT_003.png'))
        self.hitRightSprites.append(pygame.image.load('Pirate/1_entity_000_HURT_004.png'))
        self.hitRightSprites.append(pygame.image.load('Pirate/1_entity_000_HURT_005.png'))
        self.hitRightSprites.append(pygame.image.load('Pirate/1_entity_000_HURT_006.png'))
        for hit in self.hitRightSprites:
            self.hitLeftSprites.append(pygame.transform.flip(hit,True,False))
        self.currentHit = 0
        self.isHit = False
        #for death animation
        self.deathRightSprites = []
        self.deathLeftSprites = []
        self.deathRightSprites.append(pygame.image.load('Pirate/1_entity_000_DIE_000.png'))
        self.deathRightSprites.append(pygame.image.load('Pirate/1_entity_000_DIE_001.png'))
        self.deathRightSprites.append(pygame.image.load('Pirate/1_entity_000_DIE_002.png'))
        self.deathRightSprites.append(pygame.image.load('Pirate/1_entity_000_DIE_003.png'))
        self.deathRightSprites.append(pygame.image.load('Pirate/1_entity_000_DIE_004.png'))
        self.deathRightSprites.append(pygame.image.load('Pirate/1_entity_000_DIE_005.png'))
        self.deathRightSprites.append(pygame.image.load('Pirate/1_entity_000_DIE_006.png'))
        for death in self.deathRightSprites:
            self.deathLeftSprites.append(pygame.transform.flip(death,True,False))
        self.currentDeath = 0
        self.isDeath = False
        

        super().__init__(img_path,health,damage,bg_rect.centerx,bg_rect.centery)

    #updating
    def update(self):
        #attacking
        if self.isAttacking == True and self.isHit == False and self.isDeath == False:
            self.currentAttack += 0.4
            if self.currentAttack >= len(self.attackLeftSprites):
                self.currentAttack = 0
                self.isAttacking = False
            if(self.direction == 'r'):
                self.image = self.attackRightSprites[int(self.currentAttack)]
            else:
               self.image = self.attackLeftSprites[int(self.currentAttack)] 
        #walking
        if self.isWalking == True and self.isAttacking == False and self.isHit == False and self.isDeath == False:
            self.currentWalk += 0.4
            if self.currentWalk >= len(self.walkingLeftSprites):
                self.currentWalk = 0
                self.isWalking = False
            if(self.direction == 'r'):
                self.image = self.walkingRightSprites[int(self.currentWalk)]
            else:
                self.image = self.walkingLeftSprites[int(self.currentWalk)]
        #idle
        if self.isAttacking == False and self.isWalking == False and self.isHit == False and self.isDeath == False:
            self.currentIdle += 0.3
            if self.currentIdle >= len(self.idleLeftSprites):
                self.currentIdle = 0
            if(self.direction == 'r'):
                self.image = self.idleRightSprites[int(self.currentIdle)]
            else:
                self.image = self.idleLeftSprites[int(self.currentIdle)]
        #hit
        if self.isHit == True and self.isDeath == False:
            self.currentHit += 0.4
            if self.currentHit >= len(self.hitLeftSprites):
                self.currentHit = 0
                self.isHit = False
            if(self.direction == 'r'):
                self.image = self.hitRightSprites[int(self.currentHit)]
            else:
                self.image = self.hitLeftSprites[int(self.currentHit)]
        #death
        if self.isDeath == True:
            self.currentDeath += 0.4
            if self.currentDeath >= len(self.deathLeftSprites):
                self.currentDeath = len(self.deathLeftSprites) - 1
                # self.isDeath = False
            if(self.direction == 'r'):
                self.image = self.deathRightSprites[int(self.currentDeath)]
            else:
                self.image = self.deathLeftSprites[int(self.currentDeath)]
    #attacking
    def attack(self):
        self.isAttacking = True
    #walking
    def walk(self):
        self.isWalking = True
    #hit
    def hit(self):
        self.isHit = True
    #death
    def death(self):
        self.isDeath = True
    
    def collisionBeach(self):
        if self.rect.left < bg_rect.left - 25:
            self.rect.left = bg_rect.left - 25
        if self.rect.right > bg_rect.right + 25:
            self.rect.right = bg_rect.right + 25
        if self.rect.top < bg_rect.top - 15:
            self.rect.top = bg_rect.top - 15
        if self.rect.bottom > 528:
            self.rect.bottom = 528

    def collisionForest(self):
        if self.rect.left < bg_rect.left - 25:
            self.rect.left = bg_rect.left - 25
        if self.rect.top < bg_rect.top - 15:
            self.rect.top = bg_rect.top - 15
        if self.rect.bottom > bg_rect.bottom + 5:
            self.rect.bottom = bg_rect.bottom + 5
        if self.rect.right > bg_rect.right + 25:
            self.rect.right = bg_rect.right + 25
        if self.rect.bottom > 591 and self.rect.centerx > 920:
            self.rect.bottom = 591
        if self.rect.right > 920 and self.rect.bottom > 591:
            self.rect.right = 920

    def collisionCave(self):
        if self.rect.left < bg_rect.left - 25:
            self.rect.left = bg_rect.left - 25
        if self.rect.bottom < 170:
            self.rect.bottom = 170
        if self.rect.bottom > bg_rect.bottom - 3:
            self.rect.bottom = bg_rect.bottom - 3
        if self.rect.right > bg_rect.right + 25:
            self.rect.right = bg_rect.right + 25
        if self.rect.bottom > 584 and self.rect.centerx > 1020:
            self.rect.bottom = 584
        if self.rect.right > 1020 and self.rect.bottom > 585:
            self.rect.right = 1020
            
    def flipPlayer(self,direction):
        #initialize player image
        player_img_with_left_flip = pygame.transform.flip(self.tempImage, True, False)
        player_img_with_right_flip = self.tempImage
        #initialize player image
        if(direction == 'r'):
            self.image = player_img_with_right_flip
        else:
            self.image = player_img_with_left_flip

class Mob(GameObject):
    def __init__(self,img_path,health,damage,speed):
        self.speed = speed
        random_side = random.choice([-1,1])
        self.direction = 'r'

        # Deciding whether the mob will spawn the left or right
        if random_side == -1: # Left
            rand_x = 50
            self.direction = 'l'
        else: # Right
            rand_x = bg_rect.right-50
            self.direction = 'r'

        # Spawn mob at random y value
        rand_y = random.randint(50,528 - 50)

        #for walking animation
        self.walkingRightSprites = []
        self.walkingLeftSprites = []
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile000.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile001.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile002.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile003.png'))
        for walk in self.walkingRightSprites:
            self.walkingLeftSprites.append(pygame.transform.flip(walk,True,False))
        self.currentWalk = 0
        self.isWalking = True

        super().__init__(img_path,health,damage, rand_x,rand_y)

    def update(self):
        self.rect.x = self.rect.x + self.speed[0]
        self.rect.y = self.rect.y + self.speed[1]
        #walking
        if self.isWalking == True: #and self.isAttacking == False and self.isHit == False and self.isDeath == False:
            self.currentWalk += 0.2
            if self.currentWalk >= len(self.walkingLeftSprites):
                self.currentWalk = 0
            if(self.direction == 'r'):
                self.image = self.walkingRightSprites[int(self.currentWalk)]
            else:
                self.image = self.walkingLeftSprites[int(self.currentWalk)]
        
    def collisionBeach(self):
        if self.rect.left < bg_rect.left:
            self.rect.left = bg_rect.left
            self.speed[0] *= -1
            self.direction = 'r'
        if self.rect.right > bg_rect.right:
            self.rect.right = bg_rect.right
            self.speed[0] *= -1
            self.direction = 'l'
        if self.rect.top < bg_rect.top:
            self.rect.top = bg_rect.top
            self.speed[1] *= -1
        if self.rect.bottom > 528:
            self.rect.bottom = 528
            self.speed[1] *= -1

    def collisionForest(self):
        if self.rect.left < bg_rect.left:
            self.rect.left = bg_rect.left
            self.speed[0] *= -1
            self.direction = 'r'
        if self.rect.top < bg_rect.top:
            self.rect.top = bg_rect.top
            self.speed[1] *= -1
        if self.rect.bottom > bg_rect.bottom:
            self.rect.bottom = bg_rect.bottom
            self.speed[1] *= -1
        if self.rect.right > bg_rect.right:
            self.rect.right = bg_rect.right
            self.speed[0] *= -1
            self.direction = 'l'
        if self.rect.bottom > 591 and self.rect.centerx > 920:
            self.rect.bottom = 591
            self.speed[1] *= -1
        if self.rect.right > 920 and self.rect.bottom > 591:
            self.rect.right = 920
            self.speed[0] *= -1
            self.direction = 'l'

    def collisionCave(self):
        if self.rect.left < bg_rect.left:
            self.rect.left = bg_rect.left
            self.speed[0] *= -1
            self.direction = 'r'
        if self.rect.bottom < 180:
            self.rect.bottom = 180
            self.speed[1] *= -1
        if self.rect.bottom > bg_rect.bottom - 5:
            self.rect.bottom = bg_rect.bottom - 5
            self.speed[1] *= -1
        if self.rect.right > bg_rect.right:
            self.rect.right = bg_rect.right
            self.speed[0] *= -1
            self.direction = 'l'
        if self.rect.bottom > 574 and self.rect.centerx > 995:
            self.rect.bottom = 574
            self.speed[1] *= -1
        if self.rect.right > 995 and self.rect.bottom > 585:
            self.rect.right = 995
            self.speed[0] *= -1
            self.direction = 'l'

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
