import pygame
import random
import time

pygame.init()


#carga los sonidos(no los pone)
crash_sound = pygame.mixer.Sound("explosion.wav")
#carga la musica (no los pone)
pygame.mixer.music.load("music.mp3")

display_width = 800
display_height = 600

#              R        G    B
black     = (  0,   0,   0)
white     = (255, 255, 255)
red       = (255,   0,   0)
blue      = (  0,   0, 255)
green     = (  0, 255,   0)
yellow    = (255, 255,   0)
gray      = (100, 100, 100)
white     = (255, 255, 255)
orange    = (255, 128,   0)
bright_green=( 0, 255,   0)
bright_red  = (255,   10,   0)


ship_width = 24

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Space Invaders !')
clock = pygame.time.Clock()

shipImg = pygame.image.load('player.gif')
iconImg = pygame.image.load('icon2.png')
meteoriteIMG = pygame.image.load("meteorite 1.png")

pygame.display.set_icon(iconImg)

pause = False
#crash = True

def invaders_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, red)
    gameDisplay.blit(text,(0,0))

#def meteorite(invaderx, invadery, invaderw, invaderh, color):
#    gameDisplay.blit(meteoriteIMG((gameDisplay, color, [invaderx, invadery, invaderw, invaderh])))

def meteorite(invaderx, invadery, invaderw, invaderh, color):
    pygame.draw.rect(gameDisplay, color, [invaderx, invadery, invaderw, invaderh])

#def invaders(invaderx, invadery, invaderw, invaderh, color):
#    pygame.draw.rect(gameDisplay, color, [invaderx, invadery, invaderw, invaderh])

def ship(x,y):
    gameDisplay.blit(shipImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    

    
def button(msg, x, y,w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action !=None:
            action()
##            if action == "play":
##                game_loop()
##            elif action == "quit":
##                pygame.quit()
##                quit()

    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()


#__Menu de cuando chocas con los meteoritos
def crash():
    
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    #gameDisplay.fill(blue)
    largeText = pygame.font.Font('freesansbold.ttf',55)
    TextSurf, TextRect = text_objects("You crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again ?", 150, 450, 175, 50, green, bright_green,game_loop)
        button("Quit ?", 550, 450, 100, 50, red, bright_red,quit)

        pygame.display.update()
        clock.tick(15)

#para quitar la pausa
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


#__Menu para pausar el juego
def paused():

    pygame.mixer.music.pause()

    #gameDisplay.fill(blue)
    largeText = pygame.font.Font('freesansbold.ttf',55)
    TextSurf, TextRect = text_objects("Pausado", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("CONTINUE ???", 150, 450, 175, 50, green, bright_green,unpause)
        button("QUIT ???", 550, 450, 100, 50, red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

#__ Menu al iniciar el juego
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',55)
        TextSurf, TextRect = text_objects("Kenneth lo logre :D", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("PLAY", 150, 450, 100, 50, green, bright_green,game_loop)
        button("QUIT", 550, 450, 100, 50, red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


#____Juego principal
def game_loop():
    global pause

    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
######

# parametros de los meteoritos - puse mal el nombre D:
    invader_startx = random.randrange(0, display_width)
    invader_starty = -600
    invader_speed = 5
    invader_width = 50
    invader_height = 50

    invaderCount = 1

    dodged = 0
######
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #____________Teclas para el Juego _________________#
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                        pause = True
                        paused()
            ###################################################
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(gray)

     # _______movimiento de los meteoritos_______
        # invader(invaderx, invadery, invaderw, invaderh, color)
        meteorite(invader_startx, invader_starty, invader_width, invader_height, white)
       
        invader_starty += invader_speed
        ship(x,y)
        invaders_dodged(dodged)

     ##contar el puntaje y el choque con los meteoritos
        if x > display_width - ship_width or x < 0:
            crash()

        if invader_starty > display_height:
            invader_starty = 0 - invader_height
            invader_startx = random.randrange(0,display_width)
            dodged +=1
            invader_speed += 0
            invader_width += 0 #(dodged *1.2)


        if invader_starty > display_height:
            invader_starty = 0 - invader_height
            invader_startx = random.randrange(0,display_width)
            
        if y < invader_starty + invader_height:
            #print ("y crossover")

            if x > invader_startx and x < invader_startx + invader_width or x+ship_width > invader_startx and x + ship_width < invader_startx+invader_width:
                #print("x crossover")
                crash()

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
