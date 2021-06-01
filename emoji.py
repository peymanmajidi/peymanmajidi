import pygame, sys, os, random
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

class Emoji:
    global space
    global screen
    def __init__(self, pos):
        self.image = get_random_emoji_images()
        self.body = pymunk.Body(1,1, body_type= pymunk.Body.DYNAMIC)
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, int(self.image.get_height()/2))
        space.add(self.body, self.shape)
    def draw(self):
        x = int(self.body.position.x)
        y = int(self.body.position.y)
        emoji_rec = self.image.get_rect(center= (x,y))
        screen.blit(self.image, emoji_rec)
           
def get_random_emoji_images():
    path = './emojis/'
    images = os.listdir(path)
    rand = random.randint(0,len(images)-1)
    return pygame.image.load(path+"/"+ images[rand])
    
    
        
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

emojis = []

circles = []
circles.append(object_circle(space,(500+5,500-5),100))
circles.append(object_circle(space,(150,700),200))

rects = []
rects.append(object_rect(space, (0,600), 800, 100))





while True:
    # track events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            emojis.append(Emoji(pos= event.pos))
           
            
            
    # while body   
    screen.fill((217,217,217))
    space.step(1/50)
    
    for emoji in emojis:
        emoji.draw()

    draw_playground(circles, rects)
    
    pygame.display.update()
    clock.tick(FPS) # frame per sec
    