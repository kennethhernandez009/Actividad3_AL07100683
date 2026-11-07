print ("\n****Nombre Completo:Kenneth Israel Hdz C.***\n")
print ("***Matrícula:AL07100683***\n")
print ("Ejercicio 12: Alta de mangas y cómics con código")
print()

# ¿Cuántos mangas o cómics vamos a dar de alta?
cuantos = int(input("¿Cuántos mangas o cómics vas a registrar?: "))

# Aquí sumaremos el valor de toda la colección
total_tomos = 0

# "Para cada" número del 1 al total de registros...
for numero in range(1, cuantos + 1):
    # Creamos el código: str() convierte el número en texto
    codigo = "MNG" + str(numero)

    print()
    print("📚 Manga o cómic con código", codigo)
    titulo = input("Título: ")

    # Pedimos el número de tomos y lo validamos
    while True:
        tomos = int(input("Número de tomos: "))
        if tomos > 0:
            break
        print("❌ El número de tomos debe ser mayor que 0")
        
    ejemplares = int(input("Ejemplares en la colección: "))

    # Calculamos cuántos tomos hay en total de este registro
    valor = tomos * ejemplares
    total_tomos = total_tomos + valor

    # Mostramos la ficha
    print("✅ Alta exitosa")
    print("   Código:", codigo, "   Título:", titulo)
    print("   Tomos:", tomos, "   Ejemplares:", ejemplares,
          "   Total de tomos:", valor)

# Ya terminamos todas las altas
print()
print("===== RESUMEN DE LA COLECCIÓN =====")
print("Mangas y cómics dados de alta:", cuantos)
print("📚 Total de tomos en la colección:", total_tomos)
