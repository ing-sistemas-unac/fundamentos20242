"""
Crea un programa que cuente el número de vocales en una cadena ingresada por el usuario.
"""
print("Ingrese una palabra")
palabra = input()
vocal_a = 0
vocal_e = 0
vocal_i = 0
vocal_o = 0
vocal_u = 0
for i in range(0, len(palabra)):
    if palabra[i] == "a":
        vocal_a += 1
    elif palabra[i] == "e":
        vocal_e += 1
    elif palabra[i] == "i":
        vocal_i += 1
    elif palabra[i] == "o":
        vocal_o += 1
    elif palabra[i] == "u":
        vocal_u += 1
    else: 
        pass
print(f"La palabra {palabra} tiene\n{vocal_a} vocal a\n{vocal_e} vocal e\n{vocal_i} vocal i\n{vocal_o} vocal o\n{vocal_u} vocal u\nTotal vocales = {vocal_a+vocal_e+vocal_i+vocal_o+vocal_u}")