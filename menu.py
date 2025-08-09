
while True:
    print("\nSelecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Introduce la opción (1/2/3/4/5): ")

    if opcion == '5':
        print("Saliendo de la calculadora. ¡Adiós!")
        break

    if opcion in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Entrada no válida. Por favor, introduce solo números.")
            continue # Vuelve al inicio del bucle

        if opcion == '1':
            print("El resultado es:", num1 + num2)
        elif opcion == '2':
            print("El resultado es:", num1 - num2)
        elif opcion == '3':
            print("El resultado es:", num1 * num2)
        elif opcion == '4':
            if num2 != 0:
                print("El resultado es:", num1 / num2)
            else:
                print("Error: No se puede dividir por cero.")
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")