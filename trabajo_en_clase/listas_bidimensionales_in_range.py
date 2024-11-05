notas = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]
# imprimir índices con in range()
for i in range(len(notas)): 
    for j in range(len(notas[i])): 
        print(f"[{i}][{j}]:{notas[i][j]}", end=" ")
    print() 
    