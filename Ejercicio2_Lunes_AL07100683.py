print ("\n****Nombre Completo:Kenneth Israel Hdz C.***\n")
print ("***Matrícula:AL07100683***\n")
print ("~~~ Ejercicio 2: Menú de la Cafetería Cute ~~~")

# while True: el menú se repite siempre; la única salida es el break
while True:
    #Mostrarnos el menú
    print()
    print("==== ☕CAFETERÍA CUTE ====")
    print ("1. Ver bebidas")
    print ("2. Ver postres")
    print ("3. Ver horario")
    print ("4. Salir")

    # Pedimos la opción
    opción = input ("Elige una opción: ")

    # Revisamos qué opción eligió
    if opción == "1":
        print ("🧋 Frappé de cajeta . . . . $65")
        print ("🍵 Matcha Latte . . . . $70")
        print ("🍓 Smoothie de Fresa . . . . $55")
    elif opción == "2":
        print ("🍪 Galleta Red Velvet . . . . $35")
        print ("🧁 Cupcake de Oreo . . . . $40")
        print ("🍩 Dona Glaseada . . . . $30")
    elif opción == "3":
        print ("🕐 Lunes a Viernes: 7:00 a 20:00")
        print ("🕑 Sábados: 9:00 a 14:00")
    elif opción == "4":
        print ("👋¡Gracias por visitarnos!")
        # El cliente eligió salir: break nos saca del while
        break
    else:
        print ("❌Opción no válida, elige del 1 al 4")
        


        
