# función que no tiene parámetros y no retorna nada
def decir_hola():
    print("¡Hola!")
# llamar a la función 
decir_hola()

# función que no tiene parámetros y retorna "¡Hola!"
def decir_hola():
    return "¡Hola!"
# llamar a la función 
print(decir_hola())

# función que recibe un parámetro y no retorna nada
def saludar_a(nombre):
    print("Hola", nombre)
# llamar a la función
saludar_a("Juan David")

# función que recibe un parámetro y retorna un saludo personalizado
def saludar_a(nombre):
    return "Hola " + nombre
# llamar a la función
print(saludar_a("Juan David"))

# función que recibe múltiples parámetros y retorna un saludo personalizado
def saludo_personalizado(momento, nombre, apellido):
    return momento + " " + nombre + " " + apellido
# llamar a la función pidiendo que se ingresen por teclado los datos
momento = input("ingrese el saludo que quiere dar ")
nombre = input("ingrese el nombre ")
apellido = input("ingrese el apellido ")
print(saludo_personalizado(momento, nombre, apellido))
