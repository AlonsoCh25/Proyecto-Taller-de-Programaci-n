import pygame,sys
from pygame.locals import *

#Elementos Constantes
ancho = 800
alto = 600


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Space Invaders 1.0")
    salir = False
    while salir != True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: #Cuando se precione la tecla de salida. La pantalla se cerrará.
                    salir = True
        pygame.display.update()

main()
