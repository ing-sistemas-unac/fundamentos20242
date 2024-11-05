"""
Crea un programa que solicite al usuario un número y calcule la suma de todos los números naturales hasta ese número.
"""
print("Ingrese un número")
numero = int(input())
suma = 0
for i in range(1, numero+1):
    print(f"{suma}+{i}={suma+i}")
    suma += i