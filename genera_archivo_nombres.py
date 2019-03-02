import string
import random

def genera_string_aleatorio():

    letras_Up = list(string.ascii_uppercase)
    letras_Down = list(string.ascii_lowercase)
    tammano = len(letras_Down)
    aleatorio = random.randrange(tammano)
    cadena = letras_Up[aleatorio]
    for i in range(random.randrange(5,14)):
        aleatorio = random.randrange(tammano)
        cadena += letras_Down[aleatorio]
    return cadena

def genera_numero_aleatorio():

    digits = list(string.digits)
    numero = ""
    for i in range(8):
        aleatorio = random.randrange(10)
        numero += digits[aleatorio]
    return numero


with open('datos.txt', 'w') as datos:
    for i in range(10):
        escritura = genera_string_aleatorio() + "," + genera_string_aleatorio() + "," + genera_numero_aleatorio() + "\n"
        datos.writelines(escritura)

with open('datos.txt','r') as datos:
    print(datos.read())
