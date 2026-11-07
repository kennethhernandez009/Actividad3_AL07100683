print ("\n****Nombre Completo:Kenneth Israel Hdz C.***\n")
print ("***Matrícula:AL07100683***\n")
print ("Ejercicio 9: Torneo de videojuegos")
print()

# Datos del torneo
juego = input("¿De qué juego es el torneo?: ")
cantidad = int(input("¿Cuántos jugadores hay?: "))

# Contadores y acumuladores
total_puntos = 0
finalistas = 0

# Para guardar al mejor: empezamos con -1 para que cualquier puntaje lo supere
mejor_nombre = ""
mejor_puntos = -1

# "Para cada" jugador del 1 al total...
for jugador in range(1, cantidad + 1):
    print()
    print("🎮 Jugador", jugador)
    nombre = input("Gamertag: ")
    puntos = int(input("Puntos: "))

    # Sumamos sus puntos al total
    total_puntos = total_puntos + puntos

    # ¿Tiene 100 puntos o más?
    if puntos >= 100:
        print("🏅", nombre, "pasa a la final")
        finalistas = finalistas + 1
    else:
        print("💪", nombre, "sigue practicando")

    # ¿Sus puntos son MAYORES que los del mejor hasta ahora?
    if puntos > mejor_puntos:
        # Ahora él es el mejor
        mejor_puntos = puntos
        mejor_nombre = nombre

# Ya registramos a todos: mostramos los resultados
print()
print("===== 🏆 RESULTADOS DEL TORNEO DE", juego, "=====")
print("Puntos de todos los jugadores:", total_puntos)
print("Finalistas:", finalistas)
print("👑 Ganador:", mejor_nombre, "con", mejor_puntos, "puntos")
