# ===================== ESTRUCTURAS PRINCIPALES =====================
cursos = []         # Lista de cursos
historial = []      # Pila para registrar cambios
solicitudes = []    # Cola de revisión

# ===================== FUNCIONES =====================
# Opcion 1 / Registra todos los cursos que desea el usuario 
def registrar_curso():
    nombre = input("Ingrese el nombre del curso: ").strip()
    if not nombre:
        print(" El nombre no puede estar vacío.")
        return
    try:
        nota = float(input("Ingrese la nota obtenida: "))
        if 0 <= nota <= 100:
            cursos.append({"nombre": nombre, "nota": nota})
            historial.append(f"Curso registrado: {nombre} - Nota: {nota}")
            print(" Curso registrado con éxito.")
        else:
            print(" La nota debe estar entre 0 y 100.")
    except ValueError:
        print(" Entrada inválida. La nota debe ser numérica.")

# Opcion 2 / Muestra todos los cursos que ingreso el usuario 
def mostrar_cursos():
    if not cursos:
        print(" No hay cursos registrados.")
    else:
        print("Cursos registrados:")
        for i, curso in enumerate(cursos, 1):
            print(f"{i}. {curso['nombre']} - Nota: {curso['nota']}")

# Opcion 3 / Calcula el promedio de todas las notas que ingreso el usuario 
def calcular_promedio():
    if not cursos:
        print(" No hay cursos para calcular promedio.")
        return
    promedio = sum(c["nota"] for c in cursos) / len(cursos)
    print(f" Promedio general: {round(promedio, 2)}")

# Opcion 4/ Cuenta los cursos que aprobo o reprobo 
def contar_aprobados():
    aprobados = sum(1 for c in cursos if c["nota"] >= 60)
    reprobados = len(cursos) - aprobados
    print(f" Cursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}")

# Opcion 5/ Busca el curso que el usuario desea 
def buscar_lineal():
    nombre = input("Ingrese el nombre del curso: ").strip().lower()
    encontrados = [c for c in cursos if nombre in c["nombre"].lower()]
    if encontrados:
        for c in encontrados:
            print(f" Curso encontrado: {c['nombre']} - Nota: {c['nota']}")
    else:
        print(" Curso no encontrado.")

# Opcion 6/ Si hay una nota que desea Cambiar 
def actualizar_nota():
    nombre = input("Ingrese el nombre del curso: ").strip().lower()
    for c in cursos:
        if c["nombre"].lower() == nombre:
            try:
                nueva_nota = float(input("Ingrese la nueva nota: "))
                if 0 <= nueva_nota <= 100:
                    historial.append(f"Nota actualizada: {c['nombre']} de {c['nota']} a {nueva_nota}")
                    c["nota"] = nueva_nota
                    print(" Nota actualizada correctamente.")
                else:
                    print(" Nota fuera de rango.")
            except ValueError:
                print("Entrada inválida.")
            return
    print("Curso no encontrado.")

# Opcion 7/ Elimina un curso  
def eliminar_curso():
    nombre = input("Ingrese el curso a eliminar: ").strip().lower()
    for i, c in enumerate(cursos):
        if c["nombre"].lower() == nombre:
            confirm = input(f"¿Está seguro que desea eliminar '{c['nombre']}'? (s/n): ").lower()
            if confirm == 's':
                historial.append(f"Curso eliminado: {c['nombre']} - Nota: {c['nota']}")
                cursos.pop(i)
                print("Curso eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
            return
    print(" Curso no encontrado.")

# Opcion 8 / Ordena cursos por nota   
def ordenar_por_nota():
    for i in range(len(cursos)):
        for j in range(len(cursos) - i - 1):
            if cursos[j]["nota"] > cursos[j + 1]["nota"]:
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
    print(" Cursos ordenados por nota (burbuja).")

# Opcion 9 / Ordena cursos por nombre
def ordenar_por_nombre():
    for i in range(1, len(cursos)):
        actual = cursos[i]
        j = i - 1
        while j >= 0 and cursos[j]["nombre"].lower() > actual["nombre"].lower():
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = actual
    print(" Cursos ordenados por nombre (inserción).")

# Opcion 10 / Busca curso por nombre
def buscar_binaria():
    ordenar_por_nombre()
    nombre = input("Ingrese el nombre del curso: ").strip().lower()
    izq, der = 0, len(cursos) - 1
    while izq <= der:
        mid = (izq + der) // 2
        if cursos[mid]["nombre"].lower() == nombre:
            print(f" Curso encontrado: {cursos[mid]['nombre']} - Nota: {cursos[mid]['nota']}")
            return
        elif cursos[mid]["nombre"].lower() < nombre:
            izq = mid + 1
        else:
            der = mid - 1
    print(" Curso no encontrado.")

# Opcion 11 / Simular cola de solicitudes de revisión
def simular_cola():
    nombre = input("Ingrese el nombre del curso para revisión: ").strip()
    solicitudes.append(nombre)
    print(f" Solicitud agregada para '{nombre}'")
    print(" Procesando solicitudes...")
    while solicitudes:
        print(f" Revisando curso: {solicitudes.pop(0)}")

# Opcion 12 / Mostrar historial de cambios 
def mostrar_historial():
    if not historial:
        print(" No hay historial de cambios.")
    else:
        print(" Historial de cambios:")
        for cambio in reversed(historial):
            print(f"- {cambio}")

# ===================== MENÚ PRINCIPAL =====================
def menu():
    while True:
        print("\n====== GESTOR DE NOTAS ACADÉMICAS ======")
        print("1. Registrar nuevo curso")
        print("2. Mostrar todos los cursos y notas")
        print("3. Calcular promedio general")
        print("4. Contar cursos aprobados y reprobados")
        print("5. Buscar curso por nombre (búsqueda lineal)")
        print("6. Actualizar nota de un curso")
        print("7. Eliminar un curso")
        print("8. Ordenar cursos por nota (ordenamiento burbuja)")
        print("9. Ordenar cursos por nombre (ordenamiento inserción)")
        print("10. Buscar curso por nombre (búsqueda binaria)")
        print("11. Simular cola de solicitudes de revisión")
        print("12. Mostrar historial de cambios (pila)")
        print("13. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_curso()
        elif opcion == '2':
            mostrar_cursos()
        elif opcion == '3':
            calcular_promedio()
        elif opcion == '4':
            contar_aprobados()
        elif opcion == '5':
            buscar_lineal()
        elif opcion == '6':
            actualizar_nota()
        elif opcion == '7':
            eliminar_curso()
        elif opcion == '8':
            ordenar_por_nota()
        elif opcion == '9':
            ordenar_por_nombre()
        elif opcion == '10':
            buscar_binaria()
        elif opcion == '11':
            simular_cola()
        elif opcion == '12':
            mostrar_historial()
        elif opcion == '13':
            print(" Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print(" Opción inválida. Intente nuevamente.")
menu()
