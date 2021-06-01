import pygame, sys
import pymunk

# constants
SCREEN_SIZE = (800,800)
FPS = 120
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
EMOJI = pygame.image.load('emoji.png')
GRAVITY = 250

def create_apple(space,pos):
    body = pymunk.Body(1,1, body_type= pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, int(EMOJI.get_height()/2))
    space.add(body, shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        x = int(apple.body.position.x)
        y = int(apple.body.position.y)
        # pygame.draw.circle(screen, RED,  (x,y),80)
        emoji_rec = EMOJI.get_rect(center= (x,y))
        screen.blit(EMOJI, emoji_rec)
        
        
def object_circle(space,pos, size):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, size)
    space.add(body, shape)
    return shape

def object_rect(space,pos, width, height):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    vs = [pos, (width, pos[1]), (width, height), (pos[0], height)]
    shape = pymunk.Poly(body, vs)
    space.add(body, shape)
    return shape

     

def draw_playground(circles, rects):
    for circle in circles:
        x = int(circle.body.position.x)
        y = int(circle.body.position.y)
        pygame.draw.circle(screen, WHITE,  (x,y),circle.radius)   
    for rect in rects:
        x = int(rect.body.position.x)
        y = int(rect.body.position.y)
        pygame.draw.rect(screen, GREEN,  (0,600+100, 800, 100))



# pymunk setup
space = pymunk.Space()
space.gravity = (0,GRAVITY)

# pygame setup
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

apples = []
# apples.append(create_apple(space, (100, 10)))

circles = []
circles.append(object_circle(space,(500+5,500-5),100))
circles.append(object_circle(space,(150,700),200))

rects = []
# rects.append(object_rect(space, (0,600), 800, 100))





while True:
    # track events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space, event.pos))
            
            
            
    # while body   
    screen.fill((217,217,217))
    space.step(1/50)
    draw_apples(apples)
    draw_playground(circles, rects)
    
    pygame.display.update()
    clock.tick(FPS) # frame per sec
    