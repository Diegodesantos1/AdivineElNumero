#Mensaje de selección del nivel de difiultad
print("Selecciona el nivel de dificultad 1:Simple, 2:Intermedio, 3:Avanzado, 4:Experto")
nivel=int(input())

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

if nivel ==3:
    import random
    numero=random.randint (0,1000000)
    print("Has seleccionado el nivel Intermedio, tienes que adivinar un número del 0 al 1.000.000 y sólo tienes 80 intentos")
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

