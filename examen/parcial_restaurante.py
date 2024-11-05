"""
El restaurante Sabores de mi tierra está solicitando crear un programa que permita recibir pedidos de los clientes y que calcule su precio de forma automática. 
El restaurante ofrece tres tipos de platos principales: Carne, Pollo y Vegetariano. Dependiendo del plato que el cliente elija, se le ofrecerán diferentes opciones adicionales.
A continuación en la tabla se presentan las diferentes opciones para cada plato:
TABLA DE OPCIONES
El precio del pedido del cliente se calcula con base en la TABLA DE PRECIOS. 
"""

plato_principal = int(input("Elige el plato principal:\n1. Carne\n2. Pollo\n3. Vegetariano\n"))
precio = 0

if plato_principal == 1:
    tipo_proteina = int(input("Elige cómo deseas la carne:\n1. Término medio\n2. Bien cocida\n"))
    if tipo_proteina == 1:
        precio += 25000
    elif tipo_proteina == 2:
        precio += 25000
    else: 
        precio += 0 
    acompañamiento = int(input("Elige el acompañamiento:\n1. Papas fritas\n2. Ensalada\n3. Arroz\n"))
    if acompañamiento == 1:
        precio += 2000
    else:
        precio += 0
    bebida = int(input("Elige la bebida que deseas:\n1. Soda\n2. Jugo natural\n3. Limonada\n"))
    if bebida == 1:
        precio += 5000
    elif bebida == 2:
        precio += 3000
    elif bebida == 3:
        precio += 2500
    else:
        precio += 0
    

if plato_principal == 2:
    tipo_proteina = int(input("Elige cómo deseas el pollo:\n1. Frito\n2. A la plancha\n"))
    if tipo_proteina == 1:
        precio += 20000
    elif tipo_proteina == 2:
        precio += 23000
    else: 
        precio += 0 
    acompañamiento = int(input("Elige el acompañamiento:\n1. Papas fritas\n2. Ensalada\n3. Arroz\n"))
    if acompañamiento == 1:
        precio += 2000
    else:
        precio += 0
    bebida = int(input("Elige la bebida que deseas:\n1. Soda\n2. Jugo natural\n3. Limonada\n"))
    if bebida == 1:
        precio += 5000
    elif bebida == 2:
        precio += 3000
    elif bebida == 3:
        precio += 2500
    else:
        precio += 0

if plato_principal == 3:
    tipo_proteina = int(input("Elige lo que deseas:\n1. Ensalada\n2. Tofu\n"))
    if tipo_proteina == 1:
        precio += 18000
    elif tipo_proteina == 2:
        precio += 20000
    else: 
        precio += 0 
    acompañamiento = int(input("Elige el acompañamiento:\n1. Quinoa\n2. Vegetales al vapor\n"))
    if acompañamiento == 1:
        precio += 3000
    else:
        precio += 0
    bebida = int(input("Elige la bebida que deseas:\n1. Jugo natural\n2. Agua\n"))
    if bebida == 1:
        precio += 3000
    elif bebida == 2:
        precio += 1000
    else:
        precio += 0


postre = int(input("¿Postre?\n1. No desea postre\n2. Flan\n3. Brownie\n4. Helado\n"))
if postre == 1:
    precio += 0
elif postre == 2:
    precio += 6000
elif postre == 3:
    precio += 7000
elif postre == 4:
    precio += 5000
else:
    precio += 0

tamaño_porcion = int(input("Indique el tamaño de la porción que desea:\n1.Pequeña\n2. Normal\n3. Grande\n"))
if tamaño_porcion == 1:
    precio_total = precio-(precio*0.1)
if tamaño_porcion == 2:
    precio_total = precio
elif tamaño_porcion == 3:
    precio_total = precio+(precio*0.2)

print("Debe pagar", precio_total)


