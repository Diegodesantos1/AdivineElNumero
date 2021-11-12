#Importamos random
import random
from tabulate import tabulate
#Defino la función de seleccionar el nivel de dificultad, como la IA lo hace automático, aumento el número de intentos en cada caso
def seleccion_nivel():
    print("Selecciona el nivel de dificultad")
    print("\n 1:Simple"+ "\n 2:Intermedio" + "\n 3:Avanzado" + "\n 4:Experto")
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
def realizarjuego():
    print("Escriba 1 para que juegue la IA")
    print("Escriba 2 para jugar tú")
    jugador=int(input())
    eleccionjugador = jugador
    if 0< eleccionjugador <=2:
        if eleccionjugador == 1:
            print("Has elegido que juegue la IA")
        elif eleccionjugador == 2:
            print("Has elegido tú")
    else:
        print("Nivel no válido")
    if jugador == 1:
        numIA= random.randint(min,max) #Esto se definirá más adelante.
        n_intentos = 0
        while n_intentos < n_intentos_max:
            print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos} intentos")
            n_intentos += 1
            if numero < numeroAadivinar:
                print("Te has quedado corto, selecciona otro número mayor")
            if numero > numeroAadivinar:
                print("Te has pasado, selecciona otro número menor")
            if numero == numeroAadivinar:
                break
        if numero == numeroAadivinar:
            print(f"¡Has acertado, enhorabuena, has necesitado {n_intentos} intentos!")
            puntuacion = n_intentos_max - n_intentos
            print("¿Dime tu nombre")
            nombre="IA"
            table = [['Nombre', 'Nivel de dificultad', 'Puntuación'],[nombre, eleccionnivel,puntuacion]]
            print(tabulate(table, headers='firstrow', tablefmt='grid'))
        if numero != numeroAadivinar :
            print("Se te han acabado los intentos, derrota")
















if eleccionnivel ==1: #Nivel simple
    seleccion_jugador()
    if eleccionjugador ==1:
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
    elif eleccionjugador ==2:
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
if eleccionnivel ==2: #Nivel intermedio
    seleccion_jugador()
    if seleccion_jugador ==1:
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
    elif seleccion_jugador == 2:
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
if eleccionnivel ==3: #Nivel difícil
    seleccion_jugador()
    if seleccion_jugador == 1:
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
    elif seleccion_jugador == 2:
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
if eleccionnivel ==4: #Nivel avanzado
    seleccion_jugador()
    if seleccion_jugador == 1:
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
    elif seleccion_jugador == 2:
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
table = [['Nombre', 'Nivel de dificultad', 'Puntuación'],[nombre, eleccionnivel,puntuacion]]
print(tabulate(table, headers='firstrow', tablefmt='grid'))