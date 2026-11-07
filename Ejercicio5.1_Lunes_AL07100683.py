
print ("\n****Nombre Completo:Kenneth Israel Hdz C.***\n")
print ("***Matrícula:AL07100683***\n")
print ("Ejercicio 5: Colección de Manga y Cómics - Menú principal")
print()

# Pedimos el nombre del sistema
nombre_sistema = input("¿Cómo se llama tu sistema? ")

# Contador de operaciones: empieza en 0
operaciones = 0

# El menú se repite siempre: la única salida es el break
while True:
    print()
    print("======", nombre_sistema, "======")
    print("1. Altas")
    print("2. Bajas")
    print("3. Cambios")
    print("4. Consultas")
    print("5. Imprimir")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("➕ Aquí podrás agregar un manga o cómic")
        operaciones = operaciones + 1
    elif opcion == "2":
        print("🗑️ Aquí podrás eliminar un manga o cómic")
        operaciones = operaciones + 1
    elif opcion == "3":
        print("✏️ Aquí podrás modificar los datos de un manga o cómic")
        operaciones = operaciones + 1
    elif opcion == "4":
        print("🔍 Aquí podrás buscar mangas o cómics")
        operaciones = operaciones + 1
    elif opcion == "5":
        print("📚 Aquí se mostrarán todos los mangas y cómics")
        operaciones = operaciones + 1
    elif opcion == "6":
        # Antes de salir, confirmamos
        seguro = input("¿Seguro que quieres salir? (s/n): ")

        # ¿La respuesta es IGUAL a "s"?
        if seguro == "s":
            print("👋 Hiciste", operaciones, "operaciones. ¡Hasta luego!")
            # break nos saca del while
            break
        else:
            print("👍 Regresando al menú...")

    else:
        # Opción inválida: no se cuenta como operación
        print("❌ Opción no válida, elige del 1 al 6")
