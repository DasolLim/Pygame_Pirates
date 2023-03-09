import pygame
pygame.init()

# Initialize the game
bg_img = pygame.image.load('backgroundimage.png')
bg_img = pygame.transform.scale(bg_img,(1280,780))
bg_rect = bg_img.get_rect()

screen = pygame.display.set_mode((bg_rect.width, bg_rect.height))
screen_rect = screen.get_rect()


# Initialize the first beach scene image
beachImg = pygame.image.load('sceneimage.png')
beachImg = pygame.transform.scale(beachImg,(1280,780))
beach_rect = beachImg.get_rect()

def render():
    screen.blit(bg_img,bg_rect)
    pygame.display.flip()

render()
running = True
FPS = 60
clock = pygame.time.Clock()
# gameloop
while running:
    clock.tick(FPS)
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # David once you implement start button changes
        # CHANGE THIS EVENT HERE so that once start is clicked it performs this
        if event.type == pygame.KEYDOWN:
            bg_img = beachImg

    #render
    render()


pygame.quit()