# datos para realizar las pruebas
asistentes = [ 
    ["Juan Pérez", "1001", 20, "Concierto Rock Fest", 40000, True], 
    ["María López", "1002", 22, "Conferencia AI Summit", 30000, False], 
    ["Carlos Gómez", "1003", 25, "Obra de Teatro Clásicos", 32000, True], 
    ["Ana Méndez", "1004", 23, "Festival de Jazz", 45000, False], 
    ["Pedro Martínez", "1005", 21, "Concierto Rock Fest", 50000, False], 
    ["Laura Fernández", "1006", 24, "Conferencia AI Summit", 24000, True], 
    ["Raúl Castro", "1007", 27, "Festival de Jazz", 45000, False], 
    ["Carmen Díaz", "1008", 29, "Concierto Rock Fest", 50000, False], 
    ["Miguel Reyes", "1009", 31, "Obra de Teatro Clásicos", 32000, True], 
    ["Paola Jiménez", "1010", 26, "Concierto Rock Fest", 40000, True], 
    ["Luis Sánchez", "1011", 28, "Festival de Jazz", 45000, False], 
    ["Andrea Vargas", "1012", 22, "Conferencia AI Summit", 30000, False], 
    ["Sofía Moreno", "1013", 30, "Obra de Teatro Clásicos", 32000, True], 
    ["Jorge Díaz", "1014", 25, "Concierto Rock Fest", 40000, True], 
    ["Patricia Ruiz", "1015", 24, "Festival de Jazz", 45000, False], 
    ["Camilo Paredes", "1016", 23, "Conferencia AI Summit", 30000, False], 
    ["Lucía Castro", "1017", 27, "Obra de Teatro Clásicos", 32000, True], 
    ["Fernando González", "1018", 29, "Festival de Jazz", 45000, False], 
    ["Silvia Martínez", "1019", 21, "Concierto Rock Fest", 40000, True], 
    ["Mateo Ríos", "1020", 24, "Concierto Rock Fest", 50000, False], 
    ["Diana Quintero", "1021", 28, "Obra de Teatro Clásicos", 32000, True], 
    ["Iván Reyes", "1022", 26, "Conferencia AI Summit", 30000, False], 
    ["Natalia Peña", "1023", 30, "Festival de Jazz", 36000, True], 
    ["Samuel Serrano", "1024", 22, "Concierto Rock Fest", 50000, False], 
    ["Gloria Hurtado", "1025", 25, "Festival de Jazz", 45000, False], 
    ["Oscar Zamora", "1026", 27, "Conferencia AI Summit", 24000, True], 
    ["Verónica Rojas", "1027", 23, "Obra de Teatro Clásicos", 40000, False], 
    ["Manuel Herrera", "1028", 29, "Concierto Rock Fest", 40000, True], 
    ["Clara Duarte", "1029", 28, "Festival de Jazz", 36000, True], 
    ["David Londoño", "1030", 24, "Conferencia AI Summit", 30000, False], 
    ["Isabel Bravo", "1031", 22, "Obra de Teatro Clásicos", 40000, False], 
    ["Gabriel Ruiz", "1032", 25, "Concierto Rock Fest", 40000, True], 
    ["Valentina Cárdenas", "1033", 21, "Festival de Jazz", 36000, True], 
    ["Francisco León", "1034", 24, "Conferencia AI Summit", 30000, False], 
    ["Rosa Mendoza", "1035", 27, "Obra de Teatro Clásicos", 32000, True], 
    ["Andrés Gutiérrez", "1036", 23, "Concierto Rock Fest", 50000, False], 
    ["Mónica Aguirre", "1037", 29, "Festival de Jazz", 45000, False], 
    ["Rodrigo Cortés", "1038", 26, "Concierto Rock Fest", 40000, True], 
    ["Elena Pacheco", "1039", 31, "Conferencia AI Summit", 24000, True], 
    ["Fabián Quintero", "1040", 25, "Festival de Jazz", 45000, False], 
    ["Susana Ortiz", "1041", 28, "Obra de Teatro Clásicos", 40000, False], 
    ["Emilio Bernal", "1042", 24, "Concierto Rock Fest", 40000, True], 
    ["Carolina Vallejo", "1043", 23, "Festival de Jazz", 45000, False], 
    ["Ricardo Suárez", "1044", 26, "Conferencia AI Summit", 24000, True], 
    ["Paula Ramírez", "1045", 29, "Concierto Rock Fest", 50000, False], 
    ["Antonio Beltrán", "1046", 22, "Obra de Teatro Clásicos", 32000, True], 
    ["Gloria Vergara", "1047", 27, "Festival de Jazz", 36000, True], 
    ["Esteban Vargas", "1048", 28, "Conferencia AI Summit", 30000, False], 
    ["Sara Acosta", "1049", 25, "Concierto Rock Fest", 40000, True], 
    ["Lucía Silva", "1050", 30, "Festival de Jazz", 36000, True], 
] 

def promedio_edades():
    edades = 0
    for i in range(len(asistentes)):
        edades += asistentes[i][2]
    promedio = edades/50
    print("Promedio edades", promedio)

def numero_asistentes_descuento():
    descuento = 0
    for i in range(len(asistentes)):
        if asistentes[i][5] == True:
            descuento += 1
    print("Descuento", descuento)
