"""
Crea un programa que imprima todos los números pares en un rango que el usuario determine.
"""
print("Ingrese el número inicial")
rango_inicio = int(input())
print("Ingrese el número final")
rango_fin = int(input())
for i in range(rango_inicio, rango_fin, 2):
    # condición para validar si se inicia en un número par o impar
    if i%2 == 0:
        print(i)
    else:
        print(i+1)
    