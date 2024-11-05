notas = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]
# enumerate para imprimir los índices
for i, fila in enumerate(notas): 
    for j, item in enumerate(fila): 
        print(f"[{i}][{j}]:{item}", end=" ")
    print() 