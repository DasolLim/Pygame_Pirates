#imports
import pygame, gameSprites

#initializing pygame
pygame.init()

#initializng mixer
pygame.mixer.init()

# Initialize the game
bg_img = pygame.image.load('backgroundimage.png')
bg_img = pygame.transform.scale(bg_img, (1280, 780))
bg_rect = bg_img.get_rect()

#Initialize cursor image
cursor_img = pygame.image.load('cursor.png')
cursor_img = pygame.transform.scale(cursor_img,(50,50))
cursor_rect = cursor_img.get_rect()
pygame.mouse.set_visible(False)
loadPlaying = True

screen = pygame.display.set_mode((bg_rect.width, bg_rect.height))
screen_rect = screen.get_rect()


# Initialize the first beach scene image
beachImg = pygame.image.load('sceneimage.png')
beachImg = pygame.transform.scale(beachImg, (1280, 780))
beach_rect = beachImg.get_rect()

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


#Initialize player image
player_img = pygame.image.load("Pirate_Sprite_100x100.png")
player_img_with_left_flip = pygame.transform.flip(player_img, True, False)
player_img_with_right_flip = player_img

# Creating Player Sprite
num_of_player = 1
player_group = pygame.sprite.Group()
for x in range (num_of_player):
    player_group.add(gameSprites.Player("Pirate_Sprite_100x100.png", 50, 50, 0, 0))

# Creating Mob Sprite
num_of_mobs = 5
mob_group = pygame.sprite.Group()
for x in range (num_of_mobs):
    mob_group.add(gameSprites.Mob("mob.png", 50, 50, [4,4]))

def render():

    # pygame.draw.rect(screen, color, startRect)
    screen.blit(bg_img,bg_rect)
    
    if not loadPlaying:
        screen.blit(player_img, player_group.sprites()[0].rect)
        
        # Drawing mobs on screen
        mob_group.update()
        mob_group.draw(screen)
        for sprites in mob_group.sprites():
            sprites.collision()

    #checking if mouse is within game window
    if pygame.mouse.get_focused() == True and loadPlaying:
        #adding mouse image to screen
        screen.blit(cursor_img,pygame.mouse.get_pos())

    #refreshing screen
    pygame.display.flip()

#musicPlayer
def musicPlayer(music,vol = 0.7,loop = 0,initialPlay = 0):

    if initialPlay:
        pygame.mixer.music.load(music) 
        
    else:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(music)
        
    pygame.mixer.music.set_volume(vol)
    pygame.mixer.music.play(loop)
    
    
render()
running = True
FPS = 60
clock = pygame.time.Clock()

#playing menu music
musicPlayer('menuMusic.mp3',loop = -1, initialPlay=1)

# gameloop
while running:
    
    clock.tick(FPS)

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            print(x, y)
            # start the game when button is pressed by moving to a different scene
            if startRect.collidepoint(x, y) and loadPlaying:
                loadPlaying=False
                bg_img = beachImg
                musicPlayer('pirateArr.mp3')
            
            # exit the game when button is pressed
            if exitRect.collidepoint(x, y) and loadPlaying:
                running = False

    #Player movement
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

    
    #Rough player boundaries
    player_group.sprites()[0].collision()

    # render
    render()

    #begining level music
    if not pygame.mixer.music.get_busy():
        musicPlayer('levelMusic.mp3', 0.01, -1)

    
pygame.quit()