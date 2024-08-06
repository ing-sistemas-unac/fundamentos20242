# Este programa suma dos números
# Se importa la librería colorama para dar estilos al texto en consola
from colorama import init, Fore, Style
init()
# Se piden al usuario los dos números
print(Fore.BLUE + "Ingrese el primer número = ")
numero1 = int(input())
print(Fore.CYAN + "Ingrese el segundo número = ")
numero2 = int(input())
# Se calcula la suma
suma = numero1 + numero2
# Se muestra el resultado
print(Fore.GREEN + "El resultado es", suma)



