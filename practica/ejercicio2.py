precipitaciones = [["Agua de Dios",642,1497,1472,1186,1605,0],
["Carmen de Carupa",208,532,1122,1838,0,0],
["Chocontá",9,26,362,37,1099,189],
["Cogua",99,289,946,0,0,0],
["El Colegio",254,645,889,1634,1177,895],
["Facatativá",131,643,633,1629,115,88],
["Funza",188,495,996,994,1796,39],
["Fúquene",9,91,173,163,67,0],
["Fusagasugá",512,504,896,1918,1116,0],
["Guachetá",35,655,906,809,486,0],
["Guasca",837,91,835,1013,719,702],
["Guatavita",12,9,342,0,0,0],
["La Calera",204,154,734,1606,1476,0],
["Lenguazaque",255,89,954,974,1046,1022],
["Nilo",889,1632,2414,2989,0,0],
["Pacho",452,1253,3198,3567,1948,0],
["Pauna",603,1103,1673,1753,0,0],
["Puli",244,977,1685,0,0,0],
["San Miguel de Sema",17,1084,2819,0,0,0],
["Santa Sofía",0,894,2619,1535,0,0],
["Santafe de Bogotá",96,1028,1028,2446,0,0],
["Sibaté",205,358,407,0,0,0],
["Simijaca",142,483,1502,1685,114,52],
["Subachoque",186,867,124,1529,1088,262],
["Suesca",16,12,66,79,69,124],
["Susa",257,381,1146,1903,0,0],
["Sutamarchán",356,376,1813,1543,0,0],
["Sutatausa",73,1,463,1638,563,441],
["Tabio",7,432,877,1844,62,0],
["Tausa",394,693,2022,1845,415,1131],
["Tenjo",78,696,862,1243,0,0],
["Tocaima",443,1599,1415,1451,1357,0],
["Ubaté",136,233,89,1521,711,0],
["Villapinzón",106,0,294,726,768,813],
["Villeta",114,501,3005,335,0,0],
["Zipacón",738,373,1081,1362,1684,0],
["Zipaquirá",276,356,743,0,0,0]]

def consultar_municipio():
    print("")
    # imprimir el nombre de todos los municipios enumerándolos
    for i in range(len(precipitaciones)):
        print(i, precipitaciones[i][0])
    # pedir el número del municipio a consultar
    municipio = int(input("Ingrese el número del municipio que desea consultar\n"))
    # imprimir la información del municipio indicado
    print(f"Municipio: {precipitaciones[municipio][0]}\nEnero: {precipitaciones[municipio][1]}\nFebrero: {precipitaciones[municipio][2]}\nMarzo: {precipitaciones[municipio][3]}\nAbril: {precipitaciones[municipio][4]}\nMayo: {precipitaciones[municipio][5]}\nJunio: {precipitaciones[municipio][6]}")
    
while True:
    opcion = int(input("\n1. Consultar municipio\n2. Consultar mayor precipitación\n3. Consultar promedio de precipitación\n0. Salir\n"))
    if opcion == 1:
        # llamar a la función consultar_municipio()
        consultar_municipio()
    elif opcion == 2:
        print("2")
    elif opcion == 3:
        print("3")
    # cerrar el programa
    elif opcion == 0:
        break
    else:
        print("Opción inválida")