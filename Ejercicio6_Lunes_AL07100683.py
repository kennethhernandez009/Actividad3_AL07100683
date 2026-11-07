
print ("\n****Nombre Completo:Kenneth Israel Hdz C.***\n")
print ("***Matrícula:AL07100683***\n")
print ("Ejercicio 6: Validar los datos de una alta")
print()

# 1. Título: mientras esté vacío, lo volvemos a pedir
titulo = input("Título del manga o cómic: ")
while titulo == "":
    print("❌ El título no puede estar vacío")
    titulo = input("Título del manga o cómic: ")

# 2. Número de tomos: mientras sea 0 o menos, lo volvemos a pedir
tomos = int(input("Número de tomos: "))
while tomos <= 0:
    print("❌ El número de tomos debe ser mayor que 0")
    tomos = int(input("Número de tomos: "))

# 3. Código: mientras esté vacío, lo volvemos a pedir
codigo = input("Código de la colección: ")
while codigo == "":
    print("❌ El código no puede estar vacío")
    codigo = input("Código de la colección: ")

# 4. Estado: al inicio todavía NO es válido
estado = ""
estado_valido = False

while estado_valido == False:
    print("Estados: 1. En curso   2. Terminado")
    opcion = input("Elige el estado: ")

    if opcion == "1":
        estado = "En curso"
        estado_valido = True
    elif opcion == "2":
        estado = "Terminado"
        estado_valido = True
    else:
        print("❌ Ese estado no existe")

# Pedimos los datos adicionales de nuestra colección
autor = input("Autor: ")
genero = input("Género: ")

# 5. Mostramos la ficha
print()
print("===== FICHA DEL MANGA O CÓMIC =====")
print("Código:", codigo)
print("Título:", titulo)
print("Autor:", autor)
print("Género:", genero)
print("Número de tomos:", tomos)
print("Estado:", estado)

# 6. Confirmación: al inicio la respuesta todavía NO es válida
respuesta_valida = False

while respuesta_valida == False:
    guardar = input("¿Guardar? (s/n): ")

    if guardar == "s":
        print("✅ Manga o cómic guardado")
        respuesta_valida = True
    elif guardar == "n":
        print("🚫 Alta cancelada")
        respuesta_valida = True
    else:
        print("❌ Escribe solo s o n")
