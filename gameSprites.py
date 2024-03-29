# imports
import pygame,random, math, random

# initializing images
bg_img = pygame.image.load('Scenes/backgroundimage.png')
bg_img = pygame.transform.scale(bg_img, (1280, 780))
bg_rect = bg_img.get_rect()

# creating rectangles
waterRect = pygame.Rect(0, 523, 1280, 500)
treeRect = pygame.Rect(912,577,500,500)
treeRectTop = pygame.Rect(836,525,500,500)
treeRectLeft = pygame.Rect(835,526,10,500)
treeRectTopGob = pygame.Rect(875,530,500,500)
treeRectLeftGob = pygame.Rect(874,531,10,500)
caveRect = pygame.Rect(1022,590,500,500)
caveRectTop = pygame.Rect(961,540,500,500)
cavRectLeft = pygame.Rect(960, 541, 10,500)

# parent sprite object
class GameObject(pygame.sprite.Sprite):
    def __init__(self,img_path,health,damage,centerX,centerY,speed):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.tempImage = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (centerX,centerY)
        self.health = health
        self.damage = damage
        self.speed = speed
        self.whoKilled = ''

# player sprite object
class Player(GameObject):
    def __init__(self,img_path,health,damage,speed,coins,luck):
        self.coins = coins
        self.direction = 'r'
        self.luck = luck
        self.maxHealth = health
        
        #////////////////////////////////Animations//////////////////////////////////////////#
        # for attacking animation
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

        # for walking animation
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

        # for idle animation
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

        # for hit animation
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
        
        # for death animation
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
        
        # super constructor call
        super().__init__(img_path,health,damage,bg_rect.centerx,bg_rect.centery,speed)
        
    # updating
    def update(self):
        
        #////////////////////////////////Animations//////////////////////////////////////////#
        # attacking
        if self.isAttacking == True and self.isHit == False and self.isDeath == False:
            self.currentAttack += 0.4
            
            if self.currentAttack >= len(self.attackLeftSprites):
                self.currentAttack = 0
                self.isAttacking = False
                
            if(self.direction == 'r'):
                self.image = self.attackRightSprites[int(self.currentAttack)]
            else:
               self.image = self.attackLeftSprites[int(self.currentAttack)] 
               
        # walking
        if self.isWalking == True and self.isAttacking == False and self.isHit == False and self.isDeath == False:
            self.currentWalk += 0.4
            
            if self.currentWalk >= len(self.walkingLeftSprites):
                self.currentWalk = 0
                self.isWalking = False
                
            if(self.direction == 'r'):
                self.image = self.walkingRightSprites[int(self.currentWalk)]
            else:
                self.image = self.walkingLeftSprites[int(self.currentWalk)]
                
        # idle
        if self.isAttacking == False and self.isWalking == False and self.isHit == False and self.isDeath == False:
            self.currentIdle += 0.3
            
            if self.currentIdle >= len(self.idleLeftSprites):
                self.currentIdle = 0

            if(self.direction == 'r'):
                self.image = self.idleRightSprites[int(self.currentIdle)]
            else:
                self.image = self.idleLeftSprites[int(self.currentIdle)]

        # hit
        if self.isHit == True and self.isDeath == False:
            self.currentHit += 0.4

            if self.currentHit >= len(self.hitLeftSprites):
                self.currentHit = 0
                self.isHit = False

                if self.health <= 0:
                    self.death()
                    self.isDeath = True

            if(self.direction == 'r'):
                self.image = self.hitRightSprites[int(self.currentHit)]
            else:
                self.image = self.hitLeftSprites[int(self.currentHit)]
                
        # death
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
        
    #////////////////////////////////Animation Methods//////////////////////////////////////////#    
    # attacking
    def attack(self):
        self.isAttacking = True
        
    # walking
    def walk(self):
        self.isWalking = True

    # hit
    def hit(self):
        self.isHit = True
        
    # death
    def death(self):
        self.isDeath = True
    #////////////////////////////////Animation Methods//////////////////////////////////////////#
    
    #///////////////////////////////Collisions//////////////////////////////////////////#
    # collision beach scene
    def collisionBeach(self):
        if self.rect.left < bg_rect.left - 25:
            self.rect.left = bg_rect.left - 25
        if self.rect.right > bg_rect.right + 25:
            self.rect.right = bg_rect.right + 25
        if self.rect.top < bg_rect.top - 15:
            self.rect.top = bg_rect.top - 15
        if pygame.Rect.colliderect(self.rect, waterRect):
            self.rect.bottom = waterRect.top

    # collision forest scene
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
            
    #collision cave scene
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
    #///////////////////////////////Collisions//////////////////////////////////////////#

# coin sprite object
class Coin(pygame.sprite.Sprite):
    def __init__(self,img_path, centerX, centerY):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.center = (centerX, centerY)

# mob class object (skeleton)
class Mob1(GameObject):
    def __init__(self,img_path,health,damage,speed):
        random_side = random.choice([-1,1])
        self.direction = 'r'
        self.type = "skeleton"
        self.playerDamage = 0
        
        # deciding whether the mob will spawn the left or right
        if random_side == -1: # Left
            rand_x = 50
            self.direction = 'r'
        else:
            rand_x = bg_rect.right-50
            self.direction = 'l'

        # spawn mob at random y value
        rand_y = random.randint(50,528 - 50)
        
        # super constructor call
        super().__init__(img_path,health,damage, rand_x,rand_y,speed)
        
        # fixing direction
        if self.direction == "l":
            for i in range(len(self.speed)):
                self.speed[i] = -self.speed[i]

        #////////////////////////////////Animations//////////////////////////////////////////#
        # for walking animation
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

        # for attacking animation
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

        # for hit animation
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
        
        # for death animation
        self.deathRightSprites = []
        self.deathLeftSprites = []
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
        
    # updating
    def update(self, mob_group, player, coinItem_group):
        if not self.isDeath == True and not self.isHit == True and not self.isAttacking == True:
            self.rect.x = self.rect.x + self.speed[0]
            self.rect.y = self.rect.y + self.speed[1]

        #////////////////////////////////Animations//////////////////////////////////////////#
        # walking
        if self.isWalking == True and self.isAttacking == False and self.isHit == False and self.isDeath == False:
            self.currentWalk += 0.2
            
            if self.currentWalk >= len(self.walkingLeftSprites):
                self.currentWalk = 0

            if(self.direction == 'r'):
                self.image = self.walkingRightSprites[int(self.currentWalk)]
            else:
                self.image = self.walkingLeftSprites[int(self.currentWalk)]

        # attacking
        if self.isAttacking == True and self.isHit == False and self.isDeath == False:
            self.currentAttack += 0.4

            if self.currentAttack >= len(self.attackLeftSprites):
                self.currentAttack = 0
                self.isAttacking = False
                player.health -= self.damage

                if player.health > 0:
                    player.whoKilled = self.type
                player.hit()

            if(self.direction == 'r'):
                self.image = self.attackRightSprites[int(self.currentAttack)]
            else:
               self.image = self.attackLeftSprites[int(self.currentAttack)] 

        # hit
        if self.isHit == True and self.isDeath == False:
            self.currentHit += 0.4

            if self.currentHit >= len(self.hitLeftSprites):
                self.currentHit = 0
                self.isHit = False
                self.health -= self.playerDamage

                if self.health <= 0:
                    self.death()

            if(self.direction == 'r'):
                self.image = self.hitRightSprites[int(self.currentHit)]
            else:
                self.image = self.hitLeftSprites[int(self.currentHit)]
                
        # death
        if self.isDeath == True:
            self.currentDeath += 0.4

            if self.currentDeath >= len(self.deathLeftSprites):
                self.currentDeath = len(self.deathLeftSprites) - 1
                self.isDeath = False
                self.selfRemove(mob_group)
                rand_x = random.randint(100, 1000)
                rand_y = random.randint(50,528 - 50)
                coinItem_group.add(Coin("Scenes\coinItemImage.png", rand_x, rand_y))
                randExtra = player.luck * 100
                randNum = random.randint(1,100)

                if randExtra >= randNum:
                    rand_x = random.randint(100, 1000)
                    rand_y = random.randint(50,528 - 50)
                    coinItem_group.add(Coin("Scenes\coinItemImage.png", rand_x, rand_y))

            if(self.direction == 'r'):
                self.image = self.deathRightSprites[int(self.currentDeath)]
            else:
                self.image = self.deathLeftSprites[int(self.currentDeath)]
        #////////////////////////////////Animations//////////////////////////////////////////#

    #////////////////////////////////Animation Methods//////////////////////////////////////////#
    # attacking
    def attack(self):
        self.isAttacking = True

    # hit
    def hit(self):
        self.isHit = True
        
    # death
    def death(self):
        self.isDeath = True

    #////////////////////////////////Animation Methods//////////////////////////////////////////#
    # remove sprite
    def selfRemove(self, mob_group):
        mob_group.remove(self)

    #///////////////////////////////Collisions//////////////////////////////////////////#
    # collision for beach scene
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

    # collision for forest scene
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
            
    # collision for cave scene       
    def collisionCave(self):
        if self.rect.left < bg_rect.left:
            self.rect.left = bg_rect.left
            self.speed[0] *= -1
            self.direction = 'r'
        if self.rect.bottom < 180 - 75:
            self.rect.bottom = 180 - 75
            self.speed[1] *= -1
        if self.rect.bottom > bg_rect.bottom - 5 - 55:
            self.rect.bottom = bg_rect.bottom - 5 - 55
            self.speed[1] *= -1
        if self.rect.right > bg_rect.right - 37:
            self.rect.right = bg_rect.right - 37
            self.speed[0] *= -1
            self.direction = 'l'
        if pygame.Rect.colliderect(self.rect, caveRectTop):
            self.rect.bottom = caveRectTop.top
            self.speed[1] *= -1
        if pygame.Rect.colliderect(self.rect, cavRectLeft):
            self.rect.right = cavRectLeft.left
            self.speed[0] *= -1
            self.direction = 'l'
    #///////////////////////////////Collisions//////////////////////////////////////////#

# mob2 sprite object (goblin)
class Mob2(GameObject):
    def __init__(self,img_path,health,damage,speed):
        random_side = random.choice([-1,1])
        self.direction = 'r'
        self.type = "goblin"
        self.playerDamage = 0

        # deciding whether the mob will spawn the left or right
        if random_side == -1:
            rand_x = 50
            self.direction = 'r'
        else:
            rand_x = bg_rect.right-50
            self.direction = 'l'
            
        # spawn mob at random y value
        rand_y = random.randint(50,528 - 50)
        super().__init__(img_path,health,damage, rand_x,rand_y,speed)

        # fixing direction
        if self.direction == "l":
            for i in range(len(self.speed)):
                self.speed[i] = -self.speed[i]

        #////////////////////////////////Animations//////////////////////////////////////////#
        # for walking animation
        self.walkingRightSprites = []
        self.walkingLeftSprites = []
        self.walkingRightSprites.append(pygame.image.load('Goblin/runtile000.png'))
        self.walkingRightSprites.append(pygame.image.load('Goblin/runtile001.png'))
        self.walkingRightSprites.append(pygame.image.load('Goblin/runtile002.png'))
        self.walkingRightSprites.append(pygame.image.load('Goblin/runtile003.png'))
        self.walkingRightSprites.append(pygame.image.load('Goblin/runtile004.png'))
        self.walkingRightSprites.append(pygame.image.load('Goblin/runtile005.png'))
        self.walkingRightSprites.append(pygame.image.load('Goblin/runtile006.png'))
        self.walkingRightSprites.append(pygame.image.load('Goblin/runtile007.png'))

        for i in range(len(self.walkingRightSprites)):
            self.walkingRightSprites[i] = pygame.transform.scale(self.walkingRightSprites[i],(200,200))

        for walk in self.walkingRightSprites:
            self.walkingLeftSprites.append(pygame.transform.flip(walk,True,False))

        self.currentWalk = 0
        self.isWalking = True
        
        # for attacking animation
        self.attackRightSprites = []
        self.attackLeftSprites = []
        self.attackRightSprites.append(pygame.image.load('Goblin/attacktile000.png'))
        self.attackRightSprites.append(pygame.image.load('Goblin/attacktile001.png'))
        self.attackRightSprites.append(pygame.image.load('Goblin/attacktile002.png'))
        self.attackRightSprites.append(pygame.image.load('Goblin/attacktile003.png'))
        self.attackRightSprites.append(pygame.image.load('Goblin/attacktile004.png'))
        self.attackRightSprites.append(pygame.image.load('Goblin/attacktile005.png'))
        self.attackRightSprites.append(pygame.image.load('Goblin/attacktile006.png'))
        self.attackRightSprites.append(pygame.image.load('Goblin/attacktile007.png'))

        for i in range(len(self.attackRightSprites)):
            self.attackRightSprites[i] = pygame.transform.scale(self.attackRightSprites[i],(200,200))

        for attack in self.attackRightSprites:
            self.attackLeftSprites.append(pygame.transform.flip(attack,True,False))

        self.currentAttack = 0
        self.isAttacking = False
        
        # for hit animation
        self.hitRightSprites = []
        self.hitLeftSprites = []
        self.hitRightSprites.append(pygame.image.load('Goblin\hittile000.png'))
        self.hitRightSprites.append(pygame.image.load('Goblin\hittile001.png'))
        self.hitRightSprites.append(pygame.image.load('Goblin\hittile002.png'))
        self.hitRightSprites.append(pygame.image.load('Goblin\hittile003.png'))

        for i in range(len(self.hitRightSprites)):
            self.hitRightSprites[i] = pygame.transform.scale(self.hitRightSprites[i],(200,200))

        for hit in self.hitRightSprites:
            self.hitLeftSprites.append(pygame.transform.flip(hit,True,False))

        self.currentHit = 0
        self.isHit = False
        
        # for death animation
        self.deathRightSprites = []
        self.deathLeftSprites = []
        self.deathRightSprites.append(pygame.image.load('Goblin\deathtile001.png'))
        self.deathRightSprites.append(pygame.image.load('Goblin\deathtile002.png'))
        self.deathRightSprites.append(pygame.image.load('Goblin\deathtile003.png'))

        for i in range(len(self.deathRightSprites)):
            self.deathRightSprites[i] = pygame.transform.scale(self.deathRightSprites[i],(200,200))

        for death in self.deathRightSprites:
            self.deathLeftSprites.append(pygame.transform.flip(death,True,False))

        self.currentDeath = 0
        self.isDeath = False
        #////////////////////////////////Animations//////////////////////////////////////////#

    # updating
    def update(self,mob_group, player, coinItem_group):
        if not self.isDeath == True and not self.isHit == True and not self.isAttacking == True:
            self.rect.x = self.rect.x + self.speed[0]
            self.rect.y = self.rect.y + self.speed[1]
        
        #////////////////////////////////Animations//////////////////////////////////////////#
        # walking
        if self.isWalking == True and self.isAttacking == False and self.isHit == False and self.isDeath == False:
            self.currentWalk += 0.2

            if self.currentWalk >= len(self.walkingLeftSprites):
                self.currentWalk = 0

            if(self.direction == 'r'):
                self.image = self.walkingRightSprites[int(self.currentWalk)]
            else:
                self.image = self.walkingLeftSprites[int(self.currentWalk)]
                
        # attacking
        if self.isAttacking == True and self.isHit == False and self.isDeath == False:
            self.currentAttack += 0.4

            if self.currentAttack >= len(self.attackLeftSprites):
                self.currentAttack = 0
                self.isAttacking = False
                player.health -= self.damage

                if player.health > 0:
                    player.whoKilled = self.type
                player.hit()

            if(self.direction == 'r'):
                self.image = self.attackRightSprites[int(self.currentAttack)]
            else:
               self.image = self.attackLeftSprites[int(self.currentAttack)] 
               
        # hit
        if self.isHit == True and self.isDeath == False:
            self.currentHit += 0.4

            if self.currentHit >= len(self.hitLeftSprites):
                self.currentHit = 0
                self.isHit = False
                self.health -= self.playerDamage

                if self.health <= 0:
                    self.death()
                    
            if(self.direction == 'r'):
                self.image = self.hitRightSprites[int(self.currentHit)]
            else:
                self.image = self.hitLeftSprites[int(self.currentHit)]
                
        # death
        if self.isDeath == True:
            self.currentDeath += 0.2
            
            if self.currentDeath >= len(self.deathLeftSprites):
                self.currentDeath = len(self.deathLeftSprites) - 1
                self.isDeath = False
                self.selfRemove(mob_group)
                rand_x = random.randint(100, 1000)
                rand_y = random.randint(50,528 - 50)
                coinItem_group.add(Coin("Scenes\coinItemImage.png", rand_x, rand_y))
                randExtra = player.luck * 100
                randNum = random.randint(1,100)
                
                if randExtra >= randNum:
                    rand_x = random.randint(100, 1000)
                    rand_y = random.randint(50,528 - 50)
                    coinItem_group.add(Coin("Scenes\coinItemImage.png", rand_x, rand_y))

            if(self.direction == 'r'):
                self.image = self.deathRightSprites[int(self.currentDeath)]
            else:
                self.image = self.deathLeftSprites[int(self.currentDeath)]
        #////////////////////////////////Animations//////////////////////////////////////////#
        
    # remove sprite
    def selfRemove(self, mob_group):
        mob_group.remove(self)

    #////////////////////////////////Animation Methods//////////////////////////////////////////#
    #attacking
    def attack(self):
        self.isAttacking = True
    #hit
    def hit(self):
        self.isHit = True
    #death
    def death(self):
        self.isDeath = True
    #////////////////////////////////Animation Methods//////////////////////////////////////////#
        
    #///////////////////////////////Collisions//////////////////////////////////////////#
    # colision for forest scene
    def collisionForest(self):
        if self.rect.left < bg_rect.left-70:
            self.rect.left = bg_rect.left-70
            self.speed[0] *= -1
            self.direction = 'r'
        if self.rect.top < bg_rect.top-80:
            self.rect.top = bg_rect.top-80
            self.speed[1] *= -1
        if self.rect.bottom > bg_rect.bottom - 40:
            self.rect.bottom = bg_rect.bottom-40
            self.speed[1] *= -1
        if self.rect.right > bg_rect.right-20:
            self.rect.right = bg_rect.right-20
            self.speed[0] *= -1
            self.direction = 'l'
        if pygame.Rect.colliderect(self.rect, treeRectTopGob):
            self.rect.bottom = treeRectTopGob.top
            self.speed[1] *= -1
        if pygame.Rect.colliderect(self.rect, treeRectLeftGob):
            self.rect.right = treeRectLeftGob.left
            self.speed[0] *= -1
            self.direction = 'l'
    #///////////////////////////////Collisions//////////////////////////////////////////#

# boss sprite object
class Boss(GameObject):
    def __init__(self,img_path,health,damage,speed):
        super().__init__(img_path,health,damage,bg_rect.centerx,bg_rect.centery,speed)
        self.direction = 'r'
        self.framecount = 0
        self.framecountmobspawn = 0
        self.playerDamage = 0
        self.type = "boss"

        #////////////////////////////////Animations//////////////////////////////////////////#
        #for walking animation
        self.walkingRightSprites = []
        self.walkingLeftSprites = []
        self.walkingRightSprites.append(pygame.image.load('Boss\walktile000.png'))
        self.walkingRightSprites.append(pygame.image.load('Boss\walktile001.png'))
        self.walkingRightSprites.append(pygame.image.load('Boss\walktile002.png'))
        self.walkingRightSprites.append(pygame.image.load('Boss\walktile003.png'))
        self.walkingRightSprites.append(pygame.image.load('Boss\walktile004.png'))
        self.walkingRightSprites.append(pygame.image.load('Boss\walktile005.png'))
        self.walkingRightSprites.append(pygame.image.load('Boss\walktile006.png'))
        
        for i in range(len(self.walkingRightSprites)):
            self.walkingRightSprites[i] = pygame.transform.scale(self.walkingRightSprites[i],(200,200))
            
        for walk in self.walkingRightSprites:
            self.walkingLeftSprites.append(pygame.transform.flip(walk,True,False))

        self.currentWalk = 0
        self.isWalking = True

        #for attacking animation
        self.attackRightSprites = []
        self.attackLeftSprites = []
        self.attackRightSprites.append(pygame.image.load('Boss/attacktile000.png'))
        self.attackRightSprites.append(pygame.image.load('Boss/attacktile001.png'))
        self.attackRightSprites.append(pygame.image.load('Boss/attacktile002.png'))
        self.attackRightSprites.append(pygame.image.load('Boss/attacktile003.png'))
        self.attackRightSprites.append(pygame.image.load('Boss/attacktile004.png'))
        self.attackRightSprites.append(pygame.image.load('Boss/attacktile005.png'))
        
        for i in range(len(self.attackRightSprites)):
            self.attackRightSprites[i] = pygame.transform.scale(self.attackRightSprites[i],(200,200))
            
        for attack in self.attackRightSprites:
            self.attackLeftSprites.append(pygame.transform.flip(attack,True,False))
            
        self.currentAttack = 0
        self.isAttacking = False
        
        #for idle animation
        self.idleRightSprites = []
        self.idleLeftSprites = []
        self.idleRightSprites.append(pygame.image.load('Boss\idletile000.png'))
        self.idleRightSprites.append(pygame.image.load('Boss\idletile001.png'))
        self.idleRightSprites.append(pygame.image.load('Boss\idletile002.png'))
        self.idleRightSprites.append(pygame.image.load('Boss\idletile003.png'))
        self.idleRightSprites.append(pygame.image.load('Boss\idletile004.png'))
        self.idleRightSprites.append(pygame.image.load('Boss\idletile005.png'))
        self.idleRightSprites.append(pygame.image.load('Boss\idletile006.png'))

        for i in range(len(self.idleRightSprites)):
            self.idleRightSprites[i] = pygame.transform.scale(self.idleRightSprites[i],(200,200))

        for idle in self.idleRightSprites:
            self.idleLeftSprites.append(pygame.transform.flip(idle,True,False))
            
        self.currentIdle = 0
        self.isIdle = False
        
        #for run animation
        self.runRightSprites = []
        self.runLeftSprites = []
        self.runRightSprites.append(pygame.image.load('Boss/run2tile000.png'))
        self.runRightSprites.append(pygame.image.load('Boss/run2tile001.png'))
        self.runRightSprites.append(pygame.image.load('Boss/run2tile002.png'))
        self.runRightSprites.append(pygame.image.load('Boss/run2tile003.png'))
        self.runRightSprites.append(pygame.image.load('Boss/run2tile004.png'))
        self.runRightSprites.append(pygame.image.load('Boss/run2tile005.png'))
        self.runRightSprites.append(pygame.image.load('Boss/run2tile006.png'))
        self.runRightSprites.append(pygame.image.load('Boss/run2tile007.png'))
        
        for i in range(len(self.runRightSprites)):
            self.runRightSprites[i] = pygame.transform.scale(self.runRightSprites[i],(200,200))
            
        for run in self.runRightSprites:
            self.runLeftSprites.append(pygame.transform.flip(run,True,False))
            
        self.currentRun = 0
        self.isRun = False
        
        #for death animation
        self.deathRightSprites = []
        self.deathLeftSprites = []
        self.deathRightSprites.append(pygame.image.load('Boss\deathtile000.png'))
        self.deathRightSprites.append(pygame.image.load('Boss\deathtile001.png'))
        self.deathRightSprites.append(pygame.image.load('Boss\deathtile002.png'))
        self.deathRightSprites.append(pygame.image.load('Boss\deathtile003.png'))

        for i in range(len(self.deathRightSprites)):
            self.deathRightSprites[i] = pygame.transform.scale(self.deathRightSprites[i],(200,200))

        for death in self.deathRightSprites:
            self.deathLeftSprites.append(pygame.transform.flip(death,True,False))

        self.currentDeath = 0
        self.isDeath = False

        # variables
        self.isHit = False
        self.currentHit = 0

        #////////////////////////////////Animations//////////////////////////////////////////#
    
    # update
    def update(self, player_rect, boss_group, mob_group):

        # find direction vector (dx, dy) between enemy and player.
        dx, dy = player_rect.centerx - self.rect.centerx, player_rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        
        if player_rect.centerx < self.rect.right:
            self.direction = 'l'
        else:
            self.direction = 'r'

        # boss tracking/attacking
        if(dist <= 50 or self.isIdle or self.isAttacking):
            self.framecountmobspawn = 0
            self.isWalking = False

            if self.framecount < 20:
                self.attack()
                self.framecount = self.framecount + 1
            else:
                self.idle()
                self.framecount = self.framecount + 1
                if self.framecount > 115:
                    self.isIdle = False
                    self.framecount = 0

        # boss mob spawning
        elif(dist>50 and not self.isIdle and not self.isAttacking):
            self.framecount = 0
            self.framecountmobspawn = self.framecountmobspawn + 1

            if self.framecountmobspawn > 500:
                self.mobspawner(mob_group)
                self.framecountmobspawn = 0

            self.walk()
            dx, dy = dx / dist, dy / dist 
            self.rect.x += dx * self.speed[0]
            self.rect.y += dy * self.speed[1]


        #////////////////////////////////Animations//////////////////////////////////////////#
        # walking
        if self.isWalking == True and self.isAttacking == False and self.isDeath == False and self.isRun == False and self.isIdle == False:
            self.currentWalk += 0.2

            if self.currentWalk >= len(self.walkingLeftSprites):
                self.currentWalk = 0
                self.isWalking = False

            if(self.direction == 'r'):
                self.image = self.walkingRightSprites[int(self.currentWalk)]
            else:
                self.image = self.walkingLeftSprites[int(self.currentWalk)]

        # attacking
        elif self.isAttacking == True and self.isDeath == False:
            self.currentAttack += 0.3

            if self.currentAttack >= len(self.attackLeftSprites):
                self.currentAttack = 0
                self.isAttacking = False
                
            if(self.direction == 'r'):
                self.image = self.attackRightSprites[int(self.currentAttack)]
            else:
               self.image = self.attackLeftSprites[int(self.currentAttack)] 

        # idle
        elif self.isWalking == False and self.isDeath == False:
            self.currentIdle += 0.3

            if self.currentIdle >= len(self.idleLeftSprites):
                self.currentIdle = 0
                
            if(self.direction == 'r'):
                self.image = self.idleRightSprites[int(self.currentIdle)]
            else:
                self.image = self.idleLeftSprites[int(self.currentIdle)]

        # death
        elif self.isDeath == True:
            self.currentDeath += 0.4
            
            if self.currentDeath >= len(self.deathLeftSprites):
                self.currentDeath = len(self.deathLeftSprites) - 1
                self.isDeath = False
                self.selfRemove(boss_group)

            if(self.direction == 'r'):
                self.image = self.deathRightSprites[int(self.currentDeath)]
            else:
                self.image = self.deathLeftSprites[int(self.currentDeath)]
        # run
        elif self.isRun == True:
            self.currentRun += 0.4
            if self.currentRun >= len(self.runLeftSprites):
                self.currentRun = len(self.runLeftSprites) - 1
                self.isRun = False
            if(self.direction == 'r'):
                self.image = self.runRightSprites[int(self.currentRun)]
            else:
                self.image = self.runLeftSprites[int(self.currentRun)]

        # hit
        if self.isHit == True and self.isDeath == False:
            self.currentHit += 0.4
            if self.currentHit >= 8:
                self.currentHit = 0
                self.isHit = False
                self.health -= self.playerDamage
                if self.health <= 0:
                    self.death()
            
        #////////////////////////////////Animations//////////////////////////////////////////#

    # remove sprite
    def selfRemove(self, boss_group):
        boss_group.remove(self)

    #////////////////////////////////Animation Methods//////////////////////////////////////////#
    # attacking
    def attack(self):
        self.isAttacking = True

    # hit
    def idle(self):
        self.isIdle = True

    # death
    def death(self):
        self.isDeath = True

    # walk
    def walk(self):
        self.isWalking = True

    # hit
    def hit(self):
        self.isHit = True
    #////////////////////////////////Animation Methods//////////////////////////////////////////#
    
    
    # mob spawn attack
    def mobspawner(self,mob_group):
        for x in range (4):
            mob_group.add(Mob1("Skeleton\walktile000.png", 3, 1, [2,2]))
        position = len(mob_group)
        mob_group.sprites()[position-4].rect.center = self.rect.center
        mob_group.sprites()[position-4].speed = [3,3]
        mob_group.sprites()[position-3].rect.center = self.rect.center
        mob_group.sprites()[position-3].speed = [-3,3]
        mob_group.sprites()[position-3].direction = 'l'
        mob_group.sprites()[position-2].rect.center = self.rect.center
        mob_group.sprites()[position-2].speed = [3,-3]
        mob_group.sprites()[position-1].rect.center = self.rect.center
        mob_group.sprites()[position-1].speed = [-3,-3]
        mob_group.sprites()[position-1].direction = 'l'