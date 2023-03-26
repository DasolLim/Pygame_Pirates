#imports
import pygame, gameSprites

#initializing pygame
pygame.init()

#initializng mixer
pygame.mixer.init()

#initialize starting image
bg_img = pygame.image.load('backgroundimage.png')
bg_img = pygame.transform.scale(bg_img, (1280, 780))
bg_rect = bg_img.get_rect()

#initialize cursor image
cursor_img = pygame.image.load('cursor.png')
cursor_img = pygame.transform.scale(cursor_img,(50,50))
cursor_rect = cursor_img.get_rect()
pygame.mouse.set_visible(False)

#boolean flag
loadPlaying = True

#initializing screen
screen = pygame.display.set_mode((bg_rect.width, bg_rect.height))
screen_rect = screen.get_rect()

#initialize beach scene
beachImg = pygame.image.load('sceneimage.png')
beachImg = pygame.transform.scale(beachImg, (1280, 780))
beach_rect = beachImg.get_rect()

#initialize forest scene
forestImg = pygame.image.load('forestScene.png')
forestImg = pygame.transform.scale(forestImg,(1280,780))
forest_rect = forestImg.get_rect()

#initialize cave image
caveImg = pygame.image.load('caveScene.png')
caveImg = pygame.transform.scale(caveImg,(1280,780))
cave_rect = caveImg.get_rect()

#initializing treasure image
treasureImg = pygame.image.load('treasure.jpg')
treasureImg = pygame.transform.scale(treasureImg,(1280,780))
treasure_rect = treasureImg.get_rect()

#initializing coin image
coinImg = pygame.image.load('coin_100x94.png')
coinImg = pygame.transform.scale(coinImg, (50,50))
coin_rect = coinImg.get_rect()

width = 395
height = 135
# start bound
# top left: x = 415, y = 225
# bottom right: x = 810, y = 360
# width = 395 & height = 135
startRect = pygame.Rect(415, 225, width, height)

# exit bound
# top left: x = 415, y = 425
# bottom right: x = 810, y = 560
# width = 395 & height = 135
exitRect = pygame.Rect(415, 425, width, height)

#initialize player image
player_img = pygame.image.load("Pirate_Sprite_100x100.png")
player_img_with_left_flip = pygame.transform.flip(player_img, True, False)
player_img_with_right_flip = player_img

#creating player Sprite
num_of_player = 1
player_group = pygame.sprite.Group()
for x in range (num_of_player):
    player_group.add(gameSprites.Player("Pirate_Sprite_100x100.png", 50, 50, 0, 0))

#initializing font
pygame.font.init()
font = pygame.font.SysFont("arial", 30)

#initializing coin text
coinCount = player_group.sprites()[0].coins
coinCountText = font.render(str(coinCount), False, (255, 255, 255))

#/////////////////////////////////////////////////////////////////////////#
# USE THESE 2 LINES TO INCREMENT coinCount and REDRAW THE COIN TEXT
# coinCount += 1
# coinCountText = font.render(str(coinCount), False, (255,255,255))
#/////////////////////////////////////////////////////////////////////////#

#creating mob sprite group
num_of_mobs = 5
mob_group = pygame.sprite.Group()
for x in range (num_of_mobs):
    mob_group.add(gameSprites.Mob("mob.png", 50, 50, [2,2]))

#render images
def render():

    #pygame.draw.rect(screen, color, startRect)

    #adding background image
    screen.blit(bg_img,bg_rect)
    
    #checking if on start screen
    if not loadPlaying:

        #displaying coin info
        screen.blit(coinCountText, (1230, 725))
        screen.blit(coinImg, (1180, 720))

        #displaying player sprite
        screen.blit(player_img, player_group.sprites()[0].rect)
        #player_group.draw(screen)
        
        #displaying mobs
        mob_group.update()
        mob_group.draw(screen)

    #checking if mouse is within game window
    if pygame.mouse.get_focused() == True:
        #adding mouse image to screen
        screen.blit(cursor_img,pygame.mouse.get_pos())

    #refreshing screen
    pygame.display.flip()

#musicPlayer
def musicPlayer(music,vol = 0,loop = 0,initialPlay = 0):
    #checking initial play
    if initialPlay:
        #loading music
        pygame.mixer.music.load(music) 
        
    else:
        #changing music
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(music)
    #setting volume    
    pygame.mixer.music.set_volume(vol)
    #looping music
    pygame.mixer.music.play(loop)

#collisionPicker
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

    
#rendering    
render()
#running to true
running = True
#FPS
FPS = 60
#setting clock
clock = pygame.time.Clock()
#collision
scene = 'beach'

#playing menu music
musicPlayer('menuMusic.mp3',loop = -1, initialPlay=1)

# gameloop
while running:
    #setting fps
    clock.tick(FPS)
    # event loop
    for event in pygame.event.get():

        #quitting event
        if event.type == pygame.QUIT:
            running = False

        #start screen event
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()

            #//////Debug///////#
            print(x, y)
            #//////////////////#

            #checking collide point of mouse with start button
            if startRect.collidepoint(x, y) and loadPlaying:
                loadPlaying=False
                bg_img = beachImg
                musicPlayer('pirateArr.mp3')
            
            #checking collide point of mouse with exit button
            if exitRect.collidepoint(x, y) and loadPlaying:
                running = False

    #player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_img = player_img_with_right_flip
        player_group.sprites()[0].rect.x += 5
    if keys[pygame.K_LEFT]:
        player_img = player_img_with_left_flip
        player_group.sprites()[0].rect.x -= 5
    if keys[pygame.K_UP]:
        player_group.sprites()[0].rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_group.sprites()[0].rect.y += 5

    #///////////////////////////#
    #if conditions are met and player exits screen through right side
    if keys[pygame.K_f]:
        bg_img = forestImg
        scene = 'forest'
    #///////////////////////////#

    #///////////////////////////#
    #if conditions are met and player exits screen through right side
    if keys[pygame.K_c]:
        bg_img = caveImg
        scene = 'cave'
    #///////////////////////////#

    #///////////////////////////#
    #if conditions are met for game completion
    if keys[pygame.K_t]:
        bg_img = treasureImg
        musicPlayer('ending.mp3')

    #player boundaries
    collisionPicker(scene)

    #render
    render()

    #begining level music
    if not pygame.mixer.music.get_busy():
        musicPlayer('levelMusic.mp3', 0.01, -1)

#exiting pygame    
pygame.quit()