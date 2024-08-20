# Pedir los lados del triángulo
print("Ingrese el lado 1")
lado1 = float(input())
print("Ingrese el lado 2")
lado2 = float(input())
print("Ingrese el lado 3")
lado3 = float(input())
# Condicionales
# Condición para triángulo equilátero
if lado1 == lado2 == lado3:
    print("El triángulo es equilátero")
# Condición para triángulo isósceles
elif (lado1 == lado2 and lado1 != lado3) or (lado1 == lado3 and lado1 != lado2) or (lado2 == lado3 and lado2 != lado1):
    print("El triángulo es isósceles")
# Condición para triángulo escaleno
else:
    print("El triángulo es escaleno")