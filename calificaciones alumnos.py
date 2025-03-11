def ingreso_alumnos():
    alumnos = {}
    id_alumno = 1
    asignaturas = ["Matemáticas", "Inglés", "Física", "Programación", "Historia"]
    
    while True:
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        id_unico = f"A{id_alumno:03d}"  # Genera un ID único con formato A001, A002, etc.
        
        if id_unico in alumnos:
            print("El ID ya existe, intente nuevamente.")
            continue
        
        calificaciones = {}
        suma_calificaciones = 0
        for asignatura in asignaturas:
            calificacion = float(input(f"Ingrese la calificación de {nombre} {apellido} en {asignatura}: "))
            calificaciones[asignatura] = calificacion
            suma_calificaciones += calificacion
        
        promedio = suma_calificaciones / len(asignaturas)
        
        alumnos[id_unico] = {
            "nombre": nombre,
            "apellido": apellido,
            "calificaciones": calificaciones,
            "promedio": promedio
        }
        id_alumno += 1
        
        continuar = input("¿Desea ingresar otro alumno? (s/n): ")
        if continuar.lower() != "s":
            break
    
    print("\nLista de alumnos y sus calificaciones:")
    for id_unico, datos in alumnos.items():
        print(f"ID: {id_unico} - {datos['nombre']} {datos['apellido']}")
        for asignatura, calificacion in datos["calificaciones"].items():
            print(f"   {asignatura}: {calificacion}")
        print(f"   Promedio: {datos['promedio']:.2f}")
        print("----------------------------")

# Ejecutar la función
ingreso_alumnos()
