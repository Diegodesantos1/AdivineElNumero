#Importamos random
import random
#Defino la función de seleccionar el nivel de dificultad, como la IA lo hace automático, aumento el número de intentos en cada caso
def seleccion_nivel():
    print("Selecciona el nivel de dificultad")
    print("1:Simple")
    print("2:Intermedio")
    print("3:Avanzado")
    print("4:Experto")
    nivel=int(input())
    global eleccionnivel
    eleccionnivel = nivel
    if 0< eleccionnivel <=4:
        if eleccionnivel ==1:
            print("Has elegido el nivel simple")

        elif eleccionnivel ==2:
            print("Has elegido el nivel intermedio")

        elif eleccionnivel ==3:
            print("Has elegido el nivel avanzado")

        elif eleccionnivel ==4:
            print("Has elegido el nivel experto")
    else:
        print("Nivel no válido")
seleccion_nivel()

def seleccion_jugador():
    print("Escriba 1 para que juegue la IA")
    print("Escriba 2 para jugar tú")
    jugador=int(input())
    global eleccionjugador
    eleccionjugador = jugador
    if 0< eleccionjugador <=2:
        if eleccionnivel == 1:
            print("Has elegido que juegue la IA")
        elif eleccionjugador == 2:
            print("Has elegido tú")
    else:
        print("Nivel no válido")
seleccion_jugador()
if eleccionnivel ==1 and eleccionjugador == 1:
    numeroAadivinar=random.randint (0,100)
    print("Has seleccionado el nivel simple, tienes que adivinar un número del 0 al 100 y sólo tienes 20 intentos")
    int(numeroAadivinar)
    numIA= random.randint (0,100)
    print(numIA)
    n_intentos=1
    n_intentos_max=100
    while numIA != numeroAadivinar and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos}")
        if numeroAadivinar < numIA:
            print("Te has pasado, selecciona otro número menor")
            numIA= random.randint (0,numIA)
            print(numIA)
            n_intentos += 1
        elif numeroAadivinar > numIA:
            print("Te has quedado corto, selecciona otro número mayor")
            numIA= random.randint (numIA,100)
            print(numIA)
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numeroAadivinar == numIA:
        print(f"¡Has acertado, enhorabuena, has necesitado {n_intentos} intentos!")
if eleccionnivel ==1 and eleccionjugador == 2:
    numero=random.randint (0,100)
    print("Has seleccionado el nivel simple, tienes que adivinar un número del 0 al 100 y sólo tienes 20 intentos")
    int(numero)
    print("Dime un número")
    num=int(input())
    n_intentos=1
    n_intentos_max=100
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

if eleccionnivel ==2 and eleccionjugador == 1:
    numeroAadivinar=random.randint (0,1000)
    print("Has seleccionado el nivel Intermedio, tienes que adivinar un número del 0 al 1000 y sólo tienes 40 intentos")
    int(numeroAadivinar)
    numIA= random.randint (0,1000)
    n_intentos_max=1000
    n_intentos=1
    while numIA != numeroAadivinar and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos}")
        if numeroAadivinar < numIA:
            print("Te has pasado, selecciona otro número menor")
            numIA= random.randint (0,numIA)
            print(numIA)
            n_intentos += 1
        elif numeroAadivinar > numIA:
            print("Te has quedado corto, selecciona otro número mayor")
            numIA= random.randint (numIA,1000)
            print(numIA)
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numeroAadivinar == numIA:
        print(f"¡Has acertado, enhorabuena, has necesitado {n_intentos} intentos!")
if eleccionnivel ==2 and eleccionjugador == 2:
    numero=random.randint (0,1000)
    print("Has seleccionado el nivel Intermedio, tienes que adivinar un número del 0 al 1000 y sólo tienes 40 intentos")
    int(numero)
    print("Dime un número")
    num=int(input())
    n_intentos_max=1000
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

if eleccionnivel ==3 and eleccionjugador == 1:
    numeroAadivinar=random.randint (0,1000000)
    print("Has seleccionado el nivel Avanzado, tienes que adivinar un número del 0 al 1.000.000 y sólo tienes 80 intentos")
    int(numeroAadivinar)
    numIA=random.randint (0,1000000)
    n_intentos=1
    n_intentos_max=2000
    while numIA != numeroAadivinar and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos}")
        if numeroAadivinar < numIA:
            print("Te has pasado, selecciona otro número menor")
            numIA= random.randint (0,numIA)
            print(numIA)
            n_intentos += 1
        elif numeroAadivinar > numIA:
            print("Te has quedado corto, selecciona otro número mayor")
            numIA= random.randint (numIA,1000000)
            print(numIA)
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numeroAadivinar == numIA:
        print(f"¡Has acertado, enhorabuena, has necesitado {n_intentos} intentos!")
if eleccionnivel ==3 and eleccionjugador == 2:
    numero=random.randint (0,1000000)
    print("Has seleccionado el nivel Avanzado, tienes que adivinar un número del 0 al 1.000.000 y sólo tienes 80 intentos")
    int(numero)
    print("Dime un número")
    num=int(input())
    n_intentos=1
    n_intentos_max=2000
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

if eleccionnivel ==4 and eleccionjugador == 1:
    numeroAadivinar=random.randint (0,1000000000000)
    print("Has seleccionado el nivel Experto, tienes que adivinar un número del 0 al 1.000.000.000.000 y sólo tienes 160 intentos")
    int(numeroAadivinar)
    numIA=random.randint (0,1000000000000)
    n_intentos=1
    n_intentos_max=5000
    while numIA != numeroAadivinar and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos}")
        if numeroAadivinar < numIA:
            print("Te has pasado, selecciona otro número menor")
            numIA=random.randint (0,numIA)
            print(numIA)
            n_intentos += 1
        elif numeroAadivinar > numIA:
            print("Te has quedado corto, selecciona otro número mayor")
            numIA=random.randint (numIA,1000000000000)
            print(numIA)
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numeroAadivinar == numIA:
        print(f"¡Has acertado, enhorabuena, has necesitado {n_intentos} intentos!")
if eleccionnivel ==4 and eleccionjugador == 2:
    numero=random.randint (0,1000000000000)
    print("Has seleccionado el nivel Experto, tienes que adivinar un número del 0 al 1.000.000.000.000 y sólo tienes 160 intentos")
    int(numero)
    print("Dime un número")
    num=int(input())
    n_intentos=1
    n_intentos_max=5000
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

puntuacion=n_intentos_max-n_intentos
if eleccionjugador ==1:
    nombre=("IA")
else:
    print("¿Dime tu nombre")
    nombre=str(input())
from tabulate import tabulate
table = [['Nombre', 'Nivel de dificultad', 'Puntuación'],[nombre, eleccionnivel,puntuacion]]
print(tabulate(table, headers='firstrow', tablefmt='grid'))