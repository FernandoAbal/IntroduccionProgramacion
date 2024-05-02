#! /usr/bin/env python
import os, random, sys, math

from pygame import*
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesSeparador import *
from funcionesRESUELTO import *
from pygame import mixer

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        pygame.mixer.init()
        volumen= 5
        pygame.mixer.music.load('musica_juegito.mp3')
        #Preparar la ventana
        pygame.display.set_caption("Separar en SIlabas")
        screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.mixer.music.set_volume(volumen/10)
        pygame.mixer.music.play(5)

        settings = pygame.image.load("configIMG2.png").convert()
        settings = transform.scale(settings, [30,30])

        setUP=0
        setVOL=0
        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        TIEMPO_MAX =121
        segundos = TIEMPO_MAX
        fps = FPS_inicial
        DIFICULTAD=2
        tiempoPerdido=0
        tiempoJuegoNuevo=1

        puntos = 0
        nivel = 0
        palabra = ""
        lemarioEnSilabas=[]
        listaPalabrasDiccionario=[]

        archivo= open("lemario.txt","r")

        #lectura del diccionario
        lectura(archivo, listaPalabrasDiccionario)

        #elige una al azar

        palabraEnPantallaAnteriorSS=''
        palabraEnPantallaAnterior=''
        if nivel==0:
            screen.fill(COLOR_NIVEL3)
            dibujar(nivel,screen)

        elif nivel==1:
            #dibujamos el nivel 1
            screen.fill(COLOR_NIVEL1)
            dibujar1(volumen,setVOL,nivel,screen, palabra, palabraEnPantalla, puntos,segundos,palabraEnPantallaAnteriorSS, setUP)
            #dibujamos la imagen del menu
            screen.blit(settings,[755,5])
        elif nivel==2:
            #dibujamos el nivel 2
            screen.fill(COLOR_NIVEL2)
            dibujar2(volumen,setVOL,nivel,screen, palabra, palabraEnPantalla, puntos,segundos,palabraEnPantallaAnteriorSS, setUP)
            #dibujamos la imagen del menu
            screen.blit(settings,[755,5])
        elif nivel==3:
            #dibujamos el nivel 3
            screen.fill(COLOR_NIVEL3)
            dibujar3(volumen,setVOL,nivel,screen, palabra, palabraEnPantalla, puntos,segundos,palabraEnPantallaAnteriorSS, setUP)
            #dibujamos la imagen del menu
            screen.blit(settings,[755,5])
        elif nivel==4:
            #dibujamos el nivel 4
            screen.fill(COLOR_NIVEL4)
            dibujar4(volumen,setVOL,nivel,screen, palabra, palabraEnPantalla, puntos,segundos,palabraEnPantallaAnteriorSS, setUP)
            #dibujamos la imagen del menu
            screen.blit(settings,[755,5])
        elif nivel==5:
            #dibujamos la pantalla GANADOR
            screen.fill(COLOR_CORRECTOLVL3)
            dibujarF(nivel,screen, palabra, palabraEnPantalla, puntos,palabraEnPantallaAnteriorSS)
        elif nivel==6:
            #dibujamos la pantalla ELEGIR DIFICULTAD
            screen.fill(COLOR_NIVEL3)
            dibujarD(nivel,screen)
        elif nivel==7:
            #dibujamos la pantalla PERDEDOR
            screen.fill(COLOR_TIEMPO_FINAL)
            dibujarP(nivel,screen, palabra, palabraEnPantalla, puntos,palabraEnPantallaAnteriorSS)




        while segundos > -100:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()
            #print(gameClock.tick(fps))


            if True:
            	fps = 3
            posX,posY = pygame.mouse.get_pos()
            #print('posX: ',posX)
            #print('posY: ',posY)
            #print (pygame.mouse.get_pos())
            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #Funcionalidad Botones pantalla Inicial

                if nivel == 0:
                    if(e.type == MOUSEBUTTONDOWN):
                        if e.button == 1 and 80<posX<320 and 300<posY<360:
                            palabraEnPantalla=nuevaPalabraConDificultad(listaPalabrasDiccionario,DIFICULTAD)
                            nivel=nivel+1

                    if(e.type == MOUSEBUTTONDOWN):
                        if e.button == 1 and 480<posX<720 and 300<posY<360:
                            nivel=6

                #Funcionalidad Botones pantalla Ganador

                elif nivel == 5:
                    if(e.type == MOUSEBUTTONDOWN):
                        if e.button == 1 and 315<posX<467 and 330<posY<355:
                            nivel=0
                            setUP=0
                            TIEMPO_MAX= TIEMPO_MAX

                #Funcionalidad Botones pantalla Perdedor

                elif nivel == 7:
                    if(e.type == MOUSEBUTTONDOWN):
                        if e.button == 1 and 315<posX<467 and 330<posY<355:
                            nivel=0
                            puntos=0
                            setUP=0
                            TIEMPO_MAX= TIEMPO_MAX

                #Funcionalidad Botones pantalla Dificultad

                elif nivel == 6:
                    if(e.type == MOUSEBUTTONDOWN):
                        if e.button == 1 and 280<posX<520 and 180<posY<239:
                            DIFICULTAD=1
                            nivel=0

                    if(e.type == MOUSEBUTTONDOWN):
                        if e.button == 1 and 280<posX<520 and 241<posY<299:
                            DIFICULTAD=2
                            nivel=0

                    if(e.type == MOUSEBUTTONDOWN):
                        if e.button == 1 and 280<posX<520 and 301<posY<360:
                            DIFICULTAD=3
                            nivel=0

                #Funcionalidad Botones pantalla Niveles

                else:
                    if(e.type == MOUSEBUTTONDOWN):
                        if e.button == 1 and 755<posX<785 and 5<posY<35:
                            if setUP==0:
                                setUP=1
                            else:
                                setUP=0
                        if setUP==1:
                            if(e.type == MOUSEBUTTONDOWN):
                                if e.button == 1 and 660<posX<780 and 38<posY<57:
                                    nivel=0
                                    puntos=0
                                    setUP=0
                                    TIEMPO_MAX= TIEMPO_MAX
                            if(e.type == MOUSEBUTTONDOWN):
                                if e.button == 1 and 660<posX<780 and 58<posY<77:
                                    if setVOL==0:
                                        setVOL=1
                                    else:
                                        setVOL=0
                                if setVOL==1:
                                    if volumen > 0:
                                        if(e.type == MOUSEBUTTONDOWN):
                                            if e.button == 1 and 660<posX<680 and 79<posY<96:
                                                volumen=volumen-1
                                    if volumen < 10:
                                        if(e.type == MOUSEBUTTONDOWN):
                                            if e.button == 1 and 760<posX<780 and 79<posY<96:
                                                volumen=volumen+1





                pygame.mixer.music.set_volume(volumen/10)
                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabra += letra #es la palabra que escribe el usuario
                    if e.key == K_BACKSPACE:
                        palabra = palabra[0:len(palabra)-1]
                    if e.key == K_RETURN:
                        #pasa la palabra a silabas
                        palabraEnPantallaEnSilabas=palabraTOsilaba(palabraEnPantalla)
                        if esCorrecta(palabraEnPantallaEnSilabas, palabra):
                            puntos += puntaje(palabra)
                        else:
                            puntos-=1
                        if puntos>=25:
                            nivel=nivel+1
                            puntos=0
                        palabraEnPantallaAnteriorSS=palabraEnPantallaEnSilabas
                        #elige una al azar con dificultad
                        palabraEnPantalla=nuevaPalabraConDificultad(listaPalabrasDiccionario,DIFICULTAD)

                        palabra = ""

            #Guardamos el tiempo mientras que el usuario no esta jugando
            if nivel==0 or nivel ==6:
                tiempoPerdido=pygame.time.get_ticks()/1000


            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000 + tiempoPerdido

            #ventanta de perdedor
            if segundos <=0:
                nivel=7

            #Limpiar pantalla anterior


            #Dibujar de nuevo todo
            if nivel==0:
                #dibujamos el menu principal
                screen.fill(COLOR_NIVEL3)
                dibujar(nivel,screen)
            elif nivel==1:
                #dibujamos el nivel 1
                screen.fill(COLOR_NIVEL1)
                dibujar1(volumen,setVOL,nivel,screen, palabra, palabraEnPantalla, puntos,segundos,palabraEnPantallaAnteriorSS, setUP)
                #dibujamos la imagen del menu
                screen.blit(settings,[755,5])
            elif nivel==2:
                #dibujamos el nivel 2
                screen.fill(COLOR_NIVEL2)
                dibujar2(volumen,setVOL,nivel,screen, palabra, palabraEnPantalla, puntos,segundos,palabraEnPantallaAnteriorSS, setUP)
                #dibujamos la imagen del menu
                screen.blit(settings,[755,5])
            elif nivel==3:
                #dibujamos el nivel 3
                screen.fill(COLOR_NIVEL3)
                dibujar3(volumen,setVOL,nivel,screen, palabra, palabraEnPantalla, puntos,segundos,palabraEnPantallaAnteriorSS, setUP)
                #dibujamos la imagen del menu
                screen.blit(settings,[755,5])
            elif nivel==4:
                #dibujamos el nivel 4
                screen.fill(COLOR_NIVEL4)
                dibujar4(volumen,setVOL,nivel,screen, palabra, palabraEnPantalla, puntos,segundos,palabraEnPantallaAnteriorSS, setUP)
                #dibujamos la imagen del menu
                screen.blit(settings,[755,5])
            elif nivel==5:
                #dibujamos la pantalla GANADOR
                screen.fill(COLOR_CORRECTOLVL3)
                dibujarF(nivel,screen, palabra, palabraEnPantalla, puntos,palabraEnPantallaAnteriorSS)
            elif nivel==6:
                #dibujamos la pantalla ELEGIR DIFICULTAD
                screen.fill(COLOR_NIVEL3)
                dibujarD(nivel,screen)
            elif nivel==7:
                #dibujamos la pantalla PERDEDOR
                screen.fill(COLOR_TIEMPO_FINAL)
                dibujarP(nivel,screen, palabra, palabraEnPantalla, puntos,palabraEnPantallaAnteriorSS)

            #Actualizamos la pantalla
            pygame.display.flip()

        while 1:

            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

        archivo.close()
#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()

