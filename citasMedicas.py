opcion1 = False
totalCita = []

while True:
        print("")
        print("   MENÚ DE CITAS MÉDICAS")
        print("")
        print("1. Programar nueva cita")
        print("2. Ver citas programadas")
        print("3. Salir")

        opcion = int(input("\nIngrese su opción:\n "))

        if opcion == 1:
            opcion1 = True
            fecha = input("Ingrese la fecha de la cita (DD/MM/AA): ")
            hora = input("Ingrese la hora de la cita (HH:MM):  ")
            nombrePaciente = input("Ingrese el nombre del paciente:  ")
            cita = (nombrePaciente,fecha,hora)
            totalCita.append(cita)          
            print("")
            print("----- ¡Cita médica programada con éxito! -----")
            
        elif opcion == 2 and opcion1 == True:
            print("\n------- Citas programadas: --------\n")
            for cita in totalCita:
                print (f"Nombre Paciente: {cita[0]}, Fecha cita: {cita[1]}, Hora cita:  {cita[2]}")
                       
        elif opcion == 3:
            print("Saliendo del sistema...")
            break
        else:
            print("\n***Opción no válida. Intente nuevamente.***")