# Bucle principal para que la calculadora no se cierre
while True:
    print("\nSelecciona una operación:")
    print("1. División")
    print("2. Módulo")
    print("3. Salir")

    opcion = input("Introduce la opción (1/2/3): ")

    if opcion == '3':
        print("Saliendo de la calculadora. ¡Adiós!")
        break

    if opcion in ('1', '2'):
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Entrada no válida. Por favor, introduce solo números.")
            continue

        if opcion == '1':
            if num2 != 0:
                print("El resultado de la división es:", num1 / num2)
            else:
                print("Error: No se puede dividir por cero.")
        elif opcion == '2':
            if num2 != 0:
                print("El resultado del módulo es:", num1 % num2)
            else:
                print("Error: No se puede calcular el módulo con un divisor de cero.")
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")