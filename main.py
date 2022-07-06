##############################
#readying modules n packages##
##############################

#import
import pygame
import time
import random
#initializing pygame 
clock = pygame.time.Clock()
pygame.init()
##############################
##############################

##############################
###########display############
##############################
#defining the display width & height along with using them to create a display and add a name n icon to it
display_width = 800
display_height = 600
#display
gameDisplay = pygame.display.set_mode((display_width,display_height))
#display name
pygame.display.set_caption('dodge the ball!!!')
gameIcon = pygame.image.load('gmicon.png')
pygame.display.set_icon(gameIcon)
##############################
##############################

##############################
#######creating colors########
##############################
#black n white
black = (0,0,0)
white = (255,255,255)
#rgb colors (normal)
blue = (0,0,200)
green = (0,200,0)
red = (200,0,0)
#rgb colors (normal)
bright_blue = (0,0,255)
bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (53,115,255)
##############################
##############################

##############################
######creating a player#######
##############################
plyr_width = 73
plyrImg = pygame.image.load('plyr_icon.png')

def plyr(x,y):
    gameDisplay.blit(plyrImg,(x,y))

##############################
##############################

################################################
###setting the loop "fuel" to keep it running###
################################################	
pause = False
##############################
##############################

##############################
#####setting up stuff =D######
##############################
#counting how many "things" we have dodged
def things_dodged(count):
    font = pygame.font.Font("amatic-sc.bold.ttf", 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))
#making the "thing"s
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 
#the objects text are written on
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 

#sets up what happens when u collide with a thing
def collided():
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Died!", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit ",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15) 
#setting up buttons
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
#defines a Quit function that if used will stop the game almost instantly
def quitgame():
    pygame.quit()
    quit()
#an unpuaseing function 
def unpause():
    global pause
    pause = False
    
#if the game is supposed to be paused than this function is used ( pause key = p)
def paused():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)   

##############################
##############################

##############################
######## main menu ###########
##############################
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("amatic-sc.bold.ttf",50)
        TextSurf, TextRect = text_objects("wanna play dodge ball in minecraft mode?", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
		
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
##############################
##############################
    
    
############################## 
######### game loop ##########
##############################
    
def game_loop():
    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.8)
 
    x_change = 0
 
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
 
    thingCount = 1
 
    dodged = 0
 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
###setting up movement keys and other####
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_a:
                    x_change = -5
                if event.key == pygame.K_d:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                if event.key == pygame.K_PERIOD:
                    things(thing_startx, thing_starty, thing_width, thing_height, block_color)
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
 ############################################

        x += x_change
        gameDisplay.fill(white)
 
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
 
 
        
        thing_starty += thing_speed
        plyr(x,y)
        things_dodged(dodged)
 
        if x > display_width - plyr_width or x < 0:
            collided()
 
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
####checking if player has collided or not (still in work and has a bug =( )####
        if y < thing_starty+thing_height:
        	print('')
 
        if x > thing_startx and x < thing_startx + thing_width and x+plyr_width > thing_startx and x + plyr_width < thing_startx+thing_width:
                print('')
                collided()
				
        
        pygame.display.update()
        clock.tick(60)
#####activating main functions######
game_intro()
game_loop()
pygame.quit()
quit()
