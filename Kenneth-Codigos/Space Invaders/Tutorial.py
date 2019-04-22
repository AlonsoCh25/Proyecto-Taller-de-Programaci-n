#Iniciamos importando modulos de pygame
import pygame

#Colores

blanco = (255,255,255)
negro = (0,0,0)
#Constantes

ancho = 600
alto = 800

#Superficies o rectangulos:

pantalla = pygame.display.set_mode([alto,ancho])
contador = pygame.Rect((0,0,0,0.30))
nave1 = pygame.image.load("imagenes/enemigo1.png")
nave2 = pygame.image.load("imagenes/enemigo2.png")
nave3 = pygame.image.load("imagenes/enemigo3.png")
fondo = pygame.image.load("imagenes/fondo.jpg")

#Definimos los medios a usar:

class Nave:#Se usan las clases para crear objetos.
    def __init__(self):
        self.nave = pygame.image.load("imagenes/navedefensora.png")
        self.laser1 = pygame.image.load("imagenes/laser1.png") 
        self.ancho_nav = 600
        self.alto_nav = 800
        self.posicion_x = self.alto_nav/2
        self.posicion_y = self.ancho_nav-50
        self.vel = 50
        self.laser1_y = 0
        self.laser2_y = 0
    def movimiento(self, vel, ancho_nav, alto_nav,  laser1_y):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #Moviviento de la nave y el laser.
                if event.key == pygame.K_DOWN:
                    ancho_nav += vel
                    if ancho_nav > 599:
                        ancho_nav = 599
                if event.key == pygame.K_UP:
                    ancho_nav -= vel
                    if ancho_nav < 80:
                        ancho_nav = 80
                if event.key == pygame.K_RIGHT:
                    alto_nav += vel
                    if alto_nav > 1499:
                        alto_nav = 1499
                if event.key == pygame.K_LEFT:
                    alto_nav -= vel
                    if alto_nav < 50:
                        alto_nav = 50
                if laser1_y <= 0:
                    if event.key == pygame.K_SPACE:
                        laser1_y = ancho_nav-50
                        laser1_x = alto_nav/2 + 23
        if laser1_y > 0:
                pantalla.blit(laser1, (laser1_x, laser1_y))
                laser1_y -= 10
                
        pantalla.blit(nave, (alto_nav/2,ancho_nav-50))
    
def main():
    pygame.init() #Acá se llaman todos los modulos de Pygame
    pantalla #Se crea la pantalla
    
    nave_x = 50
    nave_y = 50
    ult_nave = 500
    first_nave = 0
    laser1_y = 0
    laser2_y = 0
    vel = 50
    pygame.display.set_caption("Space Invaders 1.0") #Acá se define el titulo de la ventana
    salir = False
    reloj1 = pygame.time.Clock()#Se establece para posteriormente ayudar a controlar los FPS.
    reloj2 = pygame.time.Clock()
    while salir != True: #Loop Principal
        
        if ult_nave < 700:
            nave_x += vel
            ult_nave += vel
            first_nave += vel
        if ult_nave >= 700:
            nave_x -= vel
            ult_nave = 700
            first_nave -= vel
        if first_nave < 0:
            nave_x += vel
            ult_nave = 450
            first_nave = 0
        reloj1.tick(40)#Se define la tasa de FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Cuando se precione la tecla de salida. La pantalla se cerrará.
                salir = True
            
        
               
        
        
                
                    
                    
                
                
              
                
        
         
        pantalla.fill(blanco)#Completa la pantalla con el color definido
        pantalla.blit(fondo,(0,0))
        
        
        nave1_0 = pantalla.blit(nave1, (nave_x, nave_y))
        nave2_0 = pantalla.blit(nave2, (nave_x, nave_y+50))
        nave3_0 = pantalla.blit(nave3, (nave_x, nave_y+100))

        nave1_1 = pantalla.blit(nave1, (nave_x+50, nave_y))
        nave2_1 = pantalla.blit(nave2, (nave_x+50, nave_y+50))
        nave3_1 = pantalla.blit(nave3, (nave_x+50, nave_y+100))

        nave1_2 = pantalla.blit(nave1, (nave_x+100, nave_y))
        nave2_2 = pantalla.blit(nave2, (nave_x+100, nave_y+50))
        nave3_2 = pantalla.blit(nave3, (nave_x+100, nave_y+100))

        nave1_3 = pantalla.blit(nave1, (nave_x+150, nave_y))
        nave2_3 = pantalla.blit(nave2, (nave_x+150, nave_y+50))
        nave3_3 = pantalla.blit(nave3, (nave_x+150, nave_y+100))

        nave1_4 = pantalla.blit(nave1, (nave_x+200, nave_y))
        nave2_4 = pantalla.blit(nave2, (nave_x+200, nave_y+50))
        nave3_4 = pantalla.blit(nave3, (nave_x+200, nave_y+100))

        nave1_5 = pantalla.blit(nave1, (nave_x+250, nave_y))
        nave2_5 = pantalla.blit(nave2, (nave_x+250, nave_y+50))
        nave3_5 = pantalla.blit(nave3, (nave_x+250, nave_y+100))

        nave1_6 = pantalla.blit(nave1, (nave_x+300, nave_y))
        nave2_6 = pantalla.blit(nave2, (nave_x+300, nave_y+50))
        nave3_6 = pantalla.blit(nave3, (nave_x+300, nave_y+100))

        nave1_7 = pantalla.blit(nave1, (nave_x+350, nave_y))
        nave2_7 = pantalla.blit(nave2, (nave_x+350, nave_y+50))
        nave3_7 = pantalla.blit(nave3, (nave_x+350, nave_y+100))

        nave1_8 = pantalla.blit(nave1, (nave_x+400, nave_y))
        nave2_8 = pantalla.blit(nave2, (nave_x+400, nave_y+50))
        nave3_8 = pantalla.blit(nave3, (nave_x+400, nave_y+100))
        
        nave1_9 = pantalla.blit(nave1, (nave_x+450, nave_y))
        nave2_9 = pantalla.blit(nave2, (nave_x+450, nave_y+50))
        nave3_9 = pantalla.blit(nave3, (nave_x+450, nave_y+100))
        
        pygame.draw.rect(pantalla, negro, contador)
        pygame.display.update()#Se usa para actualizar la pantalla
           
            
    pygame.quit()#Cuando el "while" es false, se sale de la funcion y ejecuta esta acción
    
    


#Llamamos los medios que se definieron anterior mente.
main()
NaveDef = Nave()
NaveDef
