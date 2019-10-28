import pygame
import os
import time

BALLSPRITE =  [pygame.image.load(os.path.join('sprites/ball' ,'%s.png' % frame)) for frame in range(1, 59)]
for i in range(0,58):
    BALLSPRITE[i] = pygame.transform.scale(BALLSPRITE[i], (20, 20))
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
        pygame.draw.rect(WIN,self.BLUE,(self.x,self.y,self.height,self.width))
#-------------------------------------------------------------------------------
class enemy ():
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height = height
        self.hit=0

    def draw(self,WIN):
        self.COLOR=(255,255,255)
        if(self.x<=0):
            self.x=0
        if(self.x>=850):
            self.x=850
        pygame.draw.rect(WIN,self.COLOR,(self.x,self.y,self.width,self.height))



#Ball class---------------------------------------------------------------------
class ball():
    def __init__(self,x,y) :
        self.x=x
        self.y=y
        self.velocity = 6
        self.slope = 1
        self.diraction = "UP"
        self.spriteCount = 1

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

        #if(self.spriteCount ==58):
            #self.spriteCount=0
        #self.spriteCount +=1
        #WIN.blit(BALLSPRITE[self.spriteCount//3] , (self.x,self.y))
        pygame.draw.circle(WIN,self.COLOR,(self.x,self.y),10)
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
    if(ball.y>=560):
        if(player.x<= ball.x +10<=player.x+150):
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
            WIN.close()

def checkCollisonWithEnemy(ball,enemy):
    if(ball.y<=(enemy.y+enemy.height)):
        if(enemy.x<=ball.x+10<=enemy.x+90):
            enemy.hit=1
            ball.slope = ball.slope*-1
            ball.diraction = "DOWN"

#Update visualization-----------------------------------------------------------
def updateGame(WIN):
    WIN.blit(BACKGROUND,(0,0))
    brick.draw(WIN)
    ball_com.draw(WIN)
    for i in range (enemies_number):
        if(enemies[i].hit==0):
            enemies[i].draw(WIN)
    pygame.display.update()
#-------------------------------------------------------------------------------

#Main---------------------------------------------------------------------------
pygame.init()
WIN = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Brick Breaker")
BACKGROUND = pygame.image.load("background.jpg")

brick = player(425,580,150,20)
ball_com = ball(500,570)
enemies_number = 9
enemies = []
space = 0
i=0
for i in range(enemies_number):
    enemies.append(enemy(0 + space,0,90,20))
    space +=100

run=True
CLOCK =pygame.time.Clock()
while run :
    CLOCK.tick(30)
    updateGame(WIN)
    checkCollisionWithPlayer(ball_com,brick)
    for i in range (enemies_number):
        checkCollisonWithEnemy(ball_com,enemies[i])
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] :
        brick.x -= brick.velocity
    elif keys[pygame.K_RIGHT] :
        brick.x += brick.velocity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#Main---------------------------------------------------------------------------
