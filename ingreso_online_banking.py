import random

def online_banking():
    user_correcto = "admin"
    pass_correcta = "admin"
    intentos = 0

    print("Bienvenido al online banking!")

    while True:
        # Generar un token de 6 dígitos
        token_correcto = random.randint(100000, 999999)
        print("Token:", token_correcto)

        # Pedir credenciales
        user_usuario = input("Ingrese usuario: ")
        pass_usuario = input("Ingrese contraseña: ")
        token_usuario = input("Ingrese token: ")

        # Validar credenciales
        if user_usuario.lower() == user_correcto and pass_usuario == pass_correcta and token_usuario == str(token_correcto):
            print("Bienvenido a su Online Banking!")
            break
        else:
            intentos += 1
            if intentos == 3:
                print("Usuario bloqueado. Demasiados intentos fallidos.")
                break

            # Si aún quedan intentos
            print(f"Credenciales incorrectas. Intento {intentos} de 3.")
            ingreso = input("¿Desea intentar nuevamente? (s/n): ")
            if ingreso.lower() != "s":
                print("Gracias por utilizar online banking.")
                break

# Ejecutar la función
online_banking()