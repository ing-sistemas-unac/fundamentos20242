def contador_letras(palabras):
    letras = ["a", "b", "c", "d", "e"]
    contador = [0, 0, 0, 0, 0]

    for car in palabras.lower():
        for i in range(len(contador)):
            if car == letras[i]:
                contador[i] += 1

    print(letras)
    print(contador)

palabras = input()
contador_letras(palabras)