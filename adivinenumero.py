#Importo lo necesario
import random
numero=random.randint (0,99)
#Mensaje de selección del nivel de difiultad
print("Selecciona el nivel de dificultad 1:Simple, 2:Intermedio, 3:Avanzado, 4:Experto")
nivel=int(input())

if nivel ==1:
    print("Has seleccionado el nivel simple, tienes que adivinar un número del 0 al 99 y sólo tienes 20 intentos")
    int(numero)
    print("Dime un número")
    num=int(input())
    n_intentos=1
    while num != numero and n_intentos < 20:
        print(f"Llevas ya {n_intentos} intentos, cuidado")
        if numero < num:
            print("Te has pasado, selecciona otro número menor")
            num=int(input())
            n_intentos += 1
        if numero > num:
            print("Te has quedado corto, selecciona otro número mayor")
            num=int(input())
            n_intentos += 1
    if numero == num:
        print("¡Has acertado, enhorabuena!")
        print(f"Has necesitado {n_intentos} intentos")

