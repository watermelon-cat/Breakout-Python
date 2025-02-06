# import the pygame library and initialise the game engine
import pygame
import random
pygame.init()
#open a new window, caption it "PING PONG"
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("PING PONG")
#here's the variable that runs our game loop
doExit = False
#The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#variables to hold paddle position
#these go above game loop
p1x = 400
p1y = 650

#ball variables
bx = 500 #xposition
by = 400 #yposition
bVx = 5 #x velocity
bVy = 5 #y velocity
ball_size = 20

#Score variables
p1Score = 0

class brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100, 250), random.randrange(100, 250), random.randrange(100, 250))
        self.isDead = False
    def draw(self):
        if not self.isDead:
            pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 100, 50))
    def collide(self, bx, by):
        if not self.isDead:
            if (bx + ball_size > self.xpos and
                bx < self.xpos + 100 and # width of the brick is 100
                by + ball_size > self.ypos and
                by < self.ypos + 50): # height of brick is 50
                self.isDead = True
                return True
        return False
        
b1 = brick(250, 50)
b2 = brick(360, 50)
b3 = brick(470, 50)
b4 = brick(580, 50)
b5 = brick(690, 50)
b6 = brick(250, 150)
b7 = brick(360, 150)
b8 = brick(470, 150)
b9 = brick(580, 150)
b10 = brick(690, 150)


while not doExit: #GAME LOOP---------------------------------------------------------------------------------------------
    
    #event queue stuff------------------------------------------------------------------------------------------------
    clock.tick(60) #set the fps
    
    for event in pygame.event.get(): #check if user did something
        if event.type == pygame.QUIT: #check if user clicked close
            doExit = True #Flag that we are done so we exit game loop
            
    #game logic will go here---------------------------------------------------------------------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        p1x-=10
    if keys[pygame.K_d]:
        p1x+=10
        
            
    #ball movement
    bx -= bVx
    by -= bVy
        
    #reflect ball off the side of the walls of screen
    if bx < 0 or bx + 20 > 1000:
        bVx *= -1
            
    if by < 0 or by + 20 > 700:
        bVy *= -1
        
    #ball-paddle reflection
    if by > p1y - 20 and bx - 20 > p1x and bx + 20 < p1x + 100:
        bVy *= -1
        print("hit!")
        
        
    if bx == 1000: #RIGHT WALL
        bVx *= 1
    if bx == 0: #this has been split up from right wall collision so we can increase scores
        bVx *= -1
    
    #ball collision with each brick
    if b1.collide(bx, by):
        bVy *= -1
        p1Score += 1
    if b2.collide(bx, by):
        bVy *= -1
        p1Score += 1
    if b3.collide(bx, by):
        bVy *= -1
        p1Score += 1
    if b4.collide(bx, by):
        bVy *= -1
        p1Score += 1
    if b5.collide(bx, by):
        bVy *= -1
        p1Score += 1
    if b6.collide(bx, by):
        bVy *= -1
        p1Score += 1
    if b7.collide(bx, by):
        bVy *= -1
        p1Score += 1
    if b8.collide(bx, by):
        bVy *= -1
        p1Score += 1
    if b9.collide(bx, by):
        bVy *= -1
        p1Score += 1
    if b10.collide(bx, by):
        bVy *= -1
        p1Score += 1
            
    #render section will go here---------------------------------------------------------------------------
    screen.fill((12, 44, 94)) #wipe screen black
    
    
    #draw a circle
    pygame.draw.circle(screen, (250, 237, 52), (bx, by), 20, 100)
    
    #draw a rectangle
    pygame.draw.rect(screen, (104, 232, 117), (p1x, p1y, 100, 20), 20)

    #draw bricks
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b10.draw()

    
    #display scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (850,10))
    
    #update the screen
    pygame.display.flip()
    
            
            
#END GAME LOOP------------------------------------------------------------------------------------------------
            
pygame.quit() #when game is done close down pygame

