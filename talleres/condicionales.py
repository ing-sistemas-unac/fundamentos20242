"""
Estos factores son condicionados por los siguientes requerimientos:
•	Si el inventario de materia prima es menor que 50%, no se debe fabricar ese producto.
•	Si la demanda de un producto es alta y el inventario es suficiente, se debe priorizar la fabricación de ese producto.
•	Si el costo de producción de un producto es alto y la demanda es baja, no se debe fabricar ese producto.
•	Si un producto tiene una prioridad estratégica alta, se debe fabricar independientemente del costo, siempre que el inventario lo permita.
•	Si el producto no cumple con las condiciones anteriores, se debe informar a la fábrica que por ahora no es viable realizar esa producción. 

El programa debería recibir como datos de entrada:
•	Nombre del producto
•	Inventario de materia prima para el producto (es un número que representará el porcentaje).
•	Demanda de cada producto (baja, media, alta).
•	Costo de producción de cada producto (bajo, medio, alto).
•	Prioridad estratégica de cada producto (baja, media, alta).

El programa debería mostrar si el producto debe fabricarse o no ese día, junto con una breve justificación de la decisión.
"""
print("Ingrese el nombre del producto\t")
nombre = input()
inventario = float(input("Ingrese el número de inventario de materia prima\t"))
demanda = input("Ingrese la demanda para este producto\t")
costo = input("Ingrese el costo de producción de este producto\t")
prioridad = input("Ingrese la prioridad estratégica de este producto\t")

if inventario < 50: 
    print("El producto no debe fabricarse por falta de inventario")  
elif demanda == "alta" and inventario >= 50:
    print("El producto debe fabricarse. Se debe priorizar su fabricación por alta demanda y suficiente inventario")
elif costo == "alto" and demanda == "baja":
    print("El producto no debe fabricarse debido a altos costos y baja demanda")
elif prioridad == "alta" and inventario >= 50:
    print("El producto debe fabricarse porque la prioridad es alta y el inventario lo permite")
else:
    print("No es viable fabricar este producto")