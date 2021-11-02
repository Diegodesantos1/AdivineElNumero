import random
numero=random.randint (0,99)

int(numero)

print("Dime un número")
num=int(input())
n_intentos=1
while num != numero:
    if numero < num:
        print("Te has pasado, selecciona otro número")
        num=int(input())
        n_intentos += 1
    if numero > num:
        print("Te has quedado corto, selecciona otro número")
        num=int(input())
        n_intentos += 1
if numero == num:
    print("¡Has acertado, enhorabuena!")
    print(f"Has necesitado {n_intentos} intentos")

