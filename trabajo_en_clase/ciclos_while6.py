"""
Crea un programa que seleccione un número aleatorio y pida al usuario que ingrese un número hasta que  adivine el número elegido por el programa.
"""
import random as rn
numero = rn.randint(0, 100)
while True:
    adivinar_numero = int(input("Ingresa un número\n"))
    if adivinar_numero > numero:
        print("El número que ingresaste es mayor. Vuelve a intentarlo")
    elif adivinar_numero < numero:
        print("El número que ingresaste es menor. Vuelve a intentarlo")
    else:
        print("¡Felicitaciones! Adivinaste el número")