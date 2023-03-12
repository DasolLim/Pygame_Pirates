import pygame
pygame.init()

# Initialize the game
bg_img = pygame.image.load('backgroundimage.png')
bg_img = pygame.transform.scale(bg_img, (1280, 780))
bg_rect = bg_img.get_rect()

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
    screen.blit(bg_img, bg_rect)
    pygame.display.flip()
    # pygame.draw.rect(screen, color, startRect)
    # pygame.draw.rect(screen, color, startRect)


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
                bg_img = beachImg
            # exit the game when button is pressed
            if exitRect.collidepoint(x, y):
                running = False

    # render
    render()


pygame.quit()
