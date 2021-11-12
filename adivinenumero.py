#Importamos random
import random
#Defino la función de seleccionar el nivel de dificultad
def seleccion_nivel():
    print("Selecciona el nivel de dificultad: \n")
    print("\n 1:Simple"+ "\n 2:Intermedio" + "\n 3:Avanzado" + "\n 4:Experto")
    nivel=int(input())
    global eleccionnivel
    eleccionnivel = nivel
    if 0< eleccionnivel <=4:
        if eleccionnivel ==1:
            print("Has elegido el nivel simple, tienes que adivinar un número del 0 al 100 y sólo tienes 20 intentos")

        elif eleccionnivel ==2:
            print("Has elegido el nivel intermedio, tienes que adivinar un número del 0 al 1000 y sólo tienes 40 intentos")

        elif eleccionnivel ==3:
            print("Has elegido el nivel avanzado, tienes que adivinar un número del 0 al 1.000.000 y sólo tienes 80 intentos")

        elif eleccionnivel ==4:
            print("Has elegido el nivel experto, tienes que adivinar un número del 0 al 1.000.000.000.000 y sólo tienes 160 intentos")
    else:
        print("Nivel no válido")
seleccion_nivel()

if eleccionnivel ==1:
    numero=random.randint (0,100)
    print("Dime un número")
    num=int(input())
    n_intentos=1
    n_intentos_max=20
    while num != numero and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos}")
        if numero < num:
            print("Te has pasado, selecciona otro número menor")
            num=int(input())
            n_intentos += 1
        elif numero > num:
            print("Te has quedado corto, selecciona otro número mayor")
            num=int(input())
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numero == num:
        print(f"¡Has acertado, enhorabuena, has necesitado {n_intentos} intentos!")
#En cada intento te indica el programa si estas por debajo o encima y los intentos que llevas y te quedan

if eleccionnivel ==2:
    numero=random.randint (0,1000)
    print("Dime un número")
    num=int(input())
    n_intentos_max=40
    n_intentos=1
    while num != numero and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos}")
        if numero < num:
            print("Te has pasado, selecciona otro número menor")
            num=int(input())
            n_intentos += 1
        elif numero > num:
            print("Te has quedado corto, selecciona otro número mayor")
            num=int(input())
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numero == num:
        print(f"¡Has acertado, enhorabuena, has necesitado {n_intentos} intentos!")
#En cada intento te indica el programa si estas por debajo o encima y los intentos que llevas y te quedan
if eleccionnivel ==3:
    numero=random.randint (0,1000000)
    print("Dime un número")
    num=int(input())
    n_intentos=1
    n_intentos_max=80
    while num != numero and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos}")
        if numero < num:
            print("Te has pasado, selecciona otro número menor")
            num=int(input())
            n_intentos += 1
        elif numero > num:
            print("Te has quedado corto, selecciona otro número mayor")
            num=int(input())
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numero == num:
        print(f"¡Has acertado, enhorabuena, has necesitado {n_intentos} intentos!")
#En cada intento te indica el programa si estas por debajo o encima y los intentos que llevas y te quedan
if eleccionnivel ==4:
    numero=random.randint (0,1000000000000)
    print("Dime un número")
    num=int(input())
    n_intentos=1
    n_intentos_max=160
    while num != numero and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos}")
        if numero < num:
            print("Te has pasado, selecciona otro número menor")
            num=int(input())
            n_intentos += 1
        elif numero > num:
            print("Te has quedado corto, selecciona otro número mayor")
            num=int(input())
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numero == num:
        print(f"¡Has acertado, enhorabuena, has necesitado {n_intentos} intentos!")
#En cada intento te indica el programa si estas por debajo o encima y los intentos que llevas y te quedan

#En cada nivel de dificultad se van duplicando los intentos, fácil=20, intermedio=40, difícil= 80 y Experto = 160
puntuacion=n_intentos_max-n_intentos
print("¿Cuál es tu nombre?")
nombre=str(input())
from tabulate import tabulate
table = [['Nombre', 'Nivel de dificultad', 'Puntuación'],[nombre, eleccionnivel,puntuacion]]
print(tabulate(table, headers='firstrow', tablefmt='grid'))
