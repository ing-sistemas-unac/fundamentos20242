# Pedir los ángulos del triángulo
print("Ingrese el ángulo a (solo números)")
angulo_a = float(input())
print("Ingrese el ángulo b (solo números")
angulo_b = float(input())
print("Ingrese el ángulo c (solo números")
angulo_c = float(input())
# Condicionales 
if angulo_a < 0 or angulo_b < 0 or angulo_c < 0: 
    print("No puede ingresar valores negativos")
elif (angulo_a + angulo_b + angulo_c) > 180 or angulo_a == 0 or angulo_b == 0 or angulo_c == 0:
    print("Los valores ingresados no son los de un triángulo")
elif angulo_a == 90 or angulo_b == 90 or angulo_c == 90:
    print("El triángulo es rectángulo")
elif angulo_a < 90 and angulo_b < 90 and angulo_c < 90:
    print("El triángulo es acutángulo")
elif angulo_a > 90 or angulo_b > 90 or angulo_c > 90:
    print("El triángulo es obtusángulo")
else: 
    print("Error")
