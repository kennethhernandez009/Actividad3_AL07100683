print ("\n****Nombre Completo:Kenneth Israel Hdz C.***\n")
print ("***Matrícula:AL07100683***\n")
print ("^^^^ Ejercicio 1: Inicia Sesión en Roblox ^^^^")
print ()

#Guardamos el usuario y la contraseña correctos
usuario_correcto = "Its_KenK0"
contrasena_correcta = "092008"

#Al inicio todavía NO has iniciado sesión
sesión_iniciada = False

#Mientras NO se haya iniciado sesión, se repite
while sesión_iniciada == False:
    #Pedimos el usuario y la contraseña
    usuario = input("Usuario:")
    contrasena = input("Contraseña: ")

    #¿El usuario es IGUAL al correcto?
    if usuario == usuario_correcto:
        # Sí existe. Ahora: ¿La contraeña es IGUAL a la correcta?
        if contrasena == contrasena_correcta:
            print ("✅¡Bienvenido,", usuario, "!")
            # Ya entró: esto hace que el while se detenga
            sesión_iniciada = True
        else:
            print ("❌La contraseña es incorrecta")
    else:
        print ("❌Ese usuario no existe")

# Esto se ejecuta cuando ya salió del while
print ("🎮Cargando tus juegos..")
