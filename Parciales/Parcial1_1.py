import csv

F_usuarios = []

def contraseña(J_F):
    return len(J_F) == 6 and J_F.isalnum()

def registro():
    while len(F_usuarios) < 5:
        J_nombre = input("Ingrese el nombre de usuario: ")
        J_correo = input("Ingrese el correo electrónico: ")
        J_clave = input("Ingrese la contraseña: ")

        while not contraseña(J_clave):
            print("Contraseña inválida. Debe ser alfanumérica y tener exactamente 6 caracteres.")
            J_clave = input("Ingrese la contraseña (debe ser alfanumérica y tener exactamente 6 caracteres): ")

        F_usuarios.append({"usuario": J_nombre, "correo": J_correo, "contraseña": J_clave})
        print("!!!USUARIO REGISTRADO!!!")

        if len(F_usuarios) < 5:
            op = input("¿Desea registrar otro usuario? (Si/No): ")
            if op.lower() != 'si':
                break

    if len(F_usuarios) < 5:
        print("!!!AUN NO SE ALCANZA EL LIMITE MINIMO DE REGISTROS!!!")

def ingreso():
    J_usuario = input("Ingrese su nombre de usuario: ")
    J_clave = input("Ingrese su contraseña: ")
    
    for usuario in F_usuarios:
        if usuario["usuario"] == J_usuario and usuario["contraseña"] == J_clave:
            print("Ingreso exitoso. Bienvenido!")
            return
    
    print("Usuario o contraseña incorrectos.")

def menu():
    while True:
        print('### BIENVENIDO AL PROGRAMA ###')
        op1 = input('Marque: 1. Registrar Usuario\n\t2. Ingresar Usuario\n\t3. Salir\nIngrese la opcion: ')
        print(f'\n')

        if op1 == '1':
            print('####### REGISTRAR USUARIO #######')
            registro()
            print(f'\n')

        elif op1 == '2':
            print('####### INGRESAR USUARIO #######')
            ingreso()
            print(f'\n')

        elif op1 == '3':
            exit()

        else:
            print("!!!Ingrese una opción valida!!!")

while True:   
    menu()



















