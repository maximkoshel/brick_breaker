import pygame

class player():
    def __init__(x,y,height,width) :
        self.x=x
        self.y=y
        self.height = height
        self.width = width
        self.velocity = 5


def updateGame():
    win.blit(bakcground,(0,0))
    pygame.display.update()


#Main---------------------------------------------------------------------------
pygame.init()
win = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Brick Breaker")
bakcground = pygame.image.load("background.jpg")


run=True
clock =pygame.time.Clock()
while run :
    clock.tick(30)
    updateGame()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#Main---------------------------------------------------------------------------
