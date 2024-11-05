notas = [5.0, 3.4, 2.1, 4.9]
lista1 = [3, -3, 7, 365, 24000] # -> Datos homogéneos
lista2 = ["Nombre", "Apellido", 28, 9, 2022] # -> Datos heterogéneos
lista3 = [] # Vacía para añadir elementos luego
lista3.append(1)


frutas = ["Manzana", "Pera", "Fresa"]
for fruta in frutas:
    print(fruta)

frutas = ["Manzana", "Pera", "Fresa"]
for i in range(0, len(frutas)):
    print(frutas[i])




notas_estudiantes = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]
# Mostrar elementos por filas
for fila in notas_estudiantes:
    for item_col in fila:
        print(item_col, end=' ')
    print()

notas_estudiantes = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]
# Mostrar elementos con enumerate()
for i, row in enumerate(notas_estudiantes):
    for j, item in enumerate(row):
        print(f'n[{i}][{j}]={item} ', end=' ')
    print()

notas_estudiantes = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]
# Mostrar elementos con in range()
for i in range(len(notas_estudiantes)):
    for j in range(len(notas_estudiantes[i])):
        print(f'n[{i}][{j}]={item} ', end=' ')
    print()



