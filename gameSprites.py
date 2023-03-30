import pygame,random, math

bg_img = pygame.image.load('backgroundimage.png')
bg_img = pygame.transform.scale(bg_img, (1280, 780))
bg_rect = bg_img.get_rect()
waterRect = pygame.Rect(0, 523, 1280, 500)
treeRect = pygame.Rect(912,577,500,500)
treeRectTop = pygame.Rect(836,525,500,10)
treeRectLeft = pygame.Rect(835,526,10,500)
caveRect = pygame.Rect(1022,590,500,500)

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

        #////////////////////////////////Animations//////////////////////////////////////////#
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
        #////////////////////////////////Animations//////////////////////////////////////////#

        super().__init__(img_path,health,damage,bg_rect.centerx,bg_rect.centery)

    #updating
    def update(self):

        #////////////////////////////////Animations//////////////////////////////////////////#
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
        #////////////////////////////////Animations//////////////////////////////////////////#

    #////////////////////////////////Animations//////////////////////////////////////////#    
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
    #////////////////////////////////Animations//////////////////////////////////////////#
    
    def collisionBeach(self):
        if self.rect.left < bg_rect.left - 25:
            self.rect.left = bg_rect.left - 25
        if self.rect.right > bg_rect.right + 25:
            self.rect.right = bg_rect.right + 25
        if self.rect.top < bg_rect.top - 15:
            self.rect.top = bg_rect.top - 15
        if pygame.Rect.colliderect(self.rect, waterRect):
            self.rect.bottom = waterRect.top
    def collisionForest(self):
        if self.rect.left < bg_rect.left - 25:
            self.rect.left = bg_rect.left - 25
        if self.rect.top < bg_rect.top - 15:
            self.rect.top = bg_rect.top - 15
        if self.rect.bottom > bg_rect.bottom + 5:
            self.rect.bottom = bg_rect.bottom + 5
        if self.rect.right > bg_rect.right + 25:
            self.rect.right = bg_rect.right + 25
        if pygame.Rect.colliderect(self.rect, treeRect) and self.rect.centerx > treeRect.left:
            self.rect.bottom = treeRect.top
        if pygame.Rect.colliderect(self.rect, treeRect):
            self.rect.right = treeRect.left
    def collisionCave(self):
        if self.rect.left < bg_rect.left - 25:
            self.rect.left = bg_rect.left - 25
        if self.rect.bottom < 170:
            self.rect.bottom = 170
        if self.rect.bottom > bg_rect.bottom - 3:
            self.rect.bottom = bg_rect.bottom - 3
        if self.rect.right > bg_rect.right + 25:
            self.rect.right = bg_rect.right + 25
        if pygame.Rect.colliderect(self.rect, caveRect) and self.rect.centerx > caveRect.left:
            self.rect.bottom = caveRect.top
        if pygame.Rect.colliderect(self.rect, caveRect):
            self.rect.right = caveRect.left

            
    # def flipPlayer(self,direction):
    #     #initialize player image
    #     player_img_with_left_flip = pygame.transform.flip(self.tempImage, True, False)
    #     player_img_with_right_flip = self.tempImage
    #     #initialize player image
    #     if(direction == 'r'):
    #         self.image = player_img_with_right_flip
    #     else:
    #         self.image = player_img_with_left_flip

class Mob(GameObject):
    def __init__(self,img_path,health,damage,speed):
        self.speed = speed
        random_side = random.choice([-1,1])
        self.direction = 'r'

        # Deciding whether the mob will spawn the left or right
        if random_side == -1: # Left
            rand_x = 50
            self.direction = 'r'
        else: # Right
            rand_x = bg_rect.right-50
            self.direction = 'l'
            for i in range(len(self.speed)):
                self.speed[i] = -self.speed[i]

        # Spawn mob at random y value
        rand_y = random.randint(50,528 - 50)

        #////////////////////////////////Animations//////////////////////////////////////////#
        #for walking animation
        self.walkingRightSprites = []
        self.walkingLeftSprites = []
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile000.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile001.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile002.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile003.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile004.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile005.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile006.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile007.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile008.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile009.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile010.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile011.png'))
        self.walkingRightSprites.append(pygame.image.load('Skeleton\walktile012.png'))
        for i in range(len(self.walkingRightSprites)):
            self.walkingRightSprites[i] = pygame.transform.scale(self.walkingRightSprites[i],(66,88))
        for walk in self.walkingRightSprites:
            self.walkingLeftSprites.append(pygame.transform.flip(walk,True,False))
        self.currentWalk = 0
        self.isWalking = True
        #for attacking animation
        self.attackRightSprites = []
        self.attackLeftSprites = []
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile000.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile001.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile002.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile003.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile004.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile005.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile006.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile007.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile008.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile009.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile010.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile011.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile012.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile013.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile014.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile015.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile016.png'))
        self.attackRightSprites.append(pygame.image.load('Skeleton/attacktile017.png'))
        for i in range(len(self.attackRightSprites)):
            self.attackRightSprites[i] = pygame.transform.scale(self.attackRightSprites[i],(129,111))
        for attack in self.attackRightSprites:
            self.attackLeftSprites.append(pygame.transform.flip(attack,True,False))
        self.currentAttack = 0
        self.isAttacking = False
        #for hit animation
        self.hitRightSprites = []
        self.hitLeftSprites = []
        self.hitRightSprites.append(pygame.image.load('Skeleton\hittile000.png'))
        self.hitRightSprites.append(pygame.image.load('Skeleton\hittile001.png'))
        self.hitRightSprites.append(pygame.image.load('Skeleton\hittile002.png'))
        self.hitRightSprites.append(pygame.image.load('Skeleton\hittile003.png'))
        self.hitRightSprites.append(pygame.image.load('Skeleton\hittile004.png'))
        self.hitRightSprites.append(pygame.image.load('Skeleton\hittile005.png'))
        self.hitRightSprites.append(pygame.image.load('Skeleton\hittile006.png'))
        self.hitRightSprites.append(pygame.image.load('Skeleton\hittile007.png'))
        for i in range(len(self.hitRightSprites)):
            self.hitRightSprites[i] = pygame.transform.scale(self.hitRightSprites[i],(66,88))
        for hit in self.hitRightSprites:
            self.hitLeftSprites.append(pygame.transform.flip(hit,True,False))
        self.currentHit = 0
        self.isHit = False
        #for death animation
        self.deathRightSprites = []
        self.deathLeftSprites = []
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile000.png'))
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile001.png'))
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile002.png'))
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile003.png'))
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile004.png'))
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile005.png'))
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile006.png'))
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile007.png'))
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile008.png'))
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile009.png'))
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile010.png'))
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile011.png'))
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile012.png'))
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile013.png'))
        self.deathRightSprites.append(pygame.image.load('Skeleton\deadtile014.png'))
        for i in range(len(self.deathRightSprites)):
            self.deathRightSprites[i] = pygame.transform.scale(self.deathRightSprites[i],(66,88))
        for death in self.deathRightSprites:
            self.deathLeftSprites.append(pygame.transform.flip(death,True,False))
        self.currentDeath = 0
        self.isDeath = False
        #////////////////////////////////Animations//////////////////////////////////////////#
        super().__init__(img_path,health,damage, rand_x,rand_y)

    def update(self):
        if not self.isDeath == True and not self.isHit == True and not self.isAttacking == True:
            self.rect.x = self.rect.x + self.speed[0]
            self.rect.y = self.rect.y + self.speed[1]

        #////////////////////////////////Animations//////////////////////////////////////////#
        #walking
        if self.isWalking == True and self.isAttacking == False and self.isHit == False and self.isDeath == False:
            self.currentWalk += 0.2
            if self.currentWalk >= len(self.walkingLeftSprites):
                self.currentWalk = 0
            if(self.direction == 'r'):
                self.image = self.walkingRightSprites[int(self.currentWalk)]
            else:
                self.image = self.walkingLeftSprites[int(self.currentWalk)]
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
        #////////////////////////////////Animations//////////////////////////////////////////#

    #////////////////////////////////Animations//////////////////////////////////////////#
    #attacking
    def attack(self):
        self.isAttacking = True
    #hit
    def hit(self):
        self.isHit = True
    #death
    def death(self):
        self.isDeath = True
    #////////////////////////////////Animations//////////////////////////////////////////#
        
    def collisionBeach(self):
        if self.rect.left < bg_rect.left:
            self.rect.left = bg_rect.left
            self.speed[0] *= -1
            self.direction = 'r'
        if self.rect.right > bg_rect.right - 37:
            self.rect.right = bg_rect.right - 37
            self.speed[0] *= -1
            self.direction = 'l'
        if self.rect.top < bg_rect.top:
            self.rect.top = bg_rect.top
            self.speed[1] *= -1
        if self.rect.bottom > 528 - 58:
            self.rect.bottom = 528 - 58
            self.speed[1] *= -1

    def collisionForest(self):
        if self.rect.left < bg_rect.left:
            self.rect.left = bg_rect.left
            self.speed[0] *= -1
            self.direction = 'r'
        if self.rect.top < bg_rect.top:
            self.rect.top = bg_rect.top
            self.speed[1] *= -1
        if self.rect.bottom > bg_rect.bottom - 48:
            self.rect.bottom = bg_rect.bottom-48
            self.speed[1] *= -1
        if self.rect.right > bg_rect.right-37:
            self.rect.right = bg_rect.right-37
            self.speed[0] *= -1
            self.direction = 'l'
        if pygame.Rect.colliderect(self.rect, treeRectTop):
            self.rect.bottom = treeRectTop.top
            self.speed[1] *= -1
        if pygame.Rect.colliderect(self.rect, treeRectLeft):
            self.rect.right = treeRectLeft.left
            self.speed[0] *= -1
            self.direction = 'l'

    def collisionCave(self):
        if self.rect.left < bg_rect.left - 45:
            self.rect.left = bg_rect.left - 45
            self.speed[0] *= -1
            self.direction = 'r'
        if self.rect.bottom < 180 + 35:
            self.rect.bottom = 180 + 35
            self.speed[1] *= -1
        if self.rect.bottom > bg_rect.bottom - 5 + 45:
            self.rect.bottom = bg_rect.bottom - 5 + 45
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
    def __init__(self,img_path,health,damage,speed,shield):
        super().__init__(img_path,health,damage,bg_rect.centerx,bg_rect.centery)
        self.shield = shield
        self.speed = speed

    def update(self, player_rect,mob_group):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = player_rect.x - self.rect.x, player_rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        if(dist<125):
            self.dash()
        else:
            dx, dy = dx / dist, dy / dist  # Normalize.
            # Move along this normalized vector towards the player at current speed.
            self.rect.x += dx * self.speed[0]
            self.rect.y += dy * self.speed[0]
    

    def dash(self):
        # Input code here to perform the boss dash towards the playerCord
        playerCord=0
    
    def mobspawner(self,mob_group):
        for x in range (4):
            mob_group.add(Mob("mob.png", 50, 50, [2,2]))
        
        position = len(mob_group)
        mob_group.sprites()[position-4].rect.top = self.rect.bottom
        mob_group.sprites()[position-3].rect.bottom = self.rect.top
        mob_group.sprites()[position-2].rect.right = self.rect.left
        mob_group.sprites()[position-1].rect.left = self.rect.right




    # def update(self):
    #     self.rect = self.rect.move(self.rand_xd*self.speed,self.rand_yd*self.speed)

    #     # Edge Collision detection, if collided, bounce off edge
    #     if (self.rect.left < 140) or (self.rect.right > 1140):
    #         self.rand_xd *= -1 # Change direction for x
    #     if (self.rect.top < 0) or (self.rect.bottom > 666):
    #         self.rand_yd *= -1 # Change direction for y
