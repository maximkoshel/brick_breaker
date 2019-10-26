import pygame

class player():
    def __init__(x,y,height,width) :
        self.x=x
        self.y=y
        self.height = height
        self.width = width
        self.velocity = 5



#Main---------------------------------------------------------------------------
pygame.init()
win = pygame.display.set_mode((1000,800))
pygame.display.set_caption("First Game")
run=True
clock =pygame.time.Clock()
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


#Main---------------------------------------------------------------------------
