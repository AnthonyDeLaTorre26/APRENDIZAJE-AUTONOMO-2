import random
import string
def Solicitar_Si_o_No(mensaje):
    #Función para recibir respuesta de usuario: Si/No.
    while True:
        respuesta = input(mensaje + "(S/N):").lower()
        if respuesta in ['s', 'n']:
            return respuesta == 's'
        print("Responder con 's' (Si) o 'n' (No).")

def Generar_Contraseña(longitud, usar_mayus, usar_minus, usar_num, usar_simbol):
    #Genera una contraseña nueva y segura según los siguientes parametros.
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
        return None #Error: Caracteres no válidos.
    
     #Generar la Contraseña.
    return ''.join(random.choice(caracteres)for _ in range(longitud))

print("__________________________________")
print("|                                |")
print("|Generador de Contraseñas Seguras|")
print("|________________________________|")

if not Solicitar_Si_o_No("¿Desea Generar una Contraseña Segura?"):
    print("Solicitud Rechazada")
else: 
    #Solicitar Longitud de Contraseña.
    while True:
        try:
            Longitud = int(input("Ingresar Longitud de Contraseña: "))
            if Longitud > 0:
                break
            else:
                print("La Longitud debe ser mayor a 0.")
        except ValueError:
            print("Ingresar un número válido.")

    #Selección de lista de caracteres.
    usar_letras = Solicitar_Si_o_No("¿Desea Incluir Letras?")
    usar_mayus = usar_letras and Solicitar_Si_o_No("¿Desea Incluir Mayúsculas?")
    usar_minus = usar_letras and Solicitar_Si_o_No("¿Desea Inlcuir Minúsculas?")
    usar_num = Solicitar_Si_o_No("¿Desea Inluir Números?")
    usar_simbol = Solicitar_Si_o_No("¿Desea Incluir Símbolos?")

    #Generar Contraseña
    Contraseña = Generar_Contraseña(Longitud, usar_mayus, usar_minus, usar_num, usar_simbol)
    if Contraseña is None:
        print("Error: No se seleccionó ningún caracter. No se puede generar contraseña")
    else:
        print("\nCONTRASEÑA GENERADA:", Contraseña)
        
        #Preguntar si desea realizar modificaciones a la contraseña
        if Solicitar_Si_o_No("¿Desea Modificar su Contraseña Generada?"):
            Contraseña = input("Ingrese Nueva Contraseña Manualmente: ")
            print("Nueva Contraseña Generada: ", Contraseña)
        
        print("\nContraseña Final:")
        print( Contraseña)

        
