"""
Crea una función llamada “buscar_palabra(lista_palabras, palabra)” que tome una lista de palabras y una palabra específica como parámetros, y devuelva la cantidad de veces que la palabra aparece en la lista.
"""
lista_palabras = [
    "gato", "perro", "casa", "gato", "sol", "luna", "cielo", "mar", "perro", "árbol", 
    "flor", "lago", "rio", "montaña", "sol", "fuego", "luna", "fuego", "estrella", "mar", "perro", "gato", "fuego", "rio", "casa", "cielo", "árbol", "luna", "sol", "estrella", "montaña", "lago", "rio", "casa", "flor", "cielo", "estrella", "árbol", "fuego", "sol", "montaña", "flor", "lago", "gato", "estrella", "cielo", "mar", "luna", "perro", "casa"
]

# función para contar las veces que aparece una palabra en la lista
def buscar_palabra(lista_palabras, palabra):
    cantidad = 0
    # ciclo para recorrer todas las palabras de la lista
    for item in lista_palabras:
        # si la palabra es igual a la que se tiene en ese momento en la variable "item", se suma 1 a la variable "cantidad"
        if item == palabra:
            cantidad += 1
    # retornar la cantidad de veces que aparece la palabra en la lista
    return cantidad

while True: 
    opcion = int(input("Digite 1 para buscar una palabra o digite 0 para salir\n"))
    if opcion == 1:
        # llamado a la función
        palabra_usuario = input("Ingrese la palabra que desea contar\t")
        if buscar_palabra(lista_palabras, palabra_usuario) == 0:
            print("La palabra no se encuentra en la lista")
        else: 
            print(palabra_usuario, "=" , buscar_palabra(lista_palabras, palabra_usuario))
    elif opcion == 0:
        break
    else:
        print("Ingrese una opción válida")


