#Importo lo necesario
import random
numero=random.randint (0,99)
#Mensaje de selección del nivel de difiultad
print("Selecciona el nivel de dificultad 1:Simple, 2:Intermedio, 3:Avanzado, 4:Experto")
nivel=int(input())

if nivel ==1:
    print("Has seleccionado el nivel simple")
    int(numero)
    print("Dime un número")
    num=int(input())
    n_intentos=1
    while num != numero:
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

