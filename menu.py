def registro():
    print("Bienvenido al Registro de Usuario")
    print("Por favor ingrese los siguientes datos: ")
    
    usuario = input("Nombre de Usuario: ")
    correo = input("Correo Electronico: ")

    while True:
        contraseña = input("Contraseña: ")
        confirmar_contraseña = input("Confirme la contraseña: ")

        if contraseña == confirmar_contraseña:
            print("¡Registro Exitoso!")
            sl1 = False
            return sl1 
        else:
            print("Las contraseñas no coinciden. Intente nuevamente")

def inicioSesion():
        print("Inicio de Sesion")
        usuario = input("Ingrese su Usuario: ")
        contraseña = input("Ingrese su Contraseña: ")
        print("¡Inicion de Sesion Exitoso!")
        sl2 = False
        return sl2

def menu():
    sl = True
    while sl:

        print("Bienvenido al menú Principal")
        print("1. Registro")
        print("2. Inicion de Sesión")
        print("3. salir")

        sl1 = True
        sl2 = True

        opcion = input("Por favor seleccione una opcion: ")
        if opcion == "1":
            while sl1:
                sl1 = registro()

        elif opcion == "2":
            while sl2:
                sl2 = inicioSesion()

        elif opcion == "3":
         print("¡Hasta Luego!")
         sl = False

        else: print("Opción invalida. intente nuevamente")

menu()