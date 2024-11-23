import csv

admin = [{"admin": 'admin1'}]
usuantig = [{'usu1': 'clave1', 'correo': 'correo1', 'perfil': {'nombre': 'Perfil1', 'generos': [], 'peliculas': []}},
            {'usu2': 'clave2', 'correo': 'correo1', 'perfil': {'nombre': 'Perfil2', 'generos': [], 'peliculas': []}}]
usunuev = []

# Listado de planes de suscripción con precios y características
planes_suscripcion = {
    "basico": {"precio": 10000, "caracteristicas": ["Acceso limitado"]},
    "estandar": {"precio": 20000, "caracteristicas": ["Acceso medio", "HD"]},
    "premium": {"precio": 30000, "caracteristicas": ["Acceso completo", "HD", "4K"]}
}

# Historial de pagos (puede cargarse de un archivo para persistencia)
historial_pagos = []
def J_ACTUALIZARINFO1():
    nombre = input('Digite su nuevo nombre:\n')
    contra = input('Digite su nueva contraseña:\n')
    if len(contra) <= 6 and contra.isalnum():
        usuantig[0]['usu1'] = str(contra)
    else:
        print('La contraseña debe ser alfanumérica y tener al menos 6 caracteres.')
        J_ACTUALIZARINFO1()
    correo = input('Digite su nuevo correo:\n')
    usuantig[0]['correo'] = str(correo)
    print('Datos almacenados con éxito')
    print(usuantig[0])
    Acceso()

def J_ACTUALIZARINFO2():
    nombre = input('Digite su nuevo nombre:\n')
    contra = input('Digite su nueva contraseña:\n')
    if len(contra) <= 6 and contra.isalnum():
        usuantig[1]['usu2'] = str(contra)
    else:
        print('La contraseña debe ser alfanumérica y tener al menos 6 caracteres.')
        J_ACTUALIZARINFO2()
    correo = input('Digite su nuevo correo:\n')
    usuantig[1]['correo'] = str(correo)
    print('Datos almacenados con éxito')
    print(usuantig[1])
    Acceso()

def J_PERZONALIZAR1():
    perfil = usuantig[0]['perfil']
    perfil['nombre'] = input('Digite el nuevo nombre del perfil:\n')
    perfil['generos'] = input('Ingrese sus géneros favoritos separados por comas:\n').split(',')
    perfil['peliculas'] = input('Ingrese sus películas favoritas separadas por comas:\n').split(',')
    print('Perfil personalizado con éxito')
    print(perfil)
    Acceso()

def J_PERZONALIZAR2():
    perfil = usuantig[1]['perfil']
    perfil['nombre'] = input('Digite el nuevo nombre del perfil:\n')
    perfil['generos'] = input('Ingrese sus géneros favoritos separados por comas:\n').split(',')
    perfil['peliculas'] = input('Ingrese sus películas favoritas separadas por comas:\n').split(',')
    print('Perfil personalizado con éxito')
    print(perfil)
    Acceso()
def mostrar_planes():
    print("Planes de suscripción disponibles:")
    for plan, detalles in planes_suscripcion.items():
        print(f"{plan.capitalize()}: Precio {detalles['precio']} - Características: {', '.join(detalles['caracteristicas'])}")

def registrar_pago(usuario, plan):
    precio = planes_suscripcion[plan]['precio']
    metodo_pago = input("Ingrese su método de pago (tarjeta de crédito/débito): ")
    print(f"Procesando pago de {precio} para el plan {plan.capitalize()} mediante {metodo_pago}...")
    
    # Guardar el pago en el historial
    pago = {"usuario": usuario, "plan": plan, "monto": precio, "metodo_pago": metodo_pago}
    historial_pagos.append(pago)
    
    with open('historial_pagos.csv', 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([usuario, plan, precio, metodo_pago])
    
    print("Pago realizado exitosamente.")

def ver_historial_pagos(usuario):
    print(f"Historial de pagos de {usuario}:")
    for pago in historial_pagos:
        if pago["usuario"] == usuario:
            print(f"Plan: {pago['plan'].capitalize()}, Monto: {pago['monto']}, Método: {pago['metodo_pago']}")

def cargar_historial_pagos():
    try:
        with open('historial_pagos.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                historial_pagos.append({"usuario": fila[0], "plan": fila[1], "monto": int(fila[2]), "metodo_pago": fila[3]})
    except FileNotFoundError:
        pass

def cargar_contenido():
    titulo = input("Ingrese el título: ")
    genero = input("Ingrese el género: ")
    duracion = input("Ingrese la duración: ")
    
    with open('contenido.csv', 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([titulo, genero, duracion])
    print("Contenido agregado exitosamente.")

def eliminar_contenido():
    titulo = input("Ingrese el título del contenido a eliminar: ")
    
    contenido = []
    with open('contenido.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] != titulo:
                contenido.append(fila)
    
    with open('contenido.csv', 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(contenido)
    print("Contenido eliminado exitosamente.")

def actualizar_contenido():
    titulo = input("Ingrese el título del contenido a actualizar: ")
    nuevo_titulo = input("Ingrese el nuevo título: ")
    nuevo_genero = input("Ingrese el nuevo género: ")
    nueva_duracion = input("Ingrese la nueva duración: ")
    
    contenido = []
    with open('contenido.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[0] == titulo:
                fila[0] = nuevo_titulo
                fila[1] = nuevo_genero
                fila[2] = nueva_duracion
            contenido.append(fila)
    
    with open('contenido.csv', 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(contenido)
    print("Contenido actualizado exitosamente.")

def J_ADMIN():
    modulo = int(input("1. Cargar contenido\n2. Eliminar contenido\n3. Actualizar contenido\n4. Gestión de suscripciones y pagos\n5. Salir\n"))
    if modulo == 1:
        cargar_contenido()
    elif modulo == 2:
        eliminar_contenido()
    elif modulo == 3:
        actualizar_contenido()
    elif modulo == 4:
        gestion_suscripciones()
    elif modulo == 5:
        exit()
    else:
        print("Dato erróneo")

def gestion_suscripciones():
    print("Gestión de suscripciones y pagos:")
    usuario = input("Ingrese el usuario para gestionar suscripciones: ")
    
    while True:
        print("\n1. Mostrar planes de suscripción")
        print("2. Registrar pago")
        print("3. Ver historial de pagos")
        print("4. Salir")
        
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

def J_CLIENTEANTI():
    usu = input("Ingrese su usuario: ").lower()
    contra = input("Ingrese su contraseña: ")
    if usu in usuantig[0] and contra == usuantig[0]['usu1']:
        print("BIENVENIDO USU1")
        modulo = int(input("PERFIL:\n\t1.PERFIL 1\n\t2.PERFIL 2\n\t3.PERSONALIZAR PERFIL\n\t4.Actualización de info\n\t5.Eliminar cuenta\n\t6.Salir\n"))
        if modulo == 1:
            pass
        elif modulo == 2:
            pass
        elif modulo == 3:
            J_PERZONALIZAR1()
        elif modulo == 4:
            J_ACTUALIZARINFO1()
        elif modulo == 5:
            opc = input('DESEA ELIMINAR SU CUENTA MARQUE:\n\t1.Eliminar\n\t2.CANCELAR\n')
            if opc == '1':
                print('Cuenta eliminada')
            if opc == '2':
                J_CLIENTEANTI()
        elif modulo == 6:
            Acceso()
        else:
            print("Dato erróneo")
    else:
        print("Usuario o contraseña erróneo")
    
    if usu in usuantig[1] and contra == usuantig[1]['usu2']:
        print("BIENVENIDO USU2")
        modulo = int(input("PERFIL:\n\t1.PERFIL 1\n\t2.PERFIL 2\n\t3.PERSONALIZAR PERFIL\n\t4.Actualización de info\n\t5.Eliminar cuenta\n\t6.Salir\n"))
        if modulo == 1:
            pass
        elif modulo == 2:
            pass
        elif modulo == 3:
            J_PERZONALIZAR2()
        elif modulo == 4:
            J_ACTUALIZARINFO2()
        elif modulo == 5:
            opc = input('DESEA ELIMINAR SU CUENTA MARQUE:\n\t1.Eliminar\n\t2.CANCELAR\n')
            if opc == '1':
                print('Cuenta eliminada')
            if opc == '2':
                J_CLIENTEANTI()
        elif modulo == 6:
            Acceso()
        else:
            print("Dato erróneo")
    else:
        print("Usuario o contraseña erróneo")

def J_CLIENTENUEV():
    with open('clientesnuevos.csv', 'a', newline='') as i:
        escri = csv.writer(i, delimiter=';')
        NOMBRE = input('Digite su nombre: \n')
        CORREO = input('Digite su correo: \n')
        CONTRA = input('Digite su contraseña alfanumérica de 6 dígitos: \n')
        if len(CONTRA) <= 6 and CONTRA.isalnum():
            escri.writerow([NOMBRE, CORREO, CONTRA])
            usunuev.append({'nombre': NOMBRE, 'correo': CORREO, 'contraseña': CONTRA, 'perfil': {'nombre': NOMBRE, 'generos': [], 'peliculas': []}})
            print(f'{NOMBRE}, tus datos se han almacenado con éxito\n')
        else:
            print('La contraseña debe ser alfanumérica y tener al menos 6 caracteres.')
            J_CLIENTENUEV()

def Acceso():
    cargar_historial_pagos()  # Cargar historial de pagos al iniciar
    while True:
        print("\nAcceso al Sistema")
        print("1. Administrador")
        print("2. Cliente Antiguo")
        print("3. Cliente Nuevo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            J_ADMIN()
        elif opcion == '2':
            J_CLIENTEANTI()
        elif opcion == '3':
            J_CLIENTENUEV()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Resto de las funciones se mantiene igual

while True:
    Acceso()
