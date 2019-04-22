#Aca se importan las librerias o modulos que se
#utilizaran durante la ejecucion de la aplicacion.
import pygame,sys
from pygame.locals import *

#Para que el juego corra a una velocidad establecida se establece
#el Clock o tiempo de ejecucion.
clock = pygame.time.Clock()  
#Como obligacion para que python se ejecute debe tener la
#sentencia pygame.init()
pygame.init()
#Ahora se crea la ventana inicial con los valores de
#la resolucion.
ancho = 1000
alto = 650
ventana = pygame.display.set_mode((ancho,alto))
#Este parametro se utiliza para mostar un mensaje en la ventana
pygame.display.set_caption("Space Invaders 1.0")
#Aca se define los valores de los objetos a utilizar con sus iconos.
laser = pygame.image.load("imagenes/laser1.png")
laser_y = 0
nave_defensora = pygame.image.load("imagenes/navedefensora.png")
ancho_nave= nave_defensora.get_width()
alto_nave= nave_defensora.get_height()
nave_defensora_x = ventana.get_height() - nave_defensora.get_height()   #Estos parametros se usan para elegir
nave_defensora_y =  ventana.get_width()/2 - nave_defensora.get_width()/2 #la posicion inicial de la nave.
"""ventana.blit(nave_defensora, (nave_defensora_y, nave_defensora_x))""" #De esta manera se dibuja la nave.
velocidad = 30
#Ahora para mostrar la ventana se utilizara un loop
#infinito mientras se cumpla o sea verdad, ademas de añadir
#el evento para el clock.
while True:
    ventana.fill((0,0,0))
    clock.tick(60)
    ventana.blit(nave_defensora, (nave_defensora_y, nave_defensora_x))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                laser_y = nave_defensora_x
                laser_x = nave_defensora_y +23
            if evento.key == pygame.K_RIGHT:
                nave_defensora_y += velocidad
                if nave_defensora_y <= 0:
                    nave_defensora_y = 0
            if evento.key == pygame.K_LEFT:
                nave_defensora_y -= velocidad
                if nave_defensora_y >= ancho:
                    nave_defensora_y = ancho-50
            if evento.key == pygame.K_DOWN:
                nave_defensora_x += velocidad
                if nave_defensora_x <= 0:
                    nave_defensora_x = 0
            if evento.key == pygame.K_UP:
                nave_defensora_x -= velocidad
                if nave_defensora_x >= alto:
                    nave_defensora_x = alto-50
    if laser_y > 0:
        ventana.blit(laser, (laser_x, laser_y))
        laser_y -= 10
        
    pygame.display.update()

            
