
citas_programadas = []

def programar_nueva_cita():
    fecha = input(">>> Ingrese la fecha de la cita (DD/MM/AAAA): ")
    hora = input(">>> Ingrese la hora de la cita (HH:MM): ")
    paciente = input(">>> Ingrese el nombre del paciente: ")
    citas_programadas.append({"Fecha": fecha, "Hora": hora, "Paciente": paciente})
    print("*")
    print("Cita programada exitosamente.")
    print("*")

def ver_citas_programadas():
    if citas_programadas:
        print(">>> Citas programadas:")
        for index, cita in enumerate(citas_programadas, start=1):
            print(f"Cita {index}: Fecha: {cita['Fecha']}, Hora: {cita['Hora']}, Paciente: {cita['Paciente']}")
    else:
        print("No hay citas programadas.\n")

while True:
    print("*")
    print("Asistente para Citas Médicas")
    print("*")
    print("1. Programar nueva cita")
    print("2. Ver citas programadas")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        programar_nueva_cita()
    elif opcion == '2':
        ver_citas_programadas()
    elif opcion == '3':
        print("*")
        print("Saliste del programa...")
        print("*")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.\n")