#Iniciamos importando modulos de pygame
import pygame

#Colores

blanco = (255,255,255)
negro = (0,0,0)
#Constantes

ancho = 1000
alto = 800

#Superficies o rectangulos:

pantalla = pygame.display.set_mode([ancho,alto])
#contador = pygame.Rect((0,0,0,0.30))
nave1 = pygame.image.load("imagenes/enemigo1.png")
nave2 = pygame.image.load("imagenes/enemigo2.png")
nave3 = pygame.image.load("imagenes/enemigo3.png")
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

def main():
    global matriz
    pygame.init()
    pantalla
    pygame.display.set_caption("Space Invaders 1.0")
    bandera=True
    while bandera:
        pantalla.blit(fondo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bandera=False

                break#Cuando se precione la tecla de salida. La pantalla se cerrará.
        for i in range(3):
             for j in range(5,15):
                matriz[i][j] = pygame.draw.rect(pantalla,negro,(50*j,50*i,50,50),0)
                pantalla.blit(nave1, matriz[i][j])


    #print(matriz)

        pygame.display.update()
    pygame.quit()

def movimiento(movimiento):
    global matriz
    if movimiento == "derecha":
        for i in range(16):
             for j in range(20, 0):
                 matriz[i][j]





main()
