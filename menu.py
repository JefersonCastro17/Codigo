import funcion

def menu():
    while True:
        print("\n calculadora")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Módulo")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            funcion.suma()
        elif opcion == "2":
            funcion.resta()
        elif opcion == "3":
            funcion.multiplicacion()
        elif opcion == "4":
            funcion.division()
        elif opcion == "5":
            funcion.modulo()
        elif opcion == "0":
            print("¡Fin!")
            break
        else:
            print("Opción no encontrada")