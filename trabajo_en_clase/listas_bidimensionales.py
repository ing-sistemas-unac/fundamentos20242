notas = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]
for fila in notas: # ciclo para las filas
    for item in fila: # ciclo para los elementos de las columnas
        print(item, end=" ")
    print() # salto de línea al terminar cada fila