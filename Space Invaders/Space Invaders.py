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
alto = 600

#Superficies o rectangulos:
#Para la utilizacion de la matriz y otras variables, se determinó que la mejor manera es utilizarlas
#de manera global.
global Superficies
pantalla = pygame.display.set_mode([ancho,alto])
fuente1 = ("fuentes/space_invaders.ttf")
fuente = pygame.font.Font(fuente1, 30)

global objetos
clock = pygame.time.Clock()
intro1 = pygame.mixer.music.load("sonidos/intro1.mp3")
nave = pygame.image.load("imagenes/navedefensora.png")
laser = pygame.image.load("imagenes/laser1.png")
nave1 = pygame.image.load("imagenes/enemigo1.png")
nave2 = pygame.image.load("imagenes/enemigo2.png")
nave3 = pygame.image.load("imagenes/enemigo3.png")
laser2 = pygame.image.load("imagenes/Laser.png")
meteorito = pygame.image.load("imagenes/meteorito.png")
icono = pygame.image.load("imagenes/icono.png")
fondo = pygame.image.load("imagenes/fondo.jpg")

global matriz# SE crea la matriz con la intencio de alojar a las naves enemigas.
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
#Se intenta usar la clase Nave para los parametros y movimiento de la nave defensora, por
#algunos errores se deseña y utiliza directamente en el MainScene()
"""class Nave:
    def __init__(self):
        self.nave = pygame.image.load("imagenes/navedefensora.png")
        self.laser = pygame.image.load("imagenes/laser1.png")
        self.navex = ancho/2
        self.navey = alto-50
        self.posicionx = self.navex
        self.posiciony =  self.navey
        self.lasery = 0
        self.vel = 10
        bandera=True
        while bandera:
            pantalla.blit(fondo,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    bandera=False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #Moviviento de la nave y el laser.
                    if event.key == pygame.K_DOWN:
                        self.navex += self.vel
                        if self.navex > 599:
                            self.navex = 599
                    if event.key == pygame.K_UP:
                        self.navex -= self.vel
                        if self.navex < 80:
                            self.navex = 80
                    if event.key == pygame.K_RIGHT:
                        self.navey += self.vel
                        if self.navey > 1499:
                            self.navey = 1499
                    if event.key == pygame.K_LEFT:
                        self.navey -= self.vel
                        if self.navey < 50:
                            self.navey = 50
                    if self.lasery <= 0:
                        if event.key == pygame.K_SPACE:
                            self.lasery = self.x-50
                            laserx = self.navey/2 + 23
                    if self.lasery > 0:
                        pantalla.blit(laser, (laserx, self.lasery))
                        self.lasery -= 10
            pantalla.blit(self.nave, (self.posicionx, self.posiciony))"""
                   

#A partir de aquí, se observan las posibles Scenas del juego, como Pause, GameOver y menus, así
#como el loop principal del juego.
def GamePause():
    pantalla.blit(fondo,(0,0)) #Esto crea el fondo de la Scena
    fuentee1 = "fuentes/space_invaders.ttf"#Acá se observa como se crean las letras que aparecen en pantalla.
    fuente = pygame.font.Font(fuentee1, 50)
    fuente1 = pygame.font.Font(fuentee1, 30)
    texto = fuente.render("Game Pause", 0, (255, 255, 255))
    texto1 = fuente1.render("Precione la tecla P para continuar", 0, (230, 255, 255))
    pantalla.blit(texto,(300, 250))#Aca se dibujan los Textos
    pantalla.blit(texto1,(150, 325))
    pantalla
    global objetos#se importan los objetos globales
    pygame.display.set_icon(icono)
    pygame.display.set_caption("Space Invaders 1.0")
    bandera = True
    pygame.display.update()
    while bandera :#Mientras sea verdadero se ejecutara el codigo
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Se utiliza para cerrar el juego
                bandera=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:#Cuando se precione la tecla asignada, se dirigira al mainScene()
                    mainScene()
    
    pygame.font.quit()
    pygame.quit()
"""def GameOverScene():"""#Aquí corresponde la Scena del GameOver.
def mainScene():#Loop principal, aquí ocurren la mayor parte de los eventos.
    pygame.init()
    global matriz
    global objetos
    pantalla
    pygame.display.set_caption("Space Invaders 1.0")
    lasery = 0
    vel = 50
    pygame.mixer.music.play()
    navex = ancho/2
    navey = alto-50
    posicionx = navex
    posiciony = navey
    while True: #Mientras sea verdadero se ejecutara el codigo               
        pantalla.blit(fondo, (0,0))
        clock.tick(60)#La frecuencia de acctualizacion.
        pantalla.blit(nave, (navex, navey))#se dibuja la nave en pantalla
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:#Se utiliza para cerrar el juego
                pygame.quit()
               
            elif event.type == pygame.KEYDOWN:#Durante este segmento, se establecen las teclas y maneras de utilizar el juego, y el movimiento de la nave y el laser.
                if event.key == pygame.K_p:
                    GamePause()
                if event.key == pygame.K_DOWN:#Por ejemplo, al precionar la tecla DOWN, la nave se movera en y, la velocidad establecida.
                    navey += vel
                    if navey > 550:
                        navey = 550
                if event.key == pygame.K_UP:                    
                    navey -= vel
                    if navey < 0:
                        navey = 0
                if event.key == pygame.K_RIGHT:
                    navex += vel
                    if navex > 950:
                        navex = 950
                if event.key == pygame.K_LEFT:                    
                    navex -= vel
                    if navex < 0:
                        navex = 0
                if lasery <= 0:
                    if event.key == pygame.K_SPACE:
                        lasery = navey-50
                        laserx = navex + 23        
        if lasery > 0:
            pantalla.blit(laser, (laserx, lasery))
            lasery -= 10        
                      
        for i in range(0,3):#Con este codigo se generan las naves enemigas en los espacios deseados de la matriz.
            for j in range(5,15):
                matriz[i][j] = pygame.draw.rect(pantalla,negro,(50*j,50*i,50,50),0)
                pantalla.blit(nave1, matriz[i][j])
        pygame.display.update()
    

   
def menuScene():#Esta Scena es la que se toma de manera inicial, como una introduccion al juego.
    pantalla.blit(fondo,(0,0))#Se crea el fondo.
    fuentee1 = "fuentes/space_invaders.ttf" #Se carga la fuente a usar.
    fuente = pygame.font.Font(fuentee1, 50)
    fuente1 = pygame.font.Font(fuentee1, 30)
    fuente2 = pygame.font.Font(fuentee1, 20)
    texto = fuente.render("Space Invaders", 0, (255, 255, 255))#Se establece el texto y su color.
    texto1 = fuente1.render("Precione cualquier tecla para continuar", 0, (230, 255, 255))
    texto2 = fuente2.render("Develop by Kenneth Castillo and Camilo Solis", 0, (255, 255, 230))
    pantalla.blit(texto,(250, 250))#Aqui se dibujan en la pantalla los textos.
    pantalla.blit(texto1,(100, 325))
    pantalla.blit(texto2,(200, 550))
    pantalla
    global objetos
    pygame.display.set_icon(icono)#Se establece el icono y titulo de la ventana.
    pygame.display.set_caption("Space Invaders 1.0")
    bandera = True
    pygame.display.update()
    intro1#Se carga la musica a utilizar en el juego.
    pygame.mixer.music.play()#Se corre la musica.
    while bandera :
        pygame.init()
        for event in pygame.event.get():#Se utiliza para cerrar el juego
            if event.type == pygame.QUIT:
                bandera=False
            if event.type == pygame.KEYDOWN:#Como lo indica el enunciado, cuando se precione cualquier tecla, continuara con el loop principal.
                mainScene()
    pygame.mixer.music.stop()
    pygame.font.quit()
    pygame.quit()



#Esta funcion seria utilizada para crear el movimiento de las naves enemigas en la matriz.
"""def movimiento(movimiento):
    global matriz
    if movimiento == "derecha":
        for i in range(16):
             for j in range(20, 0):
                 matriz[i][j]"""





menuScene()
pygame.display.update()
pygame.quit()
