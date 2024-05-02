import pygame
from principal2 import*
from funcionesRESUELTO import *
from pygame.locals import *
from configuracion import *


def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")



def dibujar(nivel,screen):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)


    surface = pygame.display.set_mode((800,500))
    color = (255,0,0)
    pygame.draw.rect(surface, color, pygame.Rect(80, 300, 240, 60),  2)

    pygame.draw.rect(surface, color, pygame.Rect(480, 300, 240, 60),  2)




    #palabra boton JUGAR
    screen.blit(defaultFont.render('JUGAR', 1, COLOR_TIEMPO_FINAL), (ANCHO-640,ALTO-178))
    #palabra boton DIFICULTAD
    screen.blit(defaultFont.render('DIFICULTAD', 1, COLOR_TIEMPO_FINAL), (ANCHO-260,ALTO-178))
    #muestra el titulo
    screen.blit(defaultFontGrande.render('MENU PRINCIPAL', 1, COLOR_TIEMPO_FINAL), (ANCHO-750,ALTO-450))


def dibujarModo(nivel,screen):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)


    surface = pygame.display.set_mode((800,500))
    color = (255,0,0)
    pygame.draw.rect(surface, color, pygame.Rect(280, 120, 240, 60),  2)

    pygame.draw.rect(surface, color, pygame.Rect(280, 300, 240, 60),  2)


    #palabra boton JUGAR
    screen.blit(defaultFont.render('Infinito', 1, COLOR_TIEMPO_FINAL), (ANCHO-640,ALTO-178))
    #palabra boton DIFICULTAD
    screen.blit(defaultFont.render('Clasico', 1, COLOR_TIEMPO_FINAL), (ANCHO-260,ALTO-178))

    #muestra la palabra
    screen.blit(defaultFontGrande.render('MODOS', 1, COLOR_TIEMPO_FINAL), (ANCHO-750,ALTO-450))





def dibujarD(nivel,screen):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)


    surface = pygame.display.set_mode((800,500))
    color = (255,0,0)
    pygame.draw.rect(surface, color, pygame.Rect(280, 180, 240, 60),  2)

    pygame.draw.rect(surface, color, pygame.Rect(280, 240, 240, 60),  2)

    pygame.draw.rect(surface, color, pygame.Rect(280, 300, 240, 60),  2)


    #palabra boton JUGAR
    screen.blit(defaultFont.render('FACIL', 1, COLOR_TIEMPO_FINAL), (367,202))
    #palabra boton DIFICULTAD
    screen.blit(defaultFont.render('NORMAL', 1, COLOR_TIEMPO_FINAL), (355,262))

    screen.blit(defaultFont.render('DIFICIL', 1, COLOR_TIEMPO_FINAL), (362,322))

    #muestra la palabra
    screen.blit(defaultFontGrande.render('DIFICULTAD', 1, COLOR_TIEMPO_FINAL), (ANCHO-630,ALTO-450))





def dibujar1(volumen,setVOL,nivel,screen, palabraUsuario, palabraActual, puntos, segundos,palabraEnPantallaAnteriorSS,setUP):
    defaultFontMenu= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_MENU)
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #menu desplegable
    if setUP == 1:
        color2= (232, 95, 99)
        pygame.draw.rect(screen, color2, pygame.Rect(660, 38, 120, 20),  2)
        pygame.draw.rect(screen, color2, pygame.Rect(660, 58, 120, 20),  2)
        if setVOL == 1:
            pygame.draw.rect(screen, color2, pygame.Rect(660, 78, 120, 20),  2)

            n=0
            for q in range(0,10):
                pygame.draw.rect(screen, color2, pygame.Rect(673+n, 84, 9, 8),  2)
                n=n+9
            i=0
            for t in range(0,volumen):
                pygame.draw.rect(screen, color2, pygame.Rect(675+i, 86, 7, 4),  4)
                i=i+9

            screen.blit(defaultFont.render("+" , 1, color2), (765, 78))
            screen.blit(defaultFont.render("-" , 1, color2), (664, 78))
        screen.blit(defaultFontMenu.render("Menu Principal" , 1, color2), (675, 42))
        screen.blit(defaultFontMenu.render("Volumen" , 1, color2), (692, 62))

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-90) , (ANCHO, ALTO-90), 5)
    #Linea Vertical
    pygame.draw.line(screen, (255,255,255), (ANCHO-600, ALTO-90) , (ANCHO-600, ALTO), 5)
    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (ANCHO-580, ALTO-56))
    #palabra ingresar:
    screen.blit(defaultFont.render('INGRESAR:', 1, COLOR_TEXTO), (ANCHO-755, ALTO-56))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (600, 10))
    #muestra el nivel
    screen.blit(defaultFont.render("Nivel " + str(nivel), 1, COLOR_TEXTO), (340, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #muestra la palabra
    screen.blit(defaultFontGrande.render(palabraActual, 1, COLOR_LETRAS), (ANCHO//2-len(palabraActual)*TAMANNO_LETRA_GRANDE//4,ALTO-400))
    #muestra la palabra anterior
    screen.blit(defaultFont.render(palabraEnPantallaAnteriorSS, 1, COLOR_CORRECTO), (ANCHO//2-len(palabraEnPantallaAnteriorSS)*TAMANNO_LETRA//4,ALTO-150))


def dibujar2(volumen,setVOL,nivel,screen, palabraUsuario, palabraActual, puntos, segundos,palabraEnPantallaAnteriorSS,setUP):
    defaultFontMenu= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_MENU)
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #menu desplegable
    if setUP == 1:
        color2= (232, 95, 99)
        pygame.draw.rect(screen, color2, pygame.Rect(660, 38, 120, 20),  2)
        pygame.draw.rect(screen, color2, pygame.Rect(660, 58, 120, 20),  2)
        if setVOL == 1:
            pygame.draw.rect(screen, color2, pygame.Rect(660, 78, 120, 20),  2)
            n=0
            for q in range(0,10):
                pygame.draw.rect(screen, color2, pygame.Rect(673+n, 84, 9, 8),  2)
                n=n+9
            i=0
            for t in range(0,volumen):
                pygame.draw.rect(screen, color2, pygame.Rect(675+i, 86, 7, 4),  4)
                i=i+9
            screen.blit(defaultFont.render("+" , 1, color2), (765, 78))
            screen.blit(defaultFont.render("-" , 1, color2), (664, 78))
        screen.blit(defaultFontMenu.render("Menu Principal" , 1, color2), (675, 42))
        screen.blit(defaultFontMenu.render("Volumen" , 1, color2), (692, 62))
    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-90) , (ANCHO, ALTO-90), 5)
    #Linea Vertical
    pygame.draw.line(screen, (255,255,255), (ANCHO-600, ALTO-90) , (ANCHO-600, ALTO), 5)
    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (ANCHO-580, ALTO-56))
    #palabra ingresar:
    screen.blit(defaultFont.render('INGRESAR:', 1, COLOR_TEXTO), (ANCHO-755, ALTO-56))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (600, 10))
    #muestra el nivel
    screen.blit(defaultFont.render("Nivel " + str(nivel), 1, COLOR_TEXTO), (340, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #muestra la palabra
    screen.blit(defaultFontGrande.render(palabraActual, 1, COLOR_LETRAS), (ANCHO//2-len(palabraActual)*TAMANNO_LETRA_GRANDE//4,ALTO-400))
    #muestra la palabra anterior
    screen.blit(defaultFont.render(palabraEnPantallaAnteriorSS, 1, COLOR_CORRECTO), (ANCHO//2-len(palabraEnPantallaAnteriorSS)*TAMANNO_LETRA//4,ALTO-150))


def dibujar3(volumen,setVOL,nivel,screen, palabraUsuario, palabraActual, puntos, segundos,palabraEnPantallaAnteriorSS,setUP):
    defaultFontMenu= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_MENU)
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #menu desplegable
    if setUP == 1:
        color2= (232, 95, 99)
        pygame.draw.rect(screen, color2, pygame.Rect(660, 38, 120, 20),  2)
        pygame.draw.rect(screen, color2, pygame.Rect(660, 58, 120, 20),  2)
        if setVOL == 1:
            pygame.draw.rect(screen, color2, pygame.Rect(660, 78, 120, 20),  2)
            n=0
            for q in range(0,10):
                pygame.draw.rect(screen, color2, pygame.Rect(673+n, 84, 9, 8),  2)
                n=n+9
            i=0
            for t in range(0,volumen):
                pygame.draw.rect(screen, color2, pygame.Rect(675+i, 86, 7, 4),  4)
                i=i+9
            screen.blit(defaultFont.render("+" , 1, color2), (765, 78))
            screen.blit(defaultFont.render("-" , 1, color2), (664, 78))
        screen.blit(defaultFontMenu.render("Menu Principal" , 1, color2), (675, 42))
        screen.blit(defaultFontMenu.render("Volumen" , 1, color2), (692, 62))
    #Linea Horizontal
    pygame.draw.line(screen, (0,0,0), (0, ALTO-90) , (ANCHO, ALTO-90), 5)
    #Linea Vertical
    pygame.draw.line(screen, (0,0,0), (ANCHO-600, ALTO-90) , (ANCHO-600, ALTO), 5)
    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_NEGRO), (ANCHO-580, ALTO-56))
    #palabra ingresar:
    screen.blit(defaultFont.render('INGRESAR:', 1, COLOR_NEGRO), (ANCHO-755, ALTO-56))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_NEGRO), (600, 10))
    #muestra el nivel
    screen.blit(defaultFont.render("Nivel " + str(nivel), 1, COLOR_NEGRO), (340, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_NEGRO)
    screen.blit(ren, (10, 10))

    #muestra la palabra
    screen.blit(defaultFontGrande.render(palabraActual, 1, COLOR_NEGRO), (ANCHO//2-len(palabraActual)*TAMANNO_LETRA_GRANDE//4,ALTO-400))
    #muestra la palabra anterior
    screen.blit(defaultFont.render(palabraEnPantallaAnteriorSS, 1, COLOR_CORRECTOLVL3), (ANCHO//2-len(palabraEnPantallaAnteriorSS)*TAMANNO_LETRA//4,ALTO-150))


def dibujar4(volumen,setVOL,nivel,screen, palabraUsuario, palabraActual, puntos, segundos,palabraEnPantallaAnteriorSS,setUP):
    defaultFontMenu= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_MENU)
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #menu desplegable
    if setUP == 1:
        color2= (232, 95, 99)
        pygame.draw.rect(screen, color2, pygame.Rect(660, 38, 120, 20),  2)
        pygame.draw.rect(screen, color2, pygame.Rect(660, 58, 120, 20),  2)
        if setVOL == 1:
            pygame.draw.rect(screen, color2, pygame.Rect(660, 78, 120, 20),  2)
            n=0
            for q in range(0,10):
                pygame.draw.rect(screen, color2, pygame.Rect(673+n, 84, 9, 8),  2)
                n=n+9
            i=0
            for t in range(0,volumen):
                pygame.draw.rect(screen, color2, pygame.Rect(675+i, 86, 7, 4),  4)
                i=i+9
            screen.blit(defaultFont.render("+" , 1, color2), (765, 78))
            screen.blit(defaultFont.render("-" , 1, color2), (664, 78))
        screen.blit(defaultFontMenu.render("Menu Principal" , 1, color2), (675, 42))
        screen.blit(defaultFontMenu.render("Volumen" , 1, color2), (692, 62))

    #Linea Horizontal
    pygame.draw.line(screen, (0,0,0), (0, ALTO-90) , (ANCHO, ALTO-90), 5)
    #Linea Vertical
    pygame.draw.line(screen, (0,0,0), (ANCHO-600, ALTO-90) , (ANCHO-600, ALTO), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_NEGRO), (ANCHO-580, ALTO-56))
    #palabra ingresar:
    screen.blit(defaultFont.render('INGRESAR:', 1, COLOR_NEGRO), (ANCHO-755, ALTO-56))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_NEGRO), (600, 10))
    #muestra el nivel
    screen.blit(defaultFont.render("Nivel " + str(nivel), 1, COLOR_NEGRO), (340, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_NEGRO)
    screen.blit(ren, (10, 10))

    #muestra la palabra
    screen.blit(defaultFontGrande.render(palabraActual, 1, COLOR_NEGRO), (ANCHO//2-len(palabraActual)*TAMANNO_LETRA_GRANDE//4,ALTO-400))
    #muestra la palabra anterior
    screen.blit(defaultFont.render(palabraEnPantallaAnteriorSS, 1, COLOR_CORRECTO), (ANCHO//2-len(palabraEnPantallaAnteriorSS)*TAMANNO_LETRA//4,ALTO-150))



def dibujarF(nivel,screen, palabraUsuario, palabraActual, puntos,palabraEnPantallaAnteriorSS):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    surface = screen

    #muestra palabra
    screen.blit(defaultFont.render('Volver a Jugar', 1, (0,0,180)), (ANCHO-480,ALTO-166))
    #muestra palabra
    screen.blit(defaultFontGrande.render('GANASTE', 1, COLOR_NEGRO), (ANCHO-600,ALTO-320))

def dibujarP(nivel,screen, palabraUsuario, palabraActual, puntos,palabraEnPantallaAnteriorSS):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    surface = screen

    #muestra palabra
    screen.blit(defaultFont.render('Volver a Jugar', 1, (0,0,180)), (ANCHO-480,ALTO-166))
    #muestra palabra
    screen.blit(defaultFontGrande.render('PERDISTE', 1, COLOR_NEGRO), (ANCHO-630,ALTO-320))

