import pygame, sys

SCREEN_SIZE = (800,800)
FPS = 120

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

while True:
    # track events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # while body
    screen.fill((217,217,217))
    pygame.display.update()
    clock.tick(FPS) # frame per sec
    