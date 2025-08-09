# Bucle principal para que la calculadora no se cierre
while True:
    print("\nSelecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir")

    opcion = input("Introduce la opción (1/2/3): ")

    # Si el usuario elige 3, salimos del programa de inmediato.
    if opcion == '3':
        print("Saliendo de la calculadora. ¡Adiós!")
        break

    # Aquí solo se evalúan las opciones válidas para realizar cálculos: 1 y 2
    if opcion in ('1', '2'):
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Entrada no válida. Por favor, introduce solo números.")
            continue  # Vuelve al inicio del bucle

        if opcion == '1':
            print("El resultado es:", num1 + num2)
        elif opcion == '2':  # <-- ¡Aquí está la resta!
            print("El resultado es:", num1 - num2)
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")