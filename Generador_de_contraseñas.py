import random
import string

def Evaluar_Fuerza_Contraseña(contraseña):
    longitud = len(contraseña)
    tiene_mayus = any(c.isupper() for c in contraseña)
    tiene_minus = any(c.islower() for c in contraseña)
    tiene_num = any(c.isdigit() for c in contraseña)
    tiene_simbol = any(c in string.punctuation for c in contraseña)

    tipos = sum([tiene_mayus, tiene_minus, tiene_num, tiene_simbol])

    if longitud >= 12 and tipos >= 3:
        return "Fuerte."
    elif longitud >= 8 and tipos >= 2:
        return "Media."
    else:
        return "Débil."

def Generar_Contraseña(longitud, usar_mayus=True, usar_minus=True, usar_num=True, usar_simbol=True):
    caracteres = ""
    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_minus:
        caracteres += string.ascii_lowercase
    if usar_num:
        caracteres += string.digits
    if usar_simbol:
        caracteres += string.punctuation

    if not caracteres:
        return None
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def Solicitar_Si_o_No(mensaje):
    while True:
        respuesta = input(mensaje + " (S/N): ").strip().lower()
        if respuesta in ['s', 'n']:
            return respuesta == 's'
        print("Respuesta inválida. Intente con 'S' o 'N'.")

def Menu_Generacion():
    print("\n// OPCIONES DE GENERACIÓN DE CONTRASEÑA \\")
    print("1. Generar mi propia contraseña.")
    print("2. Contraseña automática fácil de decir (Solo Letras).")
    print("3. Contraseña automática fácil de leer (Letras + Opcional Números y Símbolos).")
    print("4. Todos los caracteres.")
    opcion = input("Seleccione una opción (1-4): ")

    while True:
        try:
            longitud = int(input("Ingrese la longitud deseada: "))
            if longitud > 0:
                break
            else:
                print("Debe ser un número mayor a 0.")
        except ValueError:
            print("Ingrese un número válido.")

    if opcion == '1':
        while True:
            contrasena = input(f"Ingrese su contraseña personalizada ({longitud} caracteres): ")
            if len(contrasena) == longitud:
                break
            else:
                print("La contraseña no cumple con la longitud especificada.")
    elif opcion == '2':
        contrasena = Generar_Contraseña(longitud, usar_mayus=True, usar_minus=True, usar_num=False, usar_simbol=False)
    elif opcion == '3':
        usar_num = Solicitar_Si_o_No("¿Desea incluir números?")
        usar_simbol = ("¿Desea incluir símbolos?")
        contrasena = Generar_Contraseña(longitud, usar_mayus=True, usar_minus=True, usar_num=usar_num, usar_simbol=usar_simbol)
    elif opcion == '4':
        print("Se usará combinación de mayúsculas, minúsculas, números y símbolos.")
        usar_completa = ("¿Desea usar esta combinación completa?")
        if usar_completa:
            contrasena = Generar_Contraseña(longitud, True, True, True, True)
        else:
            usar_mayus = ("¿Desea incluir mayúsculas?")
            usar_minus = ("¿Desea incluir minúsculas?")
            usar_num = ("¿Desea incluir números?")
            usar_simbol = ("¿Desea incluir símbolos?")
            combinaciones = sum([usar_mayus, usar_minus, usar_num, usar_simbol])
            if combinaciones < 3:
                print("Debe seleccionar al menos 3 combinaciones. Intente de nuevo.")
                return Menu_Generacion()
            contrasena = Generar_Contraseña(longitud, usar_mayus, usar_minus, usar_num, usar_simbol)
    else:
        print("Opción inválida.")
        return

    print(f"\nContraseña generada: {contrasena}")
    print("Fuerza de la contraseña:", Evaluar_Fuerza_Contraseña(contrasena))

def mostrar_reglas():
    print("\n// REGLAS DEL GENERADOR DE CONTRASEÑAS \\")
    print("- La contraseña puede contener mayúsculas, minúsculas, números y símbolos.")
    print("- Se recomienda que tenga al menos 12 caracteres.")
    print("- Una contraseña fuerte debe combinar al menos 3 tipos de caracteres.")
    print("- No use información personal predecible.")

def menu_principal():
    while True:
        print("__________________________________")
        print("|                                |")
        print("|Generador de Contraseñas Seguras|")
        print("|________________________________|")
        print("\n// MENÚ PRINCIPAL \\")
        print("1. Generar contraseña.")
        print("2. Reglas del generador de contraseña.")
        print("3. Salir.")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            Menu_Generacion()
        elif opcion == '2':
            mostrar_reglas()
        elif opcion == '3':
            print("Gracias por usar el generador de contraseñas.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu_principal()

        
