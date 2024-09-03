# Pedir al usuario que ingrese el año
print("Ingrese un año para saber si es bisiesto")
year = int(input()) # Variable para almacenar el año
# Condición padre
# Validar si es uniformemente divisible por 4
if year % 4 == 0: 
    # Condición paso 2
    # Validar si es uniformemete divisible por 100
    if year % 100 == 0:
        # Condición paso 3
        # Validar si es uniformemente divisible por 400
        if year % 400 == 0:
            # Paso 4
            print("El año es bisiesto")
        else:
            # Paso 5
            print("El año NO es bisiesto")
    else:
        # Paso 4
        print("El año es bisiesto")
else:
    print("El año NO es bisiesto")