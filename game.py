import pygame
import time
#Player Class-------------------------------------------------------------------
class player():
    def __init__(self,x,y,height,width) :
        self.x=x
        self.y=y
        self.height = height
        self.width = width
        self.velocity = 15

    def draw(self,WIN):
        self.BLUE=(0,0,255)
        if(self.x<=0):
            self.x=0
        if(self.x>=850):
            self.x=850
        pygame.draw.rect(WIN,self.BLUE,(self.x,self.y,150,20))
#-------------------------------------------------------------------------------

#Ball class---------------------------------------------------------------------
class ball():
    def __init__(self,x,y) :
        self.x=x
        self.y=y
        self.velocity = 6
        self.slope = 1
        self.diraction = "UP"

    def draw(self,WIN):
        if (self.slope<0) and self.diraction == "UP":
            self.x =self.x -self.velocity
            self.y =  self.y -(self.slope*self.velocity*-1)
        elif (self.slope>0) and self.diraction == "UP":
            self.x =self.x + self.velocity
            self.y =  self.y -(self.slope*self.velocity)
        elif (self.slope<0) and self.diraction == "DOWN":
            self.x =self.x + self.velocity
            self.y =  self.y +(self.slope*self.velocity*-1)
        elif (self.slope>0) and self.diraction == "DOWN":
            self.x =self.x - self.velocity
            self.y =  self.y +(self.slope*self.velocity)
        elif (self.slope == 0) and self.diraction == "DOWN":
            self.y = self.y+10
        elif (self.slope == 0) and self.diraction == "UP":
            self.y = self.y-10


        self.x = int(self.x)
        self.y = int(self.y)
        self.COLOR=(0,255,0)
        pygame.draw.circle(WIN, self.COLOR,(self.x,self.y),10)

#-------------------------------------------------------------------------------
def checkCollisionWithPlayer(ball,player):
#Check bounderies
    if(ball.x>=1000):
        ball.slope = ball.slope*-1

    if(ball.x<=0):
        ball.slope = ball.slope*-1

    if(ball.y<=0):
        ball.slope = ball.slope*-1
        ball.diraction = "DOWN"
#Check collision with player
    if(ball.y>=575):
        if(player.x<= ball.x <=player.x+150):
            point = ball.x - player.x
            if(0<=point<10):
                ball.slope =  -0.3
                ball.velocity = 12
                ball.diraction = "UP"
            elif(10<=point<20):
                ball.slope =  -0.5
                ball.velocity = 10
                ball.diraction = "UP"
            elif(20<=point<30):
                ball.slope =  -0.8
                ball.velocity = 8
                ball.diraction = "UP"
            elif(30<=point<40):
                ball.slope =  -1
                ball.velocity = 6
                ball.diraction = "UP"
            elif(40<=point<50):
                ball.slope =  -2
                ball.velocity = 5
                ball.diraction = "UP"
            elif(50<=point<=60):
                ball.slope =  -2.5
                ball.velocity = 4
                ball.diraction = "UP"
            elif(70<=point<80):
                ball.slope =  0
                ball.velocity = 6
                ball.diraction = "UP"
            elif(80<=point<90):
                ball.slope =  2.5
                ball.velocity = 4
                ball.diraction = "UP"
            elif(100<=point<110):
                ball.slope =  2
                ball.velocity = 4
                ball.diraction = "UP"
            elif(110<=point<120):
                ball.slope =  1
                ball.velocity = 6
                ball.diraction = "UP"
            elif(120<=point<130):
                ball.slope =  0.8
                ball.velocity = 8
                ball.diraction = "UP"
            elif(130<=point<140):
                ball.slope =  0.5
                ball.velocity = 10
                ball.diraction = "UP"
            elif(140<=point<=150):
                ball.slope =  0.3
                ball.velocity = 12
                ball.diraction = "UP"

        else:
            print("Game over")
#Update visualization-----------------------------------------------------------
def updateGame(WIN):
    WIN.blit(BACKGROUND,(0,0))
    brick.draw(WIN)
    ball_com.draw(WIN)
    pygame.display.update()
#-------------------------------------------------------------------------------

#Main---------------------------------------------------------------------------
pygame.init()
WIN = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Brick Breaker")
BACKGROUND = pygame.image.load("background.jpg")

brick = player(425,580,150,20)
ball_com = ball(500,570)

run=True
CLOCK =pygame.time.Clock()
while run :
    CLOCK.tick(60)
    updateGame(WIN)
    checkCollisionWithPlayer(ball_com,brick)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] :
        brick.x -= brick.velocity
    elif keys[pygame.K_RIGHT] :
        brick.x += brick.velocity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#Main---------------------------------------------------------------------------
