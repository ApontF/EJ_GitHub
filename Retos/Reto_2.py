''' 2. En un parqueadero se debe optimizar el manejo de la información y para agilizar el proceso de pagos es necesario registrar 
los vehículos al entrar sean carros o motos por placa, contabilizar el tiempo de permanencia y así obtener el valor a cancelar 
por cada vehículo. Se solicita tener los siguientes datos: cantidad de vehículos por tipo (moto o carro), placas, hora de 
entrada y salida, duración de parqueo y precio cobrado.Diseñe un algoritmo e impleméntelo con Python, este debe ser repetitivo y 
cumplir con las peticiones de la situación. ACLARACIÓN: Su programa registra el ingreso, pero debe seleccionar si es MOTO o CARRO, 
escribir la placa, luego escribir la hora de entrada empleando el formato de 24 horas (ingreso: 10:35), y salida (salida: 12:15), 
calcular la duración del servicio de parqueo (duración:100 min) y cobrar a la salida del parqueadero, para eso debe ingresar la 
placa y su programa le regresa el cálculo de duración y precio a cobrar. Usted dispone de los precios por fracción 
(cada 15 minutos) de parqueo para motos ($500) y carros ($1000). Debe crearse un dato que me permita saber cuántos carros y motos 
ingresaron al parqueadero durante el día y el dinero recogido. No olvide emplear un menú que le facilite el proceso. '''



import datetime

# Precios por fracción de 15 minutos
PRECIO_MOTO = 500
PRECIO_CARRO = 1000

# Listas para almacenar los registros de vehículos
vehiculos = []

# Función para calcular la diferencia en minutos entre dos horas
def calcular_duracion(entrada, salida):
    formato = "%H:%M"  # Formato de 24 horas
    entrada_dt = datetime.datetime.strptime(entrada, formato)
    salida_dt = datetime.datetime.strptime(salida, formato)
    duracion = (salida_dt - entrada_dt).total_seconds() / 60  # Duración en minutos
    return int(duracion)

# Función para calcular el precio a pagar según el tipo de vehículo y la duración
def calcular_precio(duracion, tipo):
    fracciones = duracion // 15
    if duracion % 15 != 0:
        fracciones += 1
    if tipo == 'MOTO':
        return fracciones * PRECIO_MOTO
    elif tipo == 'CARRO':
        return fracciones * PRECIO_CARRO

# Función para registrar un vehículo al entrar
def registrar_entrada():
    tipo = input("Ingrese el tipo de vehículo (MOTO/CARRO): ").upper()
    placa = input("Ingrese la placa del vehículo: ").upper()
    hora_entrada = input("Ingrese la hora de entrada (HH:MM en formato 24 horas): ")
    
    vehiculo = {
        'tipo': tipo,
        'placa': placa,
        'hora_entrada': hora_entrada,
        'hora_salida': None,
        'duracion': None,
        'precio': None
    }
    
    vehiculos.append(vehiculo)
    print(f"Vehículo {tipo} con placa {placa} registrado a las {hora_entrada}.\n")

# Función para registrar la salida de un vehículo y calcular el precio
def registrar_salida():
    placa = input("Ingrese la placa del vehículo que va a salir: ").upper()
    
    # Buscar el vehículo por la placa
    for vehiculo in vehiculos:
        if vehiculo['placa'] == placa and vehiculo['hora_salida'] is None:
            hora_salida = input("Ingrese la hora de salida (HH:MM en formato 24 horas): ")
            vehiculo['hora_salida'] = hora_salida
            duracion = calcular_duracion(vehiculo['hora_entrada'], hora_salida)
            vehiculo['duracion'] = duracion
            vehiculo['precio'] = calcular_precio(duracion, vehiculo['tipo'])
            
            print(f"Vehículo {vehiculo['tipo']} con placa {vehiculo['placa']} ha permanecido {duracion} minutos.")
            print(f"El valor a pagar es: ${vehiculo['precio']}.\n")
            return
    print("Vehículo no encontrado o ya registrado como salido.\n")

# Función para mostrar el resumen del día (cantidad de vehículos y dinero recaudado)
def mostrar_resumen():
    total_carros = sum(1 for v in vehiculos if v['tipo'] == 'CARRO')
    total_motos = sum(1 for v in vehiculos if v['tipo'] == 'MOTO')
    dinero_carros = sum(v['precio'] for v in vehiculos if v['tipo'] == 'CARRO' and v['precio'] is not None)
    dinero_motos = sum(v['precio'] for v in vehiculos if v['tipo'] == 'MOTO' and v['precio'] is not None)
    
    print(f"Resumen del día:")
    print(f"Total de carros ingresados: {total_carros}")
    print(f"Total de motos ingresadas: {total_motos}")
    print(f"Dinero recaudado por carros: ${dinero_carros}")
    print(f"Dinero recaudado por motos: ${dinero_motos}\n")

# Menú principal
def menu():
    while True:
        print("1. Registrar entrada de vehículo")
        print("2. Registrar salida de vehículo")
        print("3. Mostrar resumen del parqueadero")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_entrada()
        elif opcion == "2":
            registrar_salida()
        elif opcion == "3":
            mostrar_resumen()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

# Iniciar el programa
menu()
