import csv

# Planes de suscripción
planes_suscripcion = {
    "basico": {"precio": 1000, "caracteristicas": ["Acceso limitado"]},
    "estandar": {"precio": 2000, "caracteristicas": ["Acceso medio", "HD"]},
    "premium": {"precio": 3000, "caracteristicas": ["Acceso completo", "HD", "4K"]}
}

historial_pagos = []

# Cargar clientes desde CSV
def cargar_clientes():
    clientes = []
    try:
        with open('Parciales/Archivos/clientes.csv', 'r') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                cliente = {
                    'nombre': fila['nombre'],
                    'correo': fila['correo'],
                    'contraseña': fila['contraseña'],
                    'perfil': {
                        'nombre': fila['perfil'],
                        'generos': fila['generos'].split(','),
                        'peliculas': fila['peliculas'].split(',')
                    }
                }
                clientes.append(cliente)
    except FileNotFoundError:
        pass  # Si el archivo no existe, simplemente regresamos una lista vacía
    return clientes

# Guardar cliente nuevo en CSV
def guardar_cliente(cliente):
    with open('Parciales/Archivos/clientes.csv', 'a', newline='') as archivo:
        campos = ['nombre', 'correo', 'contraseña', 'perfil', 'generos', 'peliculas']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        # Si el archivo está vacío, escribimos la cabecera
        if archivo.tell() == 0:
            escritor.writeheader()
        escritor.writerow({
            'nombre': cliente['nombre'],
            'correo': cliente['correo'],
            'contraseña': cliente['contraseña'],
            'perfil': cliente['perfil']['nombre'],
            'generos': ','.join(cliente['perfil']['generos']),
            'peliculas': ','.join(cliente['perfil']['peliculas'])
        })

# Función para clientes nuevos
def J_clientenuev():
    NOMBRE = input('Digite su nombre: ')
    CORREO = input('Digite su correo: ')
    CONTRA = input('Digite su contraseña alfanumérica de al menos 6 dígitos: ')
    
    if len(CONTRA) >= 6 and CONTRA.isalnum():
        # Crear nuevo cliente
        nuevo_cliente = {
            'nombre': NOMBRE,
            'correo': CORREO,
            'contraseña': CONTRA,
            'perfil': {'nombre': NOMBRE, 'generos': [], 'peliculas': []}
        }
        # Guardar cliente en el CSV
        guardar_cliente(nuevo_cliente)
        print(f'{NOMBRE}, tus datos se han almacenado con éxito y ahora eres un cliente antiguo.\n')
    else:
        print('La contraseña debe ser alfanumérica y tener al menos 6 caracteres.')
        J_clientenuev()

# Función para acceso de clientes antiguos
def J_clienteanti():
    usu = input("Ingrese su usuario: ").lower()
    contra = input("Ingrese su contraseña: ")

    clientes = cargar_clientes()

    # Verificar si el usuario y contraseña coinciden con algún cliente antiguo
    for cliente in clientes:
        if cliente['nombre'].lower() == usu and cliente['contraseña'] == contra:
            print(f"BIENVENIDO {usu.upper()}")
            gestionar_usuario(cliente, usu)
            return
    
    # Si no se encuentra el usuario:
    print("Usuario o contraseña incorrectos.")

# Función para acceso como administrador
def J_admin():
    usu = input("Ingrese su usuario de administrador: ").lower()
    contra = input("Ingrese su contraseña de administrador: ")

    if usu == "admin" and contra == "admin1":
        print("BIENVENIDO ADMINISTRADOR")
        gestionar_administrador()
    else:
        print("Usuario o contraseña de administrador incorrectos.")

# Función para gestionar el menú de administrador
def gestionar_administrador():
    while True:
        
        print("\nMenú de administrador:")
        print("1. Ver todos los clientes")
        print("2. Ver historial de pagos")
        print("3. Cargar contenido")
        print("4. Eliminar contenido")
        print("5. Actualizar contenido")    
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            clientes = cargar_clientes()
            print("Clientes registrados:")
            for cliente in clientes:
                print(f"Nombre: {cliente['nombre']}, Correo: {cliente['correo']}")
        elif opcion == '2':
            ver_todos_historial_pagos()
        elif opcion == '3':
            cargar_contenido()
        elif opcion == '4':
            eliminar_contenido()
        elif opcion == '5':
            actualizar_contenido()      
        elif opcion == '6':
            Acceso()
        else:
            print("Opción no válida. Intente de nuevo.")

def cargar_contenido():
    titulo = input("Ingrese el título: ")
    genero = input("Ingrese el género: ")
    duracion = input("Ingrese la duración: ")
    
    with open('Parciales/Archivos/contenido.csv', 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([titulo, genero, duracion])
    print("Contenido agregado exitosamente.")

def eliminar_contenido():
    titulo = input("Ingrese el título del contenido a eliminar: ")
    
    contenido = []
    with open('Parciales/Archivos/contenido.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] != titulo:
                contenido.append(fila)
    
    with open('Parciales/Archivos/contenido.csv', 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(contenido)
    print("Contenido eliminado exitosamente.")

def actualizar_contenido():
    titulo = input("Ingrese el título del contenido a actualizar: ")
    nuevo_titulo = input("Ingrese el nuevo título: ")
    nuevo_genero = input("Ingrese el nuevo género: ")
    nueva_duracion = input("Ingrese la nueva duración: ")
    
    contenido = []
    with open('Parciales/Archivos/contenido.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] == titulo:
                fila[0] = nuevo_titulo
                fila[1] = nuevo_genero
                fila[2] = nueva_duracion
            contenido.append(fila)
    
    with open('Parciales/Archivos/contenido.csv', 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(contenido)
    print("Contenido actualizado exitosamente.")


# Función para ver todo el historial de pagos (para el administrador)
def ver_todos_historial_pagos():
    try:
        with open('Parciales/Archivos/historial_pagos.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            print("Historial de pagos:")
            for fila in lector:
                print(f"Usuario: {fila[0]}, Plan: {fila[1]}, Monto: {fila[2]}, Método de pago: {fila[3]}")
    except FileNotFoundError:
        print("No se ha encontrado un historial de pagos.")

# Funciones relacionadas con la gestión de usuario
def gestionar_usuario(cliente, usu):
    while True:
        modulo = int(input(f"PERFIL:\n\t1. Ver Perfil {usu}\n\t2. Personalizar Perfil\n\t3. Actualizar Info\n\t4. Eliminar cuenta\n\t5. Ver/gestionar suscripción\n\t6. Salir\n"))
        if modulo == 1:
            print(cliente)
        elif modulo == 2:
            personalizar_perfil(cliente)
        elif modulo == 3:
            actualizar_info(cliente)
        elif modulo == 4:
            eliminar_cuenta(cliente)
        elif modulo == 5:
            gestionar_suscripcion(usu)
        elif modulo == 6:
            Acceso()
        else:
            print("Dato erróneo")

# Función para personalizar perfil
def personalizar_perfil(cliente):
    perfil = cliente['perfil']
    perfil['nombre'] = input('Digite el nuevo nombre del perfil:\n')
    perfil['generos'] = input('Ingrese sus géneros favoritos separados por comas:\n').split(',')
    perfil['peliculas'] = input('Ingrese sus películas favoritas separadas por comas:\n').split(',')
    print('Perfil personalizado con éxito')
    print(perfil)

# Función para actualizar información de usuario
def actualizar_info(cliente):
    nombre = input('Digite su nuevo nombre:\n')
    contra = input('Digite su nueva contraseña (mínimo 6 caracteres):\n')
    
    if len(contra) >= 6 and contra.isalnum():
        cliente['contraseña'] = contra
    else:
        print('La contraseña debe ser alfanumérica y tener al menos 6 caracteres.')
        actualizar_info(cliente)
    
    correo = input('Digite su nuevo correo:\n')
    cliente['correo'] = correo
    print('Datos almacenados con éxito')
    print(cliente)

# Función para eliminar cuenta
def eliminar_cuenta(cliente):
    opc = input('DESEA ELIMINAR SU CUENTA MARQUE:\n\t1.Eliminar\n\t2.CANCELAR\n')
    if opc == '1':
        clientes = cargar_clientes()
        clientes = [c for c in clientes if c['nombre'] != cliente['nombre']]
        with open('Parciales/Archivos/clientes.csv', 'w', newline='') as archivo:
            campos = ['nombre', 'correo', 'contraseña', 'perfil', 'generos', 'peliculas']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(clientes)
        print('Cuenta eliminada')
    elif opc == '2':
        J_clienteanti()

# Función para gestionar suscripción
def gestionar_suscripcion(usuario):
    while True:
        print("\nGestión de suscripción:")
        print("1. Mostrar planes de suscripción")
        print("2. Registrar pago")
        print("3. Ver historial de pagos")
        print("4. Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            mostrar_planes()
        elif opcion == '2':
            plan = input("Ingrese el plan que desea (basico, estandar, premium): ").lower()
            if plan in planes_suscripcion:
                registrar_pago(usuario, plan)
            else:
                print("Plan no válido. Intente de nuevo.")
        elif opcion == '3':
            ver_historial_pagos(usuario)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Funciones auxiliares
def mostrar_planes():
    print("Planes de suscripción disponibles:")
    for plan, detalles in planes_suscripcion.items():
        print(f"{plan.capitalize()}: Precio {detalles['precio']} - Características: {', '.join(detalles['caracteristicas'])}")

def registrar_pago(usuario, plan):
    precio = planes_suscripcion[plan]['precio']
    metodo_pago = input("Ingrese su método de pago (tarjeta de crédito/débito): ")
    print(f"Procesando pago de {precio} para el plan {plan} mediante {    metodo_pago}...")
    
    # Guardar el pago en el historial
    historial_pagos.append({'usuario': usuario, 'plan': plan, 'monto': precio, 'metodo_pago': metodo_pago})
    
    with open('Parciales/Archivos/historial_pagos.csv', 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([usuario, plan, precio, metodo_pago])
    
    print("Pago registrado con éxito.")

def ver_historial_pagos(usuario):
    try:
        with open('Parciales/Archivos/historial_pagos.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            print(f"Historial de pagos para {usuario}:")
            for fila in lector:
                if fila[0] == usuario:
                    print(f"Plan: {fila[1]}, Monto: {fila[2]}, Método de pago: {fila[3]}")
    except FileNotFoundError:
        print("No se ha encontrado un historial de pagos.")

# Función principal para acceder al sistema
def Acceso():
    while True:
        print("BIENVENIDO")
        print("1. Ingresar como administrador")
        print("2. Ingresar como cliente antiguo")
        print("3. Ingresar como cliente nuevo")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            J_admin()
        elif opcion == '2':
            J_clienteanti()
        elif opcion == '3':
            J_clientenuev()
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

while True:
    Acceso()


