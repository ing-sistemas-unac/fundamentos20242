"""
Crea un programa que imprima un contador regresivo desde un número que ingrese el usuario hasta 1.
"""
print("Ingrese un número")
numero = int(input())
while numero >= 1:
    if numero == 1:
        print(numero, end=". ")
    else:
        print(numero, end=", ")
    numero -= 1
