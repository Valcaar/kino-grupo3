# Registro de usuario

import libreria as lb #importamos funciones de la libreria.py
usuarios = {} #diccionario vacío para que guarde los usuarios

while True:
    print("╔═══════════════════════════╗")
    print("║          Acceso           ║")
    print("╠═══════════════════════════╣")
    print("║ 1. Registrarse            ║")
    print("║ 2. Iniciar sesión         ║")
    print("║ 3. Salir                  ║")
    print("╚═══════════════════════════╝")

    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        print("\n--- REGISTRO DE USUARIO ---")
        try:
            edad = int(input("Digite su edad: "))
        except ValueError:
            print("Error: La edad debe ser un número.")
            continue

        if not lb.validar_edad(edad): #validamos que sea +18 usando función establecida en libreria.py
            print("Debes tener al menos 18 años para registrarte.")
            continue

        nombre = input("Nombre de usuario: ")
        if not lb.validar_nombre(nombre): #validamos que contenga solo letras
            print("El nombre solo puede contener letras.")
            continue

        clave = input("Clave (máximo 6 dígitos numéricos): ")
        if not lb.validar_clave(clave): #validamos que contenga solo números y 6 dígitos
            print("La clave debe contener solo números y máximo 6 dígitos.")
            continue
        #con esto guardamos el usuario creado en el diccionario "usuarios"
        usuarios[nombre] = {
            "clave": clave,
            "edad": edad
        }

        print("Usuario registrado con éxito.")

    elif opcion == "2":
        print("\n--- INICIAR SESIÓN ---")

        #en caso de que no haya usuarios registrados para que se registre antes.
        if not usuarios:
            print("Aún no hay usuarios registrados. Regístrate primero.")
            continue

        #3 intentos de inicio de sesión
        intentos = 3
        while intentos > 0:
            nombre = input("Nombre de usuario: ")
            clave = input("Clave: ")
            #aquí comprobamos que el nombre esté ingresado en nuestro diccionario y si su clave sea la correcta del usuario
            if nombre in usuarios and usuarios[nombre]["clave"] == clave:
                print(f"Bienvenido/a {nombre}. Inicio de sesión exitoso.")
                break
            else:
                intentos -= 1
                print(f"Nombre o clave incorrectos. Te quedan {intentos} intento(s).")

        if intentos == 0:
            print("Has superado el número máximo de intentos. Vuelve a intentarlo desde el menú.")

    elif opcion == "3":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida. Intente de nuevo.")

