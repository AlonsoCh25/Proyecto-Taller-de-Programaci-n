#Iniciamos importando modulos de pygame
import pygame
from pygame.locals import *
pygame.font.init()
#Colores
pygame.init()
blanco = (255,255,255)
negro = (0,0,0)
#Constantes
global resolution
ancho = 1000
alto = 800

#Superficies o rectangulos:
global Superficies
pantalla = pygame.display.set_mode([ancho,alto])
fuente1 = ("fuentes/space_invaders.ttf")
fuente = pygame.font.Font(fuente1, 30)

global objetos
nave = pygame.image.load("imagenes/navedefensora.png")
laser = pygame.image.load("imagenes/laser1.png")
nave1 = pygame.image.load("imagenes/enemigo1.png")
nave2 = pygame.image.load("imagenes/enemigo2.png")
nave3 = pygame.image.load("imagenes/enemigo3.png")
laser2 = pygame.image.load("imagenes/Laser.png")
meteorito = pygame.image.load("imagenes/meteorito.png")
icono = pygame.image.load("imagenes/icono.png")
fondo = pygame.image.load("imagenes/fondo.jpg")

global matriz
matriz=[[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]]
class Nave:
    def __init__(self, posicionx, posiciony):
        self.nave = pygame.image.load("imagenes/navedefensora.png")
        self.laser = pygame.image.load("imagenes/laser1.png")
        self.posicionx = posicionx
        self.posiciony =  posiciony
        self.lasery = 0
        def movimiento(self, vel, lasery, posicionx, posiciony):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #Moviviento de la nave y el laser.
                    if event.key == pygame.K_DOWN:
                        posicionx += vel
                        if posicionx > 599:
                            posicionx = 599
                    if event.key == pygame.K_UP:
                        posicionx -= vel
                        if posicionx < 80:
                            posicionx = 80
                    if event.key == pygame.K_RIGHT:
                        posiciony += vel
                        if posiciony > 1499:
                            posiciony = 1499
                    if event.key == pygame.K_LEFT:
                        posiciony -= vel
                        if posiciony < 50:
                            posiciony = 50
                    if lasery <= 0:
                        if event.key == pygame.K_SPACE:
                            lasery = posicionx-50
                            laserx = posiciony/2 + 23
            if lasery > 0:
                    pantalla.blit(laser, (laserx, lasery))
                    lasery -= 10


#def BattleScene():
#def GameOverScene():
def mainScene():
    global matriz
    global objetos
    pantalla
    pygame.display.set_caption("Space Invaders 1.0")
    bandera=True
    while bandera:
        pantalla.blit(fondo,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bandera=False
                break#Cuando se precione la tecla de salida. La pantalla se cerrará.
            if event.type == pygame.KEYDOWN:
                Nave(ancho/2, alto-50)

        for i in range(0,3):
             for j in range(5,15):
                matriz[i][j] = pygame.draw.rect(pantalla,negro,(50*j,50*i,50,50),0)
                pantalla.blit(nave1, matriz[i][j])


    #print(matriz)

        pygame.display.update()
    pygame.quit()
def menuScene():
    pantalla.blit(fondo,(0,0))
    fuentee1 = "fuentes/space_invaders.ttf"
    fuente = pygame.font.Font(fuentee1, 50)
    fuente1 = pygame.font.Font(fuentee1, 30)
    fuente2 = pygame.font.Font(fuentee1, 20)
    texto = fuente.render("Space Invaders", 0, (255, 255, 255))
    texto1 = fuente1.render("Precione cualquier tecla para continuar", 0, (230, 255, 255))
    texto2 = fuente2.render("Develop by Kenneth Castillo and Camilo Solis", 0, (255, 255, 230))
    pantalla.blit(texto,(250, 250))
    pantalla.blit(texto1,(100, 325))
    pantalla.blit(texto2,(200, 750))
    global resolution
    pantalla
    global objetos
    pygame.display.set_icon(icono)
    pygame.display.set_caption("Space Invaders 1.0")
    bandera = True
    while bandera :
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bandera=False
            if event.type == pygame.KEYDOWN:
                mainScene()
                break
    pygame.font.quit()
    pygame.quit()






def movimiento(movimiento):
    global matriz
    if movimiento == "derecha":
        for i in range(16):
             for j in range(20, 0):
                 matriz[i][j]





menuScene()
