import pygame
pygame.init()

# Initialize the game
bg_img = pygame.image.load('backgroundimage.png')
bg_img = pygame.transform.scale(bg_img,(1280,780))
bg_rect = bg_img.get_rect()

screen = pygame.display.set_mode((bg_rect.width, bg_rect.height))
screen_rect = screen.get_rect()

#testing again
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

    #render
    render()


pygame.quit()