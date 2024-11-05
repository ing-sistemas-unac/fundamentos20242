opcion = 1
while opcion != 0:
    # Imprimir menú
    print("1. Saludar\n2. Comer\n0. Salir")
    # Leer opción
    opcion = int(input())
    # Condiciones 
    if opcion == 1:
        print("Hola :)")
    elif opcion == 2:
        print("Comer :D")
    elif opcion == 0:
        print("Adiós")
    else:
        print("Opción inválida")
