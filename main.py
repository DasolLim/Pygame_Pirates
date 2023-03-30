# imports
import pygame
import gameSprites
import time

# initializing pygame
pygame.init()

# initializng mixer
pygame.mixer.init()

# //////////////////////////////////////Images//////////////////////////////////////#

# initialize starting image
mainmenu_image = pygame.image.load('backgroundimage.png')
mainmenu_image = pygame.transform.scale(mainmenu_image, (1280, 780))
mainmenu_rect = mainmenu_image.get_rect()

# initializing current image
current_img = None
current_rect = None

# initialize cursor image
cursor_img = pygame.image.load('cursor.png')
cursor_img = pygame.transform.scale(cursor_img, (25, 25))
cursor_rect = cursor_img.get_rect()
pygame.mouse.set_visible(False)

# initializing screen
screen = pygame.display.set_mode((mainmenu_rect.width, mainmenu_rect.height))
screen_rect = screen.get_rect()

# initialize text background
textBackground_image = pygame.image.load('textBackground.png')
textBackground_image = pygame.transform.scale(textBackground_image, (300, 860))
textBackground_rect = textBackground_image.get_rect()
textBackground_rect.bottomright = screen_rect.bottomright

# initialize beach scene
beachImg = pygame.image.load('sceneimage.png')
beachImg = pygame.transform.scale(beachImg, (1280, 780))
beach_rect = beachImg.get_rect()

# initialize forest scene
forestImg = pygame.image.load('forestScene.png')
forestImg = pygame.transform.scale(forestImg, (1280, 780))
forest_rect = forestImg.get_rect()

# initialize cave image
caveImg = pygame.image.load('caveScene.png')
caveImg = pygame.transform.scale(caveImg, (1280, 780))
cave_rect = caveImg.get_rect()

# initialize shop scene
shopImg = pygame.image.load('menu.png')
shopImg = pygame.transform.scale(shopImg, (750, 750))
shop_rect = shopImg.get_rect()
shop_rect.center = screen_rect.center

# initializing treasure scene
treasureImg = pygame.image.load('treasure.jpg')
treasureImg = pygame.transform.scale(treasureImg, (1280, 780))
treasure_rect = treasureImg.get_rect()

# initializing coin image
coinImg = pygame.image.load('coin_100x94.png')
coinImg = pygame.transform.scale(coinImg, (65, 65))
coin_rect = coinImg.get_rect()

# initializing heart image
heartImg = pygame.image.load('Heart.png')
heartImg = pygame.transform.scale(heartImg, (65, 65))
heart_rect = heartImg.get_rect()

# defining width/height of buttons
width = 395
height = 135

# creating rectangle for start button
startRect = pygame.Rect(415, 225, width, height)

# creating rectangle for exit button
exitRect = pygame.Rect(415, 425, width, height)

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
# player _____ rectnagle
luckRect = pygame.Rect(845, 435, 45, 50)

# ////////////////////////////////////////////////////////// #
#            INITIALIZING GREY MENU ITEM BARS                #
# ////////////////////////////////////////////////////////// #

# Black Colour initally, switches to green once item purchased
barColour = (0, 0, 0)  # Black
upgradeColour = (0, 255, 0)
# creating menu speed item bar
# 27.25 -- Each increment width
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

shopUpgradeCounts = [spdUpgradeCount, hlthUpgradeCount,
                     dmgUpgradeCount, luckUpgradeCount]
shopUpgradeCosts = [spdCost, hlthCost, dmgCost, luckCost]
shopBarRects = [speedBarRect, healthBarRect, damageBarRect, luckBarRect]
shopUpgradeRects = [spdUpgradeRect, hlthUpgradeRect,
                    dmgUpgradeRect, luckUpgradeRect]
maxUpgradeCount = 4

# initializing font
pygame.font.init()
font = pygame.font.SysFont("arial", 30)

# /////////////////////////////////////////////////////////////////////////#
# USE THESE 2 LINES TO INCREMENT coinCount and REDRAW THE COIN TEXT
# coinCount += 1
# coinCountText = font.render(str(coinCount), False, (255,255,255))
# /////////////////////////////////////////////////////////////////////////#

# //////////////////////////////////////Initialize Methods//////////////////////////////////////#

# creating player sprite group
player_group = pygame.sprite.Group()
# creating mob sprite group
mob_group = pygame.sprite.Group()
# boolean flags
loadPlaying = True
shopPlaying = False
running = True
right = True
# FPS
FPS = 60
# setting clock
clock = pygame.time.Clock()
# collision
scene = 'beach'
# initializing counts
coinCount = 0
healthCount = 50

# initializing player sprite


def initializePlayer():
    global player_group
    if player_group:
        player_group.empty()
    num_of_player = 1
    for x in range(num_of_player):
        player_group.add(gameSprites.Player(
            "Pirate_Sprite_100x100.png", 50, 50, 0, 100))


def initializeMobs():
    global mob_group
    if mob_group:
        mob_group.empty()
    num_of_mobs = 5
    for x in range(num_of_mobs):
        mob_group.add(gameSprites.Mob("mob.png", 50, 50, [2, 2]))

# render images


def render():
    # adding background image
    screen.blit(current_img, current_rect)
    # checking if on start screen
    if not loadPlaying:
        # initializing coin text
        global coinCount
        coinCount = player_group.sprites()[0].coins
        coinCountText = font.render(str(coinCount), False, (255, 255, 255))

        # initializing heart text
        global healthCount
        healthCount = player_group.sprites()[0].health

        # For now, remove the health count number text, replacing with heart images
        # healthCountText = font.render(str(healthCount), False, (255, 255, 255))

        # displaying coin/health background
        screen.blit(textBackground_image, (1125, 570))
        # displaying coin info
        screen.blit(coinCountText, (1230, 730))
        screen.blit(coinImg, (1160, 720))
        # displaying heart info
        # screen.blit(healthCountText, (1230, 680))
        screen.blit(heartImg, (1160, 665))
        # displaying player sprite
        screen.blit(player_group.sprites()[
                    0].image, player_group.sprites()[0].rect)
        # player_group.draw(screen)
        # displaying mobs
        if not shopPlaying:
            mob_group.update()
        mob_group.draw(screen)

    # //////////////////////////////////////// #
    if shopPlaying:
        screen.blit(shopImg, shop_rect)

        pygame.draw.rect(screen, upgradeColour, shopUpgradeRects[0])
        pygame.draw.rect(screen, upgradeColour, shopUpgradeRects[1])
        pygame.draw.rect(screen, upgradeColour, shopUpgradeRects[2])
        pygame.draw.rect(screen, upgradeColour, shopUpgradeRects[3])
    # //////////////////////////////////////// #

    # checking if mouse is within game window
    if pygame.mouse.get_focused() == True and loadPlaying or shopPlaying:
        # adding mouse image to screen
        screen.blit(cursor_img, pygame.mouse.get_pos())

    # refreshing screen
    pygame.display.flip()


# Reset shop upgrades
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

# musicPlayer


def musicPlayer(music, vol=0.7, loop=0, initialPlay=0):
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


def sceneBuilder(newScene):
    global current_img
    global current_rect
    global scene

    if (newScene == 'shop'):
        musicPlayer('shopMusic.mp3', 0.1, -1)
        return
    if (newScene == 'mainMenu'):
        current_img = mainmenu_image
        musicPlayer('menuMusic.mp3', loop=-1, initialPlay=1)
    elif (newScene == 'beach'):
        musicPlayer('pirateArr.mp3')
        current_img = beachImg
        scene = 'beach'
    elif (newScene == 'forest'):
        current_img = forestImg
        scene = 'forest'
        pygame.mixer.music.stop()
    elif (newScene == 'cave'):
        current_img = caveImg
        scene = 'cave'
        pygame.mixer.music.stop()
    elif (newScene == 'treasure'):
        current_img = treasureImg

    current_rect = current_img.get_rect()
    initializePlayer()
    initializeMobs()


# Initalizing methods and flags
sceneBuilder("mainMenu")

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


render()
# gameloop
while running:
    keys = pygame.key.get_pressed()
    # setting fps
    clock.tick(FPS)
    # event loop
    for event in pygame.event.get():
        # quitting event
        if event.type == pygame.QUIT:
            running = False

        # start screen event
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()

            # //////Debug///////#
            print(x, y)
            # //////////////////#

            # checking collide point of mouse with start button
            if startRect.collidepoint(x, y) and loadPlaying:
                loadPlaying = False
                sceneBuilder('beach')

            # checking collide point of mouse with exit button
            if exitRect.collidepoint(x, y) and loadPlaying:
                running = False

        # open shop event with escape key
        if keys[pygame.K_ESCAPE] and not loadPlaying and not shopPlaying:
            sceneBuilder("shop")
            shopPlaying = True

        # shop button start and exit
        if event.type == pygame.MOUSEBUTTONDOWN:
            (posX, posY) = pygame.mouse.get_pos()

            # resume / start the game on start menu button press
            if menuStartRect.collidepoint(posX, posY) and shopPlaying:
                shopPlaying = False
                pygame.mixer.music.stop()
            # exit to main screen on exit menu button press
            if menuExitRect.collidepoint(posX, posY) and shopPlaying:
                shopPlaying = False
                loadPlaying = True
                sceneBuilder("mainMenu")
                resetShop()

            if speedRect.collidepoint(posX, posY) and shopPlaying and coinCount >= shopUpgradeCosts[0]:
                shopUpgradeCounts[0] += 1
                player_group.sprites()[0].coins -= spdCost
                shopUpgradeCosts[0] += 5
                if shopUpgradeCounts[0] <= maxUpgradeCount:
                    shopUpgradeRects[0].width += 28.75
                    # Width needs to be incremented after
                else:
                    # Draw txt on screen saying Can't Upgrade anymore !
                    print("error")

            if healthRect.collidepoint(posX, posY) and shopPlaying and coinCount >= shopUpgradeCosts[1]:
                shopUpgradeCounts[1] += 1
                player_group.sprites()[0].coins -= spdCost
                shopUpgradeCosts[1] += 5
                if shopUpgradeCounts[1] <= maxUpgradeCount:
                    shopUpgradeRects[1].width += 25.25
                    # Width needs to be incremented after
                else:
                    # Draw txt on screen saying Can't Upgrade anymore !
                    print("error")

            if damageRect.collidepoint(posX, posY) and shopPlaying and coinCount >= shopUpgradeCosts[2]:
                shopUpgradeCounts[2] += 1
                player_group.sprites()[0].coins -= dmgCost
                shopUpgradeCosts[2] += 5

                if shopUpgradeCounts[2] <= maxUpgradeCount:
                    shopUpgradeRects[2].width += 26.75
                    # Width needs to be incremented after
                else:
                    # Draw txt on screen saying Can't Upgrade anymore !
                    print("error")

            if luckRect.collidepoint(posX, posY) and shopPlaying and coinCount >= shopUpgradeCosts[3]:
                shopUpgradeCounts[3] += 1
                player_group.sprites()[0].coins -= luckCost
                shopUpgradeCosts[3] += 5
                if shopUpgradeCounts[3] <= maxUpgradeCount:
                    shopUpgradeRects[3].width += 27
                    # Width needs to be incremented after
                else:
                    # Draw txt on screen saying Can't Upgrade anymore !
                    print("error")

    # player movement
    if not shopPlaying:
        if keys[pygame.K_RIGHT]:
            right = True
            player_group.sprites()[0].rect.x += 5
        if keys[pygame.K_LEFT]:
            right = False
            player_group.sprites()[0].rect.x -= 5
        if keys[pygame.K_UP]:
            player_group.sprites()[0].rect.y -= 5
        if keys[pygame.K_DOWN]:
            player_group.sprites()[0].rect.y += 5

        # player attack
        if keys[pygame.K_SPACE]:
            if right:
                player_group.sprites()[0].attack(True)
            else:
                player_group.sprites()[0].attack(False)
        if not keys[pygame.K_SPACE]:
            if right:
                player_group.sprites()[0].flipPlayer(True)
            else:
                player_group.sprites()[0].flipPlayer(False)

    # ///////////////////////////#
    # if conditions are met and player exits screen through right side
    if keys[pygame.K_f]:
        sceneBuilder("forest")

    # ///////////////////////////#

    # ///////////////////////////#
    # if conditions are met and player exits screen through right side
    if keys[pygame.K_c]:
        sceneBuilder('cave')

    # ///////////////////////////#

    # ///////////////////////////#
    # if conditions are met for game completion
    if keys[pygame.K_t]:
        sceneBuilder('treasure')

    if keys[pygame.K_b]:
        sceneBuilder('beach')

    # player boundaries
    collisionPicker(scene)

    # render
    render()

    # begining level music
    if not pygame.mixer.music.get_busy():
        musicPlayer('levelMusic.mp3', 0.01, -1)

# exiting pygame
pygame.quit()
