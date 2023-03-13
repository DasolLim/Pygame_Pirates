#imports
import pygame, time

#initializing pygame
pygame.init()

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


#Initialize player image
player_img = pygame.image.load("Pirate_Sprite_100x100.png")
player_img_with_left_flip = pygame.transform.flip(player_img, True, False)
player_img_with_right_flip = player_img
player_rect = player_img.get_rect()
player_rect.center = bg_rect.center
player_speed = 5


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


def render():

    # pygame.draw.rect(screen, color, startRect)
    # pygame.draw.rect(screen, color, startRect)
    screen.blit(bg_img,bg_rect)
    
    if not loadPlaying:
        screen.blit(player_img,player_rect)

    #checking if mouse is within game window
    if pygame.mouse.get_focused() == True and loadPlaying:
        #adding mouse image to screen
        screen.blit(cursor_img,pygame.mouse.get_pos())

    #refreshing screen
    pygame.display.flip()


render()
running = True
FPS = 60
clock = pygame.time.Clock()
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
            if startRect.collidepoint(x, y):
                loadPlaying=False
                bg_img = beachImg
            # exit the game when button is pressed
            if exitRect.collidepoint(x, y):
                running = False

    #Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_img = player_img_with_right_flip
        player_rect.x +=5
    if keys[pygame.K_LEFT]:
        player_img = player_img_with_left_flip
        player_rect.x -=5
    if keys[pygame.K_UP]:
        player_rect.y -=5
    if keys[pygame.K_DOWN]:
        player_rect.y +=5
    
    #Rough player boundaries
    if player_rect.left < bg_rect.left:
        player_rect.left = bg_rect.left
    if player_rect.right > bg_rect.right:
        player_rect.right = bg_rect.right
    if player_rect.top < bg_rect.top:
        player_rect.top = bg_rect.top
    if player_rect.bottom > bg_rect.bottom:
        player_rect.bottom = bg_rect.bottom
    # render
    render()

    

pygame.quit()