# AdivineElNumero

Mi dirección de Github es la siguiente: [Github] (https://github.com/Diegodesantos1/AdivineElNumero)

He resuelto el juego de adivinar valores enteros en función del nivel de dificultad que decidas y en cada caso puedes elegir si lo quieres resolver tú o una Inteligencia Artificial, al finalizar aparecerás en una tabla final con la puntuación correspondiente en función al número de intentos.

El diagrama de flujo que he realizado para este código es:
[Diagrama de flujo de adivinar el número]
<br>
<img height="700" src="https://github.com/Diegodesantos1/AdivineElNumero/blob/main/AdivinarN%C3%BAmeroFlowchart.png" />
<br>

El código empleado para resolverlo es el siguiente:


```#Importamos random
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
    print("Has seleccionado el nivel simple, tienes que adivinar un número del 0 al 100 y sólo tienes 10 intentos")
    numIA= random.randint (0,100)
    print(numIA)
    n_intentos=1
    n_intentos_max=10
    while numIA != numeroAadivinar and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos} intentos")
        if numeroAadivinar < numIA:
            print("Te has pasado, selecciona otro número menor")
            numIA= random.randint (numeroAadivinar,(numIA - 1)) #Pongo -1 para evitar que repita número
            print(numIA)
            n_intentos += 1
        elif numeroAadivinar > numIA:
            print("Te has quedado corto, selecciona otro número mayor")
            numIA= random.randint ((numIA + 1),numeroAadivinar) #Pongo +1 para evitar que repita número
            print(numIA)
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numeroAadivinar == numIA:
        print(f"¡Has acertado, enhorabuena, has necesitado {n_intentos} intentos!")
if eleccionnivel ==1 and eleccionjugador == 2:
    numero=random.randint (0,100)
    print("Has seleccionado el nivel simple, tienes que adivinar un número del 0 al 100 y sólo tienes 10 intentos")
    print("Dime un número")
    num=int(input())
    n_intentos=1
    n_intentos_max=10
    while num != numero and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos} intentos")
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
    print("Has seleccionado el nivel Intermedio, tienes que adivinar un número del 0 al 1000 y sólo tienes 25 intentos")
    numIA= random.randint (0,1000)
    n_intentos_max=25
    n_intentos=1
    while numIA != numeroAadivinar and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos} intentos")
        if numeroAadivinar < numIA:
            print("Te has pasado, selecciona otro número menor")
            numIA= random.randint (numeroAadivinar,(numIA - 1)) #Pongo -1 para evitar que repita número
            print(numIA)
            n_intentos += 1
        elif numeroAadivinar > numIA:
            print("Te has quedado corto, selecciona otro número mayor")
            numIA= random.randint ((numIA + 1),numeroAadivinar) #Pongo +1 para evitar que repita número
            print(numIA)
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numeroAadivinar == numIA:
        print(f"¡Has acertado, enhorabuena, has necesitado {n_intentos} intentos!")
if eleccionnivel ==2 and eleccionjugador == 2:
    numero=random.randint (0,1000)
    print("Has seleccionado el nivel Intermedio, tienes que adivinar un número del 0 al 1000 y sólo tienes 25 intentos")
    print("Dime un número")
    num=int(input())
    n_intentos_max=25
    n_intentos=1
    while num != numero and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos} intentos")
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
    print("Has seleccionado el nivel Avanzado, tienes que adivinar un número del 0 al 1.000.000 y sólo tienes 50 intentos")
    numIA=random.randint (0,1000000)
    n_intentos=1
    n_intentos_max=50
    while numIA != numeroAadivinar and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos} intentos")
        if numeroAadivinar < numIA:
            print("Te has pasado, selecciona otro número menor")
            numIA= random.randint (numeroAadivinar,(numIA - 1)) #Pongo -1 para evitar que repita número
            print(numIA)
            n_intentos += 1
        elif numeroAadivinar > numIA:
            print("Te has quedado corto, selecciona otro número mayor")
            numIA= random.randint ((numIA + 1),numeroAadivinar) #Pongo +1 para evitar que repita número
            print(numIA)
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numeroAadivinar == numIA:
        print(f"¡Has acertado, enhorabuena, has necesitado {n_intentos} intentos!")
if eleccionnivel ==3 and eleccionjugador == 2:
    numero=random.randint (0,1000000)
    print("Has seleccionado el nivel Avanzado, tienes que adivinar un número del 0 al 1.000.000 y sólo tienes 50 intentos")
    print("Dime un número")
    num=int(input())
    n_intentos=1
    n_intentos_max=50
    while num != numero and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos} intentos")
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
    print("Has seleccionado el nivel Experto, tienes que adivinar un número del 0 al 1.000.000.000.000 y sólo tienes 100 intentos")
    numIA=random.randint (0,1000000000000)
    n_intentos=1
    n_intentos_max=100
    while numIA != numeroAadivinar and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos} intentos")
        if numeroAadivinar < numIA:
            print("Te has pasado, selecciona otro número menor")
            numIA= random.randint (numeroAadivinar,(numIA - 1)) #Pongo -1 para evitar que repita número
            print(numIA)
            n_intentos += 1
        elif numeroAadivinar > numIA:
            print("Te has quedado corto, selecciona otro número mayor")
            numIA=random.randint ((numIA + 1),numeroAadivinar) #Pongo +1 para evitar que repita número
            print(numIA)
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numeroAadivinar == numIA:
        print(f"¡Has acertado, enhorabuena, has necesitado {n_intentos} intentos!")
if eleccionnivel ==4 and eleccionjugador == 2:
    numero=random.randint (0,1000000000000)
    print("Has seleccionado el nivel Experto, tienes que adivinar un número del 0 al 1.000.000.000.000 y sólo tienes 100 intentos")
    print("Dime un número")
    num=int(input())
    n_intentos=1
    n_intentos_max=100
    while num != numero and n_intentos < n_intentos_max: #Establezco el bucle
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos} intentos")
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
