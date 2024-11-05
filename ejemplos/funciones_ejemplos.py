# función sin parámetros o retorno de valores
def decir_hola():
  print("Hello!")

decir_hola()  # llamada a la función, 'Hello!' se muestra en la consola

# función con un parámetro
def hola_con_nombre(name):
  print("Hello " + name + "!")

hola_con_nombre("Eva")  # llamada a la función, 'Hello Eva!' se muestra en la consola

# función con múltiples parámetros con una sentencia de retorno
def multiplicar(val1, val2):
  return val1 * val2

print(multiplicar(3, 5))  # muestra 15 en la consola

