import pygame
import os
import time
import random

#Inited pygame here so the music can play repeatedly----------------------------
pygame.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.2)


#Adding ball sprite------------------------------------------------------------
#BALLSPRITE =  [pygame.image.load(os.path.join('sprites/ball' ,'%s.png' % frame)) for frame in range(1, 59)]
#for i in range(0,58):
    #BALLSPRITE[i] = pygame.transform.scale(BALLSPRITE[i], (10, 10))
#------------------------------------------------------------------------------


def GetRandomColor():
    return random.randint(0,255)

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
        WIN.blit(PLAYER,(self.x,self.y))
#-------------------------------------------------------------------------------
class enemy ():
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height = height
        self.hit=0
        self.counter = 0
        r1 = GetRandomColor()
        r2 = GetRandomColor()
        r3  = GetRandomColor()
        self.COLOR=(r1,r2,r3)
    def draw(self,WIN):

        self.counter +=1
        if (self.counter>=30):
            r1 = GetRandomColor()
            r2 = GetRandomColor()
            r3  = GetRandomColor()
            self.COLOR=(r1,r2,r3)
            self.counter=0
        pygame.draw.rect(WIN,self.COLOR,(self.x,self.y,self.width,self.height))



#Ball class---------------------------------------------------------------------
class ball():
    def __init__(self,x,y) :
        self.x=x
        self.y=y
        self.velocity = 6
        self.slope = 0
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
        self.COLOR=(GetRandomColor(),GetRandomColor(),GetRandomColor())

        #if(self.spriteCount ==58):
            #self.spriteCount=0
        #self.spriteCount +=1
        #WIN.blit(BALLSPRITE[self.spriteCount//3] , (self.x,self.y))
        pygame.draw.circle(WIN,self.COLOR,(self.x,self.y),5)
#-------------------------------------------------------------------------------
def checkCollisionWithPlayer(ball,player):
#Check bounderies
    if(ball.x>=995):
        ball.slope = ball.slope*-1
    if(ball.x<=5):
        ball.slope = ball.slope*-1
    if(ball.y<=5):
        ball.slope = ball.slope*-1
        ball.diraction = "DOWN"
#Check collision with player
    if(ball.y>=570):
        if(player.x<= ball.x<=player.x+155):
            point = ball.x - player.x
            if(point<10):
                ball.slope =  -0.3
                ball.velocity = 11
                ball.diraction = "UP"
            elif(10<=point<20):
                ball.slope =  -0.5
                ball.velocity = 9
                ball.diraction = "UP"
            elif(20<=point<30):
                ball.slope =  -0.8
                ball.velocity = 7
                ball.diraction = "UP"
            elif(30<=point<40):
                ball.slope =  -1
                ball.velocity = 6
                ball.diraction = "UP"
            elif(40<=point<50):
                ball.slope =  -1.5
                ball.velocity = 5
                ball.diraction = "UP"
            elif(50<=point<60):
                ball.slope =  -2
                ball.velocity = 4
                ball.diraction = "UP"
            elif(60<=point<70):
                ball.slope =  -2.5
                ball.velocity = 3
                ball.diraction = "UP"
            elif(70<=point<80):
                ball.slope = 0
                ball.velocity = 6
                ball.diraction = "UP"
            elif(80<=point<90):
                ball.slope =  2.5
                ball.velocity = 3
                ball.diraction = "UP"
            elif(90<=point<100):
                ball.slope =  2
                ball.velocity = 4
                ball.diraction = "UP"
            elif(100<=point<110):
                ball.slope =  1.5
                ball.velocity = 5
                ball.diraction = "UP"
            elif(110<=point<120):
                ball.slope =  1
                ball.velocity = 6
                ball.diraction = "UP"
            elif(120<=point<130):
                ball.slope =  0.8
                ball.velocity = 7
                ball.diraction = "UP"
            elif(130<=point<140):
                ball.slope =  0.5
                ball.velocity = 9
                ball.diraction = "UP"
            elif(140<=point):
                ball.slope =  0.3
                ball.velocity = 11
                ball.diraction = "UP"

        else:
            main()
def checkCollisonWithEnemy(ball,enemy):
    if(ball.y<=(enemy.y+enemy.height)):
        if(enemy.x<=ball.x<=enemy.x+92):
            if(enemy.hit==0):
                enemy.hit=1
                ball.slope = ball.slope*-1
                ball.diraction = "DOWN"

#Update visualization-----------------------------------------------------------
def updateGame(WIN):
    WIN.blit(BACKGROUND,(0,0))
    brick.draw(WIN)
    ball_com.draw(WIN)
    for i in range (enemies_rows):
        for j in range(enemies_number):
            if(enemies[i][j].hit==0):
                enemies[i][j].draw(WIN)
    pygame.display.update()
#-------------------------------------------------------------------------------

#Main---------------------------------------------------------------------------
def main():

    global PLAYER,WIN,BACKGROUND,brick,ball_com,enemies,enemies_rows,enemies_number
    WIN = pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Brick Breaker")
    BACKGROUND = pygame.image.load("background.jpg")
    PLAYER = pygame.image.load("player.png")

    brick = player(425,580,150,20)
    ball_com = ball(500,570)
    enemies_number = 10
    enemies_rows = 3
    enemies = [[enemy for x in range(enemies_number)]for y in range(enemies_rows)]
    space = 5
    for i in range(enemies_rows):
        for j in range(enemies_number):
            enemies[i][j]=(enemy(0+space,0+i*30,90,20))
            if space >=850:
                space = -95
            space +=100

    run=True
    CLOCK =pygame.time.Clock()
    while run :
        CLOCK.tick(60)
        updateGame(WIN)
        checkCollisionWithPlayer(ball_com,brick)
        for i in range(enemies_rows):
            for j in range(enemies_number):
                checkCollisonWithEnemy(ball_com,enemies[i][j])
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] :
            brick.x -= brick.velocity
        elif keys[pygame.K_RIGHT] :
            brick.x += brick.velocity

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
main()
#Main---------------------------------------------------------------------------
