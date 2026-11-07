print("Ejercicio 18: Mini CRUD de mangas y cómics")
print("Nombre: Kenneth Israel Hdz C.")
print("Matrícula: AL07100683")
print()

# La lista de mangas y cómics de la tienda
tienda = ["One Piece", "Kimetsu no Yaiba"]

while True:
    print()
    print("===== 📚 MINI CRUD MANGA Y CÓMICS =====")
    print("1. Altas")
    print("2. Bajas")
    print("3. Cambios")
    print("4. Consultas")
    print("5. Imprimir")
    print("6. Salir")
    opcion = input("Elige una opción: ")

    # ========== 1. ALTAS ==========
    if opcion == "1":
        nuevo = input("Manga o cómic nuevo: ")
        if nuevo == "":
            print("❌ No puede estar vacío")
        elif nuevo in tienda:
            print("⚠️", nuevo, "ya existe")
        else:
            tienda.append(nuevo)
            print("✅", nuevo, "agregado")

    # ========== 2. BAJAS ==========
    elif opcion == "2":
        if len(tienda) == 0:
            print("📭 No hay productos para eliminar")
        else:
            for i in range(len(tienda)):
                print(i + 1, ".", tienda[i])
            numero = int(input("Número a eliminar: "))
            if numero < 1:
                print("❌ Ese número no existe")
            elif numero > len(tienda):
                print("❌ Ese número no existe")
            else:
                elegido = tienda[numero - 1]
                confirmar = input("¿Eliminar " + elegido + "? (s/n): ")
                if confirmar == "s":
                    del tienda[numero - 1]
                    print("🗑️", elegido, "eliminado")
                else:
                    print("✋ Baja cancelada")

    # ========== 3. CAMBIOS ==========
    elif opcion == "3":
        if len(tienda) == 0:
            print("📭 No hay productos para cambiar")
        else:
            for i in range(len(tienda)):
                print(i + 1, ".", tienda[i])
            numero = int(input("Número a cambiar: "))
            if numero < 1:
                print("❌ Ese número no existe")
            elif numero > len(tienda):
                print("❌ Ese número no existe")
            else:
                nuevo = input("Nuevo nombre: ")
                if nuevo == "":
                    print("❌ El producto no puede estar vacío")
                elif nuevo in tienda:
                    print("⚠️", nuevo, "ya existe")
                else:
                    print("✏️", tienda[numero - 1], "cambió por", nuevo)
                    tienda[numero - 1] = nuevo

    # ========== 4. CONSULTAS ==========
    elif opcion == "4":
        buscado = input("¿Qué manga o cómic buscas? ")
        if buscado in tienda:
            print("✅ Sí tenemos", buscado)
        else:
            print("❌ No tenemos", buscado)

    # ========== 5. IMPRIMIR ==========
    elif opcion == "5":
        if len(tienda) == 0:
            print("📭 La tienda está vacía")
        else:
            print("===== 📚 INVENTARIO =====")
            for i in range(len(tienda)):
                print(i + 1, ".", tienda[i])
            print("Total:", len(tienda), "productos")

    # ========== 6. SALIR ==========
    elif opcion == "6":
        print("👋 ¡Hasta luego!")
        break

    else:
        print("❌ Opción no válida")
