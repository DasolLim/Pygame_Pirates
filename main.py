# imports
import pygame,gameSprites

# initializing pygame
pygame.init()

# initializng mixer
pygame.mixer.init()

# //////////////////////////////////////Images & Rectangle Initializations////////////////////////////////////// #
# initialize starting image
mainmenu_image = pygame.image.load('Scenes/backgroundimage.png')
mainmenu_image = pygame.transform.scale(mainmenu_image, (1280, 780))
mainmenu_rect = mainmenu_image.get_rect()

# initializing current image
current_img = None
current_rect = None

# initialize cursor image
cursor_img = pygame.image.load('Scenes/cursor.png')
cursor_img = pygame.transform.scale(cursor_img, (25, 25))
cursor_rect = cursor_img.get_rect()
pygame.mouse.set_visible(False)

# initializing screen
screen = pygame.display.set_mode((mainmenu_rect.width, mainmenu_rect.height))
screen_rect = screen.get_rect()

# initialize text background
textBackground_image = pygame.image.load('Scenes/textBackground.png')
textBackground_image = pygame.transform.scale(textBackground_image, (300, 860))
textBackground_rect = textBackground_image.get_rect()
textBackground_rect.bottomright = screen_rect.bottomright

# initialize beach scene
beachImg = pygame.image.load('Scenes/sceneimage.png')
beachImg = pygame.transform.scale(beachImg, (1280, 780))
beach_rect = beachImg.get_rect()

# initialize forest scene
forestImg = pygame.image.load('Scenes/forestScene.png')
forestImg = pygame.transform.scale(forestImg, (1280, 780))
forest_rect = forestImg.get_rect()

# initialize cave image
caveImg = pygame.image.load('Scenes/caveScene.png')
caveImg = pygame.transform.scale(caveImg, (1280, 780))
cave_rect = caveImg.get_rect()

# arrow image
arrowImg = pygame.image.load('Scenes/arrow.png')
arrowImg = pygame.transform.scale(arrowImg, (150, 100))
arrow_rect = arrowImg.get_rect()
arrow_rect.right = screen_rect.right
arrow_rect.centery = screen_rect.centery

# initialize death scenes
skeletonDeathImg = pygame.image.load('Death/skeletonDeath.png')
goblinDeathImg = pygame.image.load('Death/goblinDeath.png')
bossDeathImg = pygame.image.load('Death/bossDeath.png')
deathImgRect = skeletonDeathImg.get_rect()
deathImgRect.center = screen_rect.center
selectedDeathImg = None

# initializing win scene
treasureImg = pygame.image.load('Scenes/Win.jpg')
treasureImg = pygame.transform.scale(treasureImg, (1280, 780))
treasure_rect = treasureImg.get_rect()

# initializing coin image
coinImg = pygame.image.load('Scenes/coin_100x94.png')
coinImg = pygame.transform.scale(coinImg, (60, 60))
coin_rect = coinImg.get_rect()

# initializing heart image
heartImg = pygame.image.load('Scenes/Heart.png')
heartImg = pygame.transform.scale(heartImg, (65, 65))
heart_rect = heartImg.get_rect()

# defining width/height of buttons
width = 395
height = 135

# creating rectangle for start button
startRect = pygame.Rect(415, 225, width, height)

# creating rectangle for exit button
exitRect = pygame.Rect(415, 425, width, height)
exitRectFinal = pygame.Rect(882, 637, 334, 91)

# creating rectangle for menu start button
menuStartRect = pygame.Rect(700, 575, 165, 50)

# creating rectangle for menu exit button
menuExitRect = pygame.Rect(410, 575, 165, 50)

# player speed upgrade rectangle
speedRect = pygame.Rect(550, 300, 45, 50)

# player health upgrade rectangle
healthRect = pygame.Rect(550, 435, 45, 50)

# player attack speed upgrade rectangle
damageRect = pygame.Rect(845, 300, 45, 50)

# player rectangle
luckRect = pygame.Rect(845, 435, 45, 50)

# deathButton rectangle
deathButton = pygame.Rect(486,440,147,69)

# //////////////////////////////////////Shop Initializations//////////////////////////////////////#
#black Colour initally, switches to green once item purchased
barColour = (0, 0, 0)  # Black
upgradeColour = (0, 255, 0)

#creating menu speed item bar
speedBarRect = pygame.Rect(435, 313, 115, 31)
spdUpgradeRect = pygame.Rect(435, 313, 0, 31)
spdUpgradeCount = 0
spdCost = 5

# creating menu health item bar
# 23.75  -- Each increment width
healthBarRect = pygame.Rect(455, 447, 101, 31)
hlthUpgradeRect = pygame.Rect(455, 447, 0, 31)
hlthUpgradeCount = 0
hlthCost = 5

# creating menu damage item bar
# 25.25 -- Each increment width
damageBarRect = pygame.Rect(738, 312, 107, 31)
dmgUpgradeRect = pygame.Rect(738, 312, 0, 31)
dmgUpgradeCount = 0
dmgCost = 5

# creating menu luck item bar
# 25.50 -- Each increment width
luckBarRect = pygame.Rect(738, 445, 108, 31)
luckUpgradeRect = pygame.Rect(738, 445, 0, 31)
luckUpgradeCount = 0
luckCost = 5

# creating upgrade counts
shopUpgradeCounts = [spdUpgradeCount, hlthUpgradeCount,
                     dmgUpgradeCount, luckUpgradeCount]
shopUpgradeCosts = [spdCost, hlthCost, dmgCost, luckCost]
shopBarRects = [speedBarRect, healthBarRect, damageBarRect, luckBarRect]
shopUpgradeRects = [spdUpgradeRect, hlthUpgradeRect,
                    dmgUpgradeRect, luckUpgradeRect]
maxUpgradeCount = 4

# initialize shop scene
shopImg = pygame.image.load('Scenes/menu.png')
shopImg = pygame.transform.scale(shopImg, (750, 750))
shop_rect = shopImg.get_rect()
shop_rect.center = screen_rect.center

# initializing font
pygame.font.init()
blackColour = (0, 0, 0)
font = pygame.font.SysFont("verdana", 45)
shopFont = pygame.font.SysFont("verdana", 20)
descriptionFont = pygame.font.SysFont("verdana", 17)
shopText = font.render("SHOP", False, blackColour)

# initializing upgrade attribute texts for the shop
spdMenuText = shopFont.render("SPEED UPGRADE: +0.5", False, blackColour)
hlthMenuText = shopFont.render("HEALTH UPGRADE: +1", False, blackColour)
dmgMenuText = shopFont.render("DAMAGE UPGRADE: +1", False, blackColour)
luckMenuText = shopFont.render("LUCK UPGRADE: +10%", False, blackColour)

# description upgrade attribute texts for the shop
spdDescript = descriptionFont.render(
    "Increases your movement speed", False, blackColour)
hlthDescript = descriptionFont.render(
    "Increases your health", False, blackColour)
dmgDescript = descriptionFont.render(
    "Increases the damage you deal", False, blackColour)
luckDescript = descriptionFont.render(
    "Increases mob coin drop multiplier", False, blackColour)

# //////////////////////////////////////Initialize Groups&Variables//////////////////////////////////////#
# creating player sprite group
player_group = pygame.sprite.Group()

# creating mob sprite group
mob_group = pygame.sprite.Group()

# creating mob sprite group
boss_group = pygame.sprite.Group()

# creating coin item sprite group
coinItem_group = pygame.sprite.Group()

# boolean flags
deathPlaying = False
loadPlaying = True
shopPlaying = False
bossPlaying = False
running = True
win = False

# FPS
FPS = 60

# setting clock
clock = pygame.time.Clock()

# setting collision
scene = 'beach'

# initializing counts
stage = 0
coinCount = 0
speedCount = [5,5]
damageCount = 1
luckCount = 0
healthCount = 3
extra_distance = 0

# //////////////////////////////////////Methods//////////////////////////////////////#
# initializing player sprite
def initializePlayer():
    global player_group
    if player_group:
        player_group.empty()
    num_of_player = 1
    for x in range(num_of_player):
        player_group.add(gameSprites.Player(
            "Pirate/1_entity_000_IDLE_000.png", healthCount, damageCount, speedCount, 500, luckCount))
    global player
    player = player_group.sprites()[0]

# initializing coin sprite
def initializeCoinItem(pos_x, pos_y):
    global coinItem_group
    if coinItem_group:
        coinItem_group.empty()
    num_of_coins = 1
    for i in range(num_of_coins):
        coinItem_group.add(gameSprites.Coin("Scenes\coinItemImage.png", pos_x, pos_y))

# initializing mob sprite
def initializeMobs():
    global mob_group
    if mob_group:
        mob_group.empty()
    num_of_mobs1 = 5
    num_of_mobs2 = 5
    for x in range(num_of_mobs1):
        mob_group.add(gameSprites.Mob1(
            "Skeleton\walktile000.png", 3, 1, [2, 2]))
    if scene == 'forest':
        for x in range(num_of_mobs2):
            mob_group.add(gameSprites.Mob2(
                "Goblin/runtile000.png", 6, 1, [2.5, 2.5]))
            
# initialize boss
def initializeBoss():
    global boss_group
    if boss_group:
        boss_group.empty()
    num_of_mobs = 1
    for x in range(num_of_mobs):
        boss_group.add(gameSprites.Boss(
            "Boss\walktile000.png", 50, 2, [2.5, 2.5]))
        
# render images
def render():

    # adding background image
    screen.blit(current_img, current_rect)

    if not mob_group and not boss_group and not scene == 'treasure':
        screen.blit(arrowImg, arrow_rect)

    # checking if on start screen
    if not loadPlaying:

        # initializing respective text
        global coinCount
        coinCount = player_group.sprites()[0].coins
        coinCountText = shopFont.render(str(coinCount), False, (255, 255, 255))
        healthCount = player_group.sprites()[0].health
        healthCountText = shopFont.render(
            str(healthCount), False, (255, 255, 255))
        
        if not win and not deathPlaying:
            # displaying coin/health background
            screen.blit(textBackground_image, (1125, 570))
            # displaying coin info
            screen.blit(coinCountText, (1220, 735))
            screen.blit(coinImg, (1160, 720))
            # displaying heart info
            screen.blit(healthCountText, (1220, 685))
            screen.blit(heartImg, (1160, 665))
            # drawing player sprite
            player_group.draw(screen)

        # displaying player 
        if not shopPlaying:
            mob_group.update(mob_group, player_group.sprites()[0], coinItem_group)
            player_group.update()
        if not deathPlaying:
            # displaying mob sprites
            mob_group.draw(screen)

        # displaying respective death image
        if deathPlaying:
            global selectedDeathImg
            if(player_group.sprites()[0].whoKilled=="skeleton"):
                selectedDeathImg = skeletonDeathImg
            elif(player_group.sprites()[0].whoKilled=="goblin"):
                selectedDeathImg = goblinDeathImg
            elif(player_group.sprites()[0].whoKilled=="boss"):
                selectedDeathImg = bossDeathImg
            player_group.draw(screen)
            mob_group.draw(screen)
            if bossPlaying:
                boss_group.draw(screen)
            screen.blit(selectedDeathImg,deathImgRect)
    
        # displaying coin sprite
        coinItem_group.draw(screen)

        # displaying shop
        if shopPlaying and not deathPlaying:
            screen.blit(shopImg, shop_rect)

            # adding rectangles
            pygame.draw.rect(screen, upgradeColour, shopUpgradeRects[0])
            pygame.draw.rect(screen, upgradeColour, shopUpgradeRects[1])
            pygame.draw.rect(screen, upgradeColour, shopUpgradeRects[2])
            pygame.draw.rect(screen, upgradeColour, shopUpgradeRects[3])

            # rendering text
            spdCostText = shopFont.render(
                "COST: " + str(shopUpgradeCosts[0]), False, blackColour)
            hlthCostText = shopFont.render(
                "COST: " + str(shopUpgradeCosts[1]), False, blackColour)
            dmgCostText = shopFont.render(
                "COST: " + str(shopUpgradeCosts[2]), False, blackColour)
            luckCostText = shopFont.render(
                "COST: " + str(shopUpgradeCosts[3]), False, blackColour)
            
            # shop title text
            screen.blit(shopText, (580, 55))

            # shop cost texts
            screen.blit(spdCostText, (400, 270))
            screen.blit(dmgCostText, (705, 270))
            screen.blit(hlthCostText, (400, 403))
            screen.blit(luckCostText, (705, 403))

            # displays menu text once player hovers over upgrade buttons
            if 595 > pygame.mouse.get_pos()[0] > 550 and 350 > pygame.mouse.get_pos()[1] > 300:
                screen.blit(spdMenuText, (530, 515))
                screen.blit(spdDescript, (500, 540))
            if 595 > pygame.mouse.get_pos()[0] > 550 and 495 > pygame.mouse.get_pos()[1] > 435:
                screen.blit(hlthMenuText, (525, 515))
                screen.blit(hlthDescript, (550, 540))
            if 890 > pygame.mouse.get_pos()[0] > 845 and 350 > pygame.mouse.get_pos()[1] > 300:
                screen.blit(dmgMenuText, (525, 515))
                screen.blit(dmgDescript, (510, 540))
            if 890 > pygame.mouse.get_pos()[0] > 845 and 495 > pygame.mouse.get_pos()[1] > 435:
                screen.blit(luckMenuText, (530, 515))
                screen.blit(luckDescript, (490, 540))

        # updating and drawing boss sprite 
        if bossPlaying and not shopPlaying:
            boss_group.update(player_group.sprites()[
                              0].rect, boss_group, mob_group)
            if not deathPlaying:
                boss_group.draw(screen)



    # checking if mouse is within game window
    if pygame.mouse.get_focused() == True and loadPlaying or shopPlaying or win or deathPlaying:
        # adding mouse image to screen
        screen.blit(cursor_img, pygame.mouse.get_pos())

    # refreshing screen
    pygame.display.flip()

# musicPlayer
def musicPlayer(music, vol=0.2, loop=0, initialPlay=0):

    # checking initial play
    if initialPlay:
        # loading music
        pygame.mixer.music.load(music)
    else:
        # changing music
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(music)

    # setting volume
    pygame.mixer.music.set_volume(vol)

    # looping music
    pygame.mixer.music.play(loop)

# building the scenes
def sceneBuilder(newScene):
    global current_img
    global current_rect
    global scene
    global bossPlaying

    # determining scene
    if (newScene == 'shop'):
        musicPlayer('Music/shopMusic.mp3', loop=-1)
        return
    if (newScene == 'mainMenu'):
        current_img = mainmenu_image
        musicPlayer('Music/menuMusic.mp3', loop=-1, initialPlay=1)
    elif (newScene == 'beach'):
        if stage == 0:
            musicPlayer('Music/pirateArr.mp3')
        current_img = beachImg
        scene = 'beach'
    elif (newScene == 'forest'):
        current_img = forestImg
        scene = 'forest'
    elif (newScene == 'cave'):
        current_img = caveImg
        scene = 'cave'
        initializeBoss()
        musicPlayer('Music/bossMusic.mp3', vol=0.3)
    elif (newScene == 'treasure'):
        current_img = treasureImg
        scene = 'treasure'
    current_rect = current_img.get_rect()

    # initializing sprites
    initializePlayer()
    initializeMobs()

    # removing coin sprites
    coinItem_group.empty()

    # specific condions for certain scenes
    if newScene == "cave":
        mob_group.empty()
        player_group.sprites()[0].rect.bottom = 170
        player_group.sprites()[0].rect.left = 260
        bossPlaying = True
    elif newScene == 'treasure':
        mob_group.empty()
        boss_group.empty()

# collisionPicker
def collisionPicker(scene):
    if scene == 'beach':
        player_group.sprites()[0].collisionBeach()
        for sprites in mob_group.sprites():
            sprites.collisionBeach()

    if scene == 'forest':
        player_group.sprites()[0].collisionForest()
        for sprites in mob_group.sprites():
            sprites.collisionForest()

    if scene == 'cave':
        player_group.sprites()[0].collisionCave()
        for sprites in mob_group.sprites():
            sprites.collisionCave()

    if scene == 'treasure':
        None

# player/mob collisions
def collisions():
    
    # coin collisions
    myDict = pygame.sprite.groupcollide(
        player_group, coinItem_group, False, True)
    
    if myDict:
        player_group.sprites()[0].coins += 1

    # player/mob collisions
    myDict = pygame.sprite.groupcollide(
        player_group, mob_group, False, False)
    
    if myDict:
        hitMobs = myDict.get(player_group.sprites()[0])
    
    if player_group.sprites()[0].isAttacking and myDict:
        for x in hitMobs:

            if x.type == "goblin":
                global extra_distance
                extra_distance = 70
            else:
                extra_distance = 0

            if player_group.sprites()[0].direction == 'r' and player_group.sprites()[0].rect.centerx+extra_distance < x.rect.right:
                x.playerDamage = player_group.sprites()[0].damage
                x.hit()
            elif player_group.sprites()[0].direction == 'l' and player_group.sprites()[0].rect.centerx-extra_distance > x.rect.left:
                x.playerDamage = player_group.sprites()[0].damage
                x.hit()

    if myDict:
        for x in hitMobs:
            if player_group.sprites()[0].direction == 'r' and x.direction == 'r' and x.rect.right < player_group.sprites()[0].rect.right:
                x.attack()
            elif player_group.sprites()[0].direction == 'l' and x.direction == 'l' and x.rect.left > player_group.sprites()[0].rect.left:
                x.attack()

    # player/boss collisions
    myDict = pygame.sprite.groupcollide(
        player_group, boss_group, False, False)
    
    if myDict:
        hitBoss = myDict.get(player_group.sprites()[0])

    if boss_group and boss_group.sprites()[0].isIdle and myDict and player_group.sprites()[0].isAttacking:
        for x in hitBoss:
            x.playerDamage = player_group.sprites()[0].damage
            x.hit()

    if boss_group and pygame.sprite.collide_rect(player,boss_group.sprites()[0]) and boss_group.sprites()[0].framecount == 20:
        player.health -= boss_group.sprites()[0].damage
        player.hit()
        if player.health > 0:
            player.whoKilled = boss_group.sprites()[0].type

    if(player.health<=0):
        global deathPlaying
        deathPlaying = True

# reset shop upgrades
def resetShop():
    shopUpgradeRects[0].width = 0
    shopUpgradeRects[1].width = 0
    shopUpgradeRects[2].width = 0
    shopUpgradeRects[3].width = 0
    shopUpgradeCosts[0] = 5
    shopUpgradeCosts[1] = 5
    shopUpgradeCosts[2] = 5
    shopUpgradeCosts[3] = 5
    shopUpgradeCounts[0] = 0
    shopUpgradeCounts[1] = 0
    shopUpgradeCounts[2] = 0
    shopUpgradeCounts[3] = 0

# //////////////////////////////////////Main Game Loop//////////////////////////////////////#
# initalizing main menu
sceneBuilder("mainMenu")

# rendering
render()

# gameloop
while running:

    # setting fps
    clock.tick(FPS)

    # event loop
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        # quitting event
        if event.type == pygame.QUIT:
            running = False

        # open shop event with escape key
        if keys[pygame.K_ESCAPE] and not loadPlaying and not shopPlaying:
            sceneBuilder("shop")
            shopPlaying = True

        # button start and exit
        if event.type == pygame.MOUSEBUTTONDOWN:
            (posX, posY) = pygame.mouse.get_pos()

            # checking collide point of mouse with start button
            if startRect.collidepoint(posX, posY) and loadPlaying:
                loadPlaying = False
                coinCount = 0
                speedCount = [5,5]
                damageCount = 1
                luckCount = 0
                healthCount = 3
                sceneBuilder('beach')

            # checking collide point of mouse with exit button
            if exitRect.collidepoint(posX, posY) and loadPlaying:
                running = False

            # death screen button
            if deathButton.collidepoint(posX, posY) and deathPlaying:
                deathPlaying = False
                sceneBuilder("mainMenu")
                resetShop()
                stage = 0
                loadPlaying = True
                bossPlaying = False

            # ending game
            if exitRectFinal.collidepoint(posX, posY) and win:
                running = False

            # resume / start the game on start menu button press
            if menuStartRect.collidepoint(posX, posY) and shopPlaying:
                shopPlaying = False
                pygame.mixer.music.stop()

            # exit to main screen on exit menu button press
            if menuExitRect.collidepoint(posX, posY) and shopPlaying:
                shopPlaying = False
                loadPlaying = True
                resetShop()
                stage = 0
                sceneBuilder("mainMenu")
                bossPlaying = False

            # speed upgrade
            if speedRect.collidepoint(posX, posY) and shopPlaying:

                if shopUpgradeCounts[0] < maxUpgradeCount and coinCount >= shopUpgradeCosts[0]:
                    shopUpgradeCounts[0] += 1
                    player_group.sprites()[0].coins -= shopUpgradeCosts[0]
                    shopUpgradeRects[0].width += 28.75
                    shopUpgradeCosts[0] += 5
                    speedCount = [speedCount[0] + 0.5, speedCount[1] + 0.5]
                    player_group.sprites()[0].speed = speedCount
                    if shopUpgradeCounts[0] == 4:
                        shopUpgradeCosts[0] = "Sold out!"
        

            # health upgrade
            if healthRect.collidepoint(posX, posY) and shopPlaying:

                if shopUpgradeCounts[1] < maxUpgradeCount and coinCount >= shopUpgradeCosts[1]:
                    shopUpgradeCounts[1] += 1
                    player_group.sprites()[0].coins -= shopUpgradeCosts[1]
                    shopUpgradeRects[1].width += 25.25
                    shopUpgradeCosts[1] += 5
                    player.maxHealth += 1
                    if shopUpgradeCounts[1] == 4:
                        shopUpgradeCosts[1] = "Sold out!"

            # damage upgrade
            if damageRect.collidepoint(posX, posY) and shopPlaying:

                if shopUpgradeCounts[2] < maxUpgradeCount and coinCount >= shopUpgradeCosts[2]:
                    shopUpgradeCounts[2] += 1
                    player_group.sprites()[0].coins -= shopUpgradeCosts[2]
                    shopUpgradeRects[2].width += 26.75
                    shopUpgradeCosts[2] += 5
                    damageCount += 1
                    player_group.sprites()[0].damage = damageCount
                    if shopUpgradeCounts[2] == 4:
                        shopUpgradeCosts[2] = "Sold out!"

            # luck upgrade
            if luckRect.collidepoint(posX, posY) and shopPlaying:

                if shopUpgradeCounts[3] < maxUpgradeCount and coinCount >= shopUpgradeCosts[3]:
                    shopUpgradeCounts[3] += 1
                    player_group.sprites()[0].coins -= shopUpgradeCosts[3]
                    shopUpgradeRects[3].width += 27
                    shopUpgradeCosts[3] += 5
                    luckCount += 0.1
                    player_group.sprites()[0].luck = luckCount
                    if shopUpgradeCounts[3] == 4:
                        shopUpgradeCosts[3] = "Sold out!"

        # spacebar click for attack
        if keys[pygame.K_SPACE] and not loadPlaying and not shopPlaying:
            player_group.sprites()[0].attack()

    # player movement
    if not shopPlaying and player_group.sprites()[0].isDeath == False:

        if keys[pygame.K_RIGHT]:
            player_group.sprites()[0].walk()
            player_group.sprites()[0].rect.x += speedCount[0]
            player_group.sprites()[0].speed = speedCount
            player_group.sprites()[0].direction = 'r'

        if keys[pygame.K_LEFT]:
            player_group.sprites()[0].walk()
            player_group.sprites()[0].rect.x -= speedCount[0]
            player_group.sprites()[0].speed = speedCount
            player_group.sprites()[0].direction = 'l'

        if keys[pygame.K_UP]:
            player_group.sprites()[0].walk()
            player_group.sprites()[0].rect.y -= speedCount[0]
            player_group.sprites()[0].speed = speedCount

        if keys[pygame.K_DOWN]:
            player_group.sprites()[0].walk()
            player_group.sprites()[0].rect.y += speedCount[0]
            player_group.sprites()[0].speed = speedCount

    # ///////////////////////////#
    # if conditions are met and player exits screen through right side
    if keys[pygame.K_f]:
        sceneBuilder("forest")
    if keys[pygame.K_c]:
        sceneBuilder('cave')
        bossPlaying = True
    # if conditions are met for game completion
    if keys[pygame.K_t]:
        sceneBuilder('treasure')
        win = True
    if keys[pygame.K_b]:
        sceneBuilder('beach')
    if keys[pygame.K_4]:
        mob_group.empty()
        boss_group.empty()
        coinItem_group.empty()
    #/////////////////////////////////////#
    
    # advancing to next stage
    if not mob_group and not boss_group and not scene == 'treasure':

        if player_group.sprites()[0].rect.right >= screen_rect.right:
            healthCount = player_group.sprites()[0].maxHealth

            if stage < 5:
                stage += 1
                sceneBuilder('beach')
            elif stage < 10:
                sceneBuilder('forest')
                stage += 1
            elif stage == 10:
                sceneBuilder('cave')
                stage += 1
            else:
                sceneBuilder('treasure')
                win = True

    # player boundaries
    collisionPicker(scene)

    # player/mob collisions
    collisions()

    # render
    render()

    # begining level music
    if not pygame.mixer.music.get_busy():
        musicPlayer('Music/levelMusic.mp3', 0.01, -1)

# exiting pygame
pygame.quit()