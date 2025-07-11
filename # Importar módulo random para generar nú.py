# Importar módulo random para generar números aleatorios
import random  

# Lista de estudiantes (usamos una lista para guardar los nombres)
estudiantes = [
    "Valentina Rojas",
    "Tomás Morales",
    "Martina Castillo",
    "Benjamín Soto",
    "Isidora Fuentes",
    "Matías Herrera",
    "Antonia Díaz",
    "Lucas Vargas",
    "Camila Reyes",
    "Joaquín Paredes"
]

# Diccionario vacío donde se guardarán las notas de cada estudiante
notas = {}

# Función para asignar notas aleatorias a cada estudiante
def asignar_notas(estudiante):
    # Recorre la lista de estudiantes
    for estudiante in estudiantes:
        # Genera una nota aleatoria entre 1.0 y 7.0 con un decimal
        nota = int(random.uniform(1.0, 7.0) * 10)  / 10
        # Guarda la nota en el diccionario usando el nombre como clave
        notas[estudiante] = nota

    # Mostrar todas las notas asignadas
    print ("Notas finales de los estudiantes \n")
    for estudiante , nota in notas.items():
        print (f"{estudiante}: {nota}")

# Función para clasificar los estudiantes según su nota
def clasificar_notas():
    reprobados = []    # Lista para los estudiantes con nota < 4.0
    aprobados = []     # Lista para los estudiantes con nota >= 4.0 y < 6.0
    destacados = []    # Lista para los estudiantes con nota >= 6.0
    
    # Recorrer el diccionario de notas
    for estudiante, nota in notas.items():
        if nota < 4.0:
            reprobados.append((estudiante , nota))
        elif nota < 6.0:
            aprobados.append((estudiante, nota))
        else: 
            destacados.append((estudiante, nota))
    
    # Mostrar los resultados de clasificación
    print ("\nClasificación de estudiantes:\n")

    # Mostrar reprobados
    print (" Reprobados:")
    for estudiante, nota in reprobados:
        print (f"{estudiante}, {nota}")
    print (f"Total: {len(reprobados)} alumnos\n")

    # Mostrar aprobados
    print (" Aprobados:")
    for estudiante, nota in aprobados:
        print (f"{estudiante}, {nota}")
    print (f"Total: {len(aprobados)} alumnos\n")

    # Mostrar destacados
    print (" Destacados:")
    for estudiante, nota in destacados:
        print (f"{estudiante}, {nota}")
    print (f"Total: {len(destacados)} alumnos\n")

# Función para calcular y mostrar estadísticas del curso
def ver_estadisticas():
    # Obtener la nota más alta y más baja del diccionario
    nota_mas_alta = max(notas.values())
    nota_mas_baja = min(notas.values())

    # Buscar qué estudiante tiene la nota más alta y la más baja
    for estudiante, nota in notas.items():
        if nota == nota_mas_alta:
            mejor = estudiante
        if nota == nota_mas_baja:
            peor = estudiante

    # Calcular promedio del curso
    suma_notas = sum(notas.values())
    cantidad_estudiantes = len(notas)
    promedio = int((suma_notas / cantidad_estudiantes) * 10) / 10

    # Mostrar estadísticas
    print(" Estadísticas generales:\n")
    print(f" Nota más alta: {nota_mas_alta} (Alumno: {mejor})")
    print(f" Nota más baja: {nota_mas_baja} (Alumno: {peor})")
    print(f" Promedio del curso: {promedio}")

# Función para guardar las notas en un archivo de texto
def guardar_archivo():
    # Crear o sobreescribir el archivo "notas.txt"
    archivo = open("notas.txt", "w")

    # Escribir encabezado
    archivo.write("Listado de notas finales:\n")
    archivo.write("-------------------------\n")

    # Escribir cada línea con el nombre y su nota
    for estudiante, nota in notas.items():
        archivo.write(f"{estudiante}: {nota}\n")

    # Cerrar el archivo
    archivo.close()

    # Mensaje de éxito
    print(" Archivo 'notas.txt' creado correctamente.")

# Función principal con menú
def menu():
    notas_asignadas = False  # Bandera para saber si ya se asignaron notas
    salir = False  # Control del ciclo del menú

    # Bucle principal del menú
    while not salir:
        print("\n====== MENÚ PRINCIPAL ======")
        print("1. Asignar notas aleatorias")
        print("2. Clasificar notas")
        print("3. Ver estadísticas")
        print("4. Guardar notas en archivo")
        print("5. Salir")

        # Leer opción del usuario
        opcion = input("Ingrese una opción: ")

        # Opción 1: Asignar notas
        if opcion == "1":
            asignar_notas(estudiantes)
            notas_asignadas = True

        # Opción 2: Clasificar notas
        elif opcion == "2":
            if notas_asignadas:
                clasificar_notas()
            else:
                print(" Primero debes asignar las notas.")

        # Opción 3: Ver estadísticas
        elif opcion == "3":
            if notas_asignadas:
                ver_estadisticas()
            else:
                print(" Primero debes asignar las notas.")

        # Opción 4: Guardar en archivo
        elif opcion == "4":
            if notas_asignadas:
                guardar_archivo()
            else:
                print(" Primero debes asignar las notas.")

        # Opción 5: Salir
        elif opcion == "5":
            print("\n Gracias por usar el sistema. ¡Hasta pronto!")
            salir = True

        # Si el usuario ingresa una opción no válida
        else:
            print(" Opción inválida. Intente nuevamente.")

# Ejecutar el programa llamando al menú
menu()
