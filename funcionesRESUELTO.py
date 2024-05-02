from principal2 import *
from configuracion import *
import random
import math


def lectura(archivo, salida):
    salida=[]
    f=open('lemario.txt','r')
    lineas=f.readlines()
    for linea in lineas:
        salida.append(linea)
    f.close()
    return salida

def nuevaPalabra(lista):
    lista=[]
    cadena=''
    cadena2=''
    f=open('lemario.txt','r')
    lineas=f.readlines()
    for linea in lineas:
        lista.append(linea)
    alAzar=random.randrange(len(lista))
    cadena=cadena+lista[alAzar]
    for letra in range(len(cadena)-1):
        cadena2=cadena2+cadena[letra]
    f.close()
    return cadena2

def nuevaPalabraConDificultad(lista,dificultad):
    cadena=nuevaPalabra(lista)
    if(dificultad == 1):
        while len(cadena)>5:
            cadena=nuevaPalabra(lista)

    if(dificultad == 2):
        while len(cadena)<6 or len(cadena)>9:
            cadena=nuevaPalabra(lista)

    if(dificultad == 3):
        while 10>len(cadena):
            cadena=nuevaPalabra(lista)

    return cadena


def silabasTOpalabra(silaba):
    palabra=''
    for letra in silaba:
        if letra!='-':
            palabra=palabra+letra
    return palabra

def palabraEspacioAGuion(palabraSeparadaEnSilabas):
    nuevaPalabra=''
    for letra in palabraSeparadaEnSilabas:
        if letra==' ':
            nuevaPalabra=nuevaPalabra+'-'
        else:
            nuevaPalabra=nuevaPalabra+letra
    return nuevaPalabra



def palabraTOsilaba(palabra):
    palabra=separador(palabra)
    return palabra


def esCorrecta(palabraEnSilabasEnPantalla, palabra):
    if(palabraEnSilabasEnPantalla==palabraEspacioAGuion(palabra)):
        return True

def puntaje(palabra):
    return 5

def crearBoton(screen,boton,palabra,colorBoton,colorLetraBoton):

    if pygame.mouse.get_pos()==True:
        draw.rect(screen,colorBoton, boton, 0)
    else:
        draw.rect(screen,colorBoton,boton, 1)
    texto=myFont.render(palabra, True, colorLetraBoton)
    screen.blit(texto, (boton.x+(boton.width-texto.get_width())/2,boton.y+(aceptar.height-texto.get_height())/2))
