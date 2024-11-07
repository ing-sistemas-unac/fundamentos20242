"""
asdfghjklkjhccghjk
3
"""
cadena = "asdfghjklkjhccghjk"
longitud = 4

contador = 0

for i in range(len(cadena)):
    if contador < longitud:
        print(cadena[i], end=" ")
        contador += 1
    elif contador == longitud:
        contador = 0
        print("")
    
    
