while True:
    print("1. Saludar\n2. Decir adiós")
    opcion = int(input())
    if opcion == 1:
        print("Hola :)")
    elif opcion == 2:
        print("Adiós")
        break
    else: 
        print("Opción inválida")
