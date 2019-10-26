import pygame

#Player Class-------------------------------------------------------------------
class player():
    def __init__(self,x,y,height,width) :
        self.x=x
        self.y=y
        self.height = height
        self.width = width
        self.velocity = 15

    def draw(self,WIN):
        BLUE=(0,0,255)
        if(self.x<=0):
            self.x=0
        if(self.x>=850):
            self.x=850
        pygame.draw.rect(WIN,BLUE,(self.x,self.y,150,20))
#-------------------------------------------------------------------------------

#Ball class---------------------------------------------------------------------
class ball():
    def __init__(self,x,y) :
        self.x=x
        self.y=y
        self.velocity = 30

    def draw(self,WIN):
        BLUE=(0,255,0)
        if(self.x<=0):
            self.x=0
        if(self.x>=850):
            self.x=850
        pygame.draw.circle(WIN, BLUE,(self.x,self.y),10)
#-------------------------------------------------------------------------------
def updateGame():
    WIN.blit(BACKGROUND,(0,0))
    brick.draw(WIN)
    ball.draw(WIN)

#Main---------------------------------------------------------------------------
pygame.init()
WIN = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Brick Breaker")
BACKGROUND = pygame.image.load("background.jpg")

brick = player(425,580,150,20)
ball = ball(50,50)

run=True
CLOCK =pygame.time.Clock()
while run :
    CLOCK.tick(30)
    updateGame()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] :
        brick.x -= brick.velocity
    elif keys[pygame.K_RIGHT] :
        brick.x += brick.velocity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#Main---------------------------------------------------------------------------
