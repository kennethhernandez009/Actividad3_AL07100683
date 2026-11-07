print("Ejercicio 17: Consultas en el inventario")
print("Nombre: Kenneth Israel Hdz C.")
print("Matrícula: AL07100683")
print()

# El inventario de la tienda
inventario = ["Nike Air Force 1", "Adidas Superstar", "Nike Air Max 90",
              "Converse Chuck Taylor", "Adidas Stan Smith", "Nike Dunk Low"]

while True:
    print()
    print("===== 🔎 CONSULTAS =====")
    print("1. Buscar por nombre")
    print("2. Buscar por primera letra")
    print("3. ¿Cuántos productos hay?")
    print("4. Regresar")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        buscado = input("Nombre del modelo (con mayúsculas como en la lista): ")

        # ¿El modelo ESTÁ en el inventario?
        if buscado in inventario:
            # Recorremos los casilleros para saber dónde está
            for i in range(len(inventario)):
                if inventario[i] == buscado:
                    print("✅", buscado, "está en el lugar", i + 1)
        
        else:
            print("❌", buscado, "no está en el inventario")

    elif opcion == "2":
        letra = input("Escribe la primera letra (en mayúscula): ")
        encontrados = 0

        # "Para cada" producto del inventario...
        for producto in inventario:
            # producto[0] es la primera letra del texto
            if producto[0] == letra:
                print("👟", producto)
                encontrados = encontrados + 1

        # ¿No encontramos ninguno?
        if encontrados == 0:
            print("❌ Ningún producto empieza con", letra)
        else:
            print("Encontré", encontrados, "productos")

    elif opcion == "3":
        print("📦 Hay", len(inventario), "productos en el inventario")

    elif opcion == "4":
        print("👋 Regresando...")
        break

    else:
        print("❌ Opción no válida")
