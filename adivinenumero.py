#Mensaje de selección del nivel de dificultad
print("Selecciona el nivel de dificultad 1:Simple, 2:Intermedio, 3:Avanzado, 4:Experto")
nivel=int(input())
#En función del nivel seleccionado se ejecuta esa parte del código
if nivel ==1:
    import random
    numero=random.randint (0,100)
    print("Has seleccionado el nivel simple, tienes que adivinar un número del 0 al 100 y sólo tienes 20 intentos")
    int(numero)
    print("Dime un número")
    num=int(input())
    n_intentos=1
    n_intentos_max=20
    while num != numero and n_intentos < n_intentos_max:
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos}")
        if numero < num:
            print("Te has pasado, selecciona otro número menor")
            num=int(input())
            n_intentos += 1
        if numero > num:
            print("Te has quedado corto, selecciona otro número mayor")
            num=int(input())
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numero == num:
        print("¡Has acertado, enhorabuena!")
        print(f"Has necesitado {n_intentos} intentos")
#En cada intento te indica el programa si estas por debajo o encima y los intentos que llevas y te quedan

if nivel ==2:
    import random
    numero=random.randint (0,1000)
    print("Has seleccionado el nivel Intermedio, tienes que adivinar un número del 0 al 1000 y sólo tienes 40 intentos")
    int(numero)
    print("Dime un número")
    num=int(input())
    n_intentos_max=40
    n_intentos=1
    while num != numero and n_intentos < n_intentos_max:
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos}")
        if numero < num:
            print("Te has pasado, selecciona otro número menor")
            num=int(input())
            n_intentos += 1
        if numero > num:
            print("Te has quedado corto, selecciona otro número mayor")
            num=int(input())
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numero == num:
        print("¡Has acertado, enhorabuena!")
        print(f"Has necesitado {n_intentos} intentos")
#En cada intento te indica el programa si estas por debajo o encima y los intentos que llevas y te quedan
if nivel ==3:
    import random
    numero=random.randint (0,1000000)
    print("Has seleccionado el nivel Avanzado, tienes que adivinar un número del 0 al 1.000.000 y sólo tienes 80 intentos")
    int(numero)
    print("Dime un número")
    num=int(input())
    n_intentos=1
    n_intentos_max=80
    while num != numero and n_intentos < n_intentos_max:
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos}")
        if numero < num:
            print("Te has pasado, selecciona otro número menor")
            num=int(input())
            n_intentos += 1
        if numero > num:
            print("Te has quedado corto, selecciona otro número mayor")
            num=int(input())
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numero == num:
        print("¡Has acertado, enhorabuena!")
        print(f"Has necesitado {n_intentos} intentos")
#En cada intento te indica el programa si estas por debajo o encima y los intentos que llevas y te quedan
if nivel ==4:
    import random
    numero=random.randint (0,1000000000000)
    print("Has seleccionado el nivel Experto, tienes que adivinar un número del 0 al 1.000.000.000.000 y sólo tienes 160 intentos")
    int(numero)
    print("Dime un número")
    num=int(input())
    n_intentos=1
    n_intentos_max=160
    while num != numero and n_intentos < n_intentos_max:
        print(f"Llevas ya {n_intentos} intentos, cuidado, te quedan {n_intentos_max-n_intentos}")
        if numero < num:
            print("Te has pasado, selecciona otro número menor")
            num=int(input())
            n_intentos += 1
        if numero > num:
            print("Te has quedado corto, selecciona otro número mayor")
            num=int(input())
            n_intentos += 1
    if n_intentos >= n_intentos_max:
        print("Se te han acabado los intentos, derrota")
    if numero == num:
        print("¡Has acertado, enhorabuena!")
        print(f"Has necesitado {n_intentos} intentos")
#En cada intento te indica el programa si estas por debajo o encima y los intentos que llevas y te quedan

#En cada nivel de dificultad se van duplicando los intentos, fácil=20, intermedio=40, difícil= 80 y Experto = 160