def mostrar_empleados(empleados):
    print("\nLista de empleados:")
    for id_unico, datos in empleados.items():
        print(f"ID: {id_unico} - {datos['nombre']} {datos['apellido']} - Sector: {datos['sector']} - Sueldo: ${datos['sueldo']:.2f}")
    print("----------------------------")

def buscar_empleado(empleados):
    id_buscar = input("Ingrese el ID del empleado a buscar: ")
    if id_buscar in empleados:
        datos = empleados[id_buscar]
        print(f"Empleado encontrado: {datos['nombre']} {datos['apellido']} - Sector: {datos['sector']} - Sueldo: ${datos['sueldo']:.2f}")
    else:
        print("Empleado no encontrado.")

def eliminar_empleado(empleados):
    id_eliminar = input("Ingrese el ID del empleado a eliminar: ")
    if id_eliminar in empleados:
        del empleados[id_eliminar]
        print("Empleado eliminado correctamente.")
    else:
        print("Empleado no encontrado.")

def calcular_sueldo(sector):
    sueldos_base = {
        "Administración": 50000,
        "Técnicos": 60000,
        "Diseño": 55000,
        "Personal IT": 70000,
        "Depósito": 48000
    }
    return sueldos_base.get(sector, 0)

def ingreso_empleados():
    empleados = {}
    id_empleado = 1
    sectores = ["Administración", "Técnicos", "Diseño", "Personal IT", "Depósito"]
    
    while True:
        print("\nMenú:")
        print("1. Ingresar nuevo empleado")
        print("2. Mostrar empleados")
        print("3. Buscar empleado")
        print("4. Eliminar empleado")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del empleado: ")
            apellido = input("Ingrese el apellido del empleado: ")
            sector = input(f"Ingrese el sector del empleado {sectores}: ")
            
            if sector not in sectores:
                print("Sector inválido, intente nuevamente.")
                continue
            
            id_unico = f"E{id_empleado:03d}"  # Genera un ID único con formato E001, E002, etc.
            
            # Verificar si ya existe un empleado con el mismo nombre y apellido
            for empleado in empleados.values():
                if empleado["nombre"].lower() == nombre.lower() and empleado["apellido"].lower() == apellido.lower():
                    print("Error: El empleado ya existe en el sistema.")
                    continue
            
            sueldo = calcular_sueldo(sector)
            empleados[id_unico] = {
                "nombre": nombre,
                "apellido": apellido,
                "sector": sector,
                "sueldo": sueldo
            }
            id_empleado += 1
            print("Empleado agregado correctamente.")
            
        elif opcion == "2":
            mostrar_empleados(empleados)
        
        elif opcion == "3":
            buscar_empleado(empleados)
        
        elif opcion == "4":
            eliminar_empleado(empleados)
        
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar la función
ingreso_empleados()