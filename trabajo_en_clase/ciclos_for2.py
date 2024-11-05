"""
Crea un programa que muestre la tabla de multiplicar de un número ingresado por el usuario.
"""
print("Ingrese un número")
numero = int(input())
for i in range(1, 13):
    print(f"{numero}x{i}={numero*i}")