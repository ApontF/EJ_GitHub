'''
Diseñe un programa en Python, aplicando clases y objetos que tenga dos opciones (2 clases): convierta un número entero a número romano o convierta un número romano en un número
entero. Aclaración: Recuerde que las clases tienen atributos y métodos(funciones).  
'''



class NumeroRomano:
    def __init__(self):
        # Diccionarios de conversión
        self.numero_romano = {
            1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
            20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C',
            200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M'
        }
        #Para invertir el diccionario
        self.numero_decimal = {v: k for k, v in self.numero_romano.items()}
        self.menu()

    def numero_a_romano(self):
        try:
            numero = int(input("Ingrese el número a convertir (entre 1 y 1000): "))
            if numero < 1 or numero > 1000:
                print("Por favor, ingrese un número entre 1 y 1000.")
                return
            
            romano = ""
            for valor in sorted(self.numero_romano.keys(), reverse=True):
                while numero >= valor:
                    romano += self.numero_romano[valor]
                    numero -= valor
            print(f"El número en romano es: {romano}")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    def romano_a_numero(self):
        simbolo = input("Ingrese el número romano a convertir: ").upper()
        if all(c in "IVXLCDM" for c in simbolo):
            decimal = 0
            i = 0
            while i < len(simbolo):
                if i + 1 < len(simbolo) and simbolo[i:i+2] in self.numero_decimal:
                    decimal += self.numero_decimal[simbolo[i:i+2]]
                    i += 2
                else:
                    decimal += self.numero_decimal[simbolo[i]]
                    i += 1
            print(f"El número en decimal es: {decimal}")
        else:
            print("Símbolo inválido. Por favor, ingrese un número romano válido.")

#     def menu(self):
#         while True:
#             print("\nMenu:")
#             print("\t1. Convertir número romano a entero")
#             print("\t2. Convertir número entero a romano")
#             print("\t3. Salir")
#             opcion = input("Seleccione una opción: ")

#             if opcion == '1':
#                 self.romano_a_numero()
#             elif opcion == '2':
#                 self.numero_a_romano()
#             elif opcion == '3':
#                 print(f"\n😊😊 ¡Gracias por usar el sistema de conversión de números! 😊😊\n")
#                 exit()
#             else:
#                 print("Opción no válida, por favor intente nuevamente.")


# while True:
#     a = NumeroRomano()






'''
Diseñe un programa para un zoológico, por medio de clases y objetos. Su programa debe permitir almacenar información de animales por especies (terrestre,
aéreos y acuáticos) y las características de cada uno por especie. Aclaración: Cuando se ejecuta el programa debe preguntar que especie de animal desea 
ingresar, según su selección haremos una clase para cada especie y el objeto que se cree solicita las características pertinentes. 
'''

# import pandas as pd

# class Zoologico:
#     def __init__(self, archivo_terrestres='Archivos/POO/terrestres.csv', archivo_aereos='Archivos/POO/aereos.csv', archivo_acuaticos='Archivos/POO/acuaticos.csv'):
#         self.archivo_terrestres = archivo_terrestres
#         self.archivo_aereos = archivo_aereos
#         self.archivo_acuaticos = archivo_acuaticos

#         # Cargar o crear archivos específicos para cada tipo de animal
#         try:
#             self.df_terrestres = pd.read_csv(self.archivo_terrestres)
#         except FileNotFoundError:
#             self.df_terrestres = pd.DataFrame(columns=['Nombre', 'Especie', 'Edad', 'Velocidad'])
#             self.df_terrestres.to_csv(self.archivo_terrestres, index=False)
#             print(f"Archivo creado: {self.archivo_terrestres}")

#         try:
#             self.df_aereos = pd.read_csv(self.archivo_aereos)
#         except FileNotFoundError:
#             self.df_aereos = pd.DataFrame(columns=['Nombre', 'Especie', 'Edad', 'Envergadura'])
#             self.df_aereos.to_csv(self.archivo_aereos, index=False)
#             print(f"Archivo creado: {self.archivo_aereos}")

#         try:
#             self.df_acuaticos = pd.read_csv(self.archivo_acuaticos)
#         except FileNotFoundError:
#             self.df_acuaticos = pd.DataFrame(columns=['Nombre', 'Especie', 'Edad', 'Profundidad'])
#             self.df_acuaticos.to_csv(self.archivo_acuaticos, index=False)
#             print(f"Archivo creado: {self.archivo_acuaticos}")

#         # Inicia el menú del zoológico
#         self.menu()

#     def agregar_animal(self, tipo):
#         nombre = input("Ingrese el nombre del animal: ")
#         especie = input("Ingrese la especie del animal: ")
#         edad = int(input("Ingrese la edad del animal (en años): "))
        
#         if tipo == 'terrestre':
#             velocidad = float(input("Ingrese la velocidad máxima (km/h): "))
#             nuevo_animal = pd.DataFrame({
#                 'Nombre': [nombre],
#                 'Especie': [especie],
#                 'Edad': [edad],
#                 'Velocidad': [velocidad]
#             })
#             self.df_terrestres = pd.concat([self.df_terrestres, nuevo_animal], ignore_index=True)
#             self.df_terrestres.to_csv(self.archivo_terrestres, index=False)

#         elif tipo == 'aereo':
#             envergadura = float(input("Ingrese la envergadura (m): "))
#             nuevo_animal = pd.DataFrame({
#                 'Nombre': [nombre],
#                 'Especie': [especie],
#                 'Edad': [edad],
#                 'Envergadura': [envergadura]
#             })
#             self.df_aereos = pd.concat([self.df_aereos, nuevo_animal], ignore_index=True)
#             self.df_aereos.to_csv(self.archivo_aereos, index=False)

#         elif tipo == 'acuatico':
#             profundidad = float(input("Ingrese la profundidad máxima que alcanza (m): "))
#             nuevo_animal = pd.DataFrame({
#                 'Nombre': [nombre],
#                 'Especie': [especie],
#                 'Edad': [edad],
#                 'Profundidad': [profundidad]
#             })
#             self.df_acuaticos = pd.concat([self.df_acuaticos, nuevo_animal], ignore_index=True)
#             self.df_acuaticos.to_csv(self.archivo_acuaticos, index=False)

#         print(f"✅ Animal {tipo} agregado correctamente ✅")

#     def mostrar_animales(self, tipo):
#         if tipo == 'terrestre':
#             print("Animales Terrestres:")
#             print(self.df_terrestres)
#         elif tipo == 'aereo':
#             print("Animales Aéreos:")
#             print(self.df_aereos)
#         elif tipo == 'acuatico':
#             print("Animales Acuáticos:")
#             print(self.df_acuaticos)

#     def menu(self):
#         while True:
#             print("\n!!! MENÚ DEL ZOOLÓGICO !!!\n")
#             print("\t1. Agregar Animal Terrestre")
#             print("\t2. Agregar Animal Aéreo")
#             print("\t3. Agregar Animal Acuático")
#             print("\t4. Mostrar Animales Terrestres")
#             print("\t5. Mostrar Animales Aéreos")
#             print("\t6. Mostrar Animales Acuáticos")
#             print("\t7. Salir")
#             opcion = input("Seleccione una opción: ")

#             if opcion == '1':
#                 self.agregar_animal('terrestre')
#             elif opcion == '2':
#                 self.agregar_animal('aereo')
#             elif opcion == '3':
#                 self.agregar_animal('acuatico')
#             elif opcion == '4':
#                 self.mostrar_animales('terrestre')
#             elif opcion == '5':
#                 self.mostrar_animales('aereo')
#             elif opcion == '6':
#                 self.mostrar_animales('acuatico')
#             elif opcion == '7':
#                 print("👋👋 Saliendo del sistema del zoológico 👋👋\n")
#                 break
#             else:
#                 print("Opción no válida. Por favor, seleccione una opción correcta.")

# while True:
#     zoologico = Zoologico()


'''
Diseñe un programa aplicando POO para un concesionario de autos (automóviles, camionetas, camiones, tractocamiones), tenga en cuenta
las características en común y cree las clases necesarias, por ejemplo modelos, tipo de pintura, cantidades de unidades en inventario. 
'''

import pandas as pd

class Concesionario:
    def __init__(self, archivo_automoviles='Archivos/POO/automoviles.csv', archivo_camionetas='Archivos/POO/camionetas.csv', archivo_camiones='Archivos/POO/camiones.csv', archivo_tractocamiones='Archivos/POO/tractocamiones.csv'):
        self.archivo_automoviles = archivo_automoviles
        self.archivo_camionetas = archivo_camionetas
        self.archivo_camiones = archivo_camiones
        self.archivo_tractocamiones = archivo_tractocamiones

        try:
            self.df_automoviles = pd.read_csv(self.archivo_automoviles)
        except FileNotFoundError:
            self.df_automoviles = pd.DataFrame(columns=['Modelo', 'Pintura', 'Unidades'])
            self.df_automoviles.to_csv(self.archivo_automoviles, index=False)
            print(f"Archivo creado: {self.archivo_automoviles}")

        try:
            self.df_camionetas = pd.read_csv(self.archivo_camionetas)
        except FileNotFoundError:
            self.df_camionetas = pd.DataFrame(columns=['Modelo', 'Pintura', 'Unidades'])
            self.df_camionetas.to_csv(self.archivo_camionetas, index=False)
            print(f"Archivo creado: {self.archivo_camionetas}")

        try:
            self.df_camiones = pd.read_csv(self.archivo_camiones)
        except FileNotFoundError:
            self.df_camiones = pd.DataFrame(columns=['Modelo', 'Pintura', 'Unidades'])
            self.df_camiones.to_csv(self.archivo_camiones, index=False)
            print(f"Archivo creado: {self.archivo_camiones}")

        try:
            self.df_tractocamiones = pd.read_csv(self.archivo_tractocamiones)
        except FileNotFoundError:
            self.df_tractocamiones = pd.DataFrame(columns=['Modelo', 'Pintura', 'Unidades'])
            self.df_tractocamiones.to_csv(self.archivo_tractocamiones, index=False)
            print(f"Archivo creado: {self.archivo_tractocamiones}")

        self.menu()

    def agregar_vehiculo(self, tipo):
        modelo = input("Ingrese el modelo del vehículo: ")
        pintura = input("Ingrese el tipo de pintura: ")
        unidades = int(input("Ingrese la cantidad de unidades en inventario: "))
        
        nuevo_vehiculo = pd.DataFrame({
            'Modelo': [modelo],
            'Pintura': [pintura],
            'Unidades': [unidades]
        })

        if tipo == 'automovil':
            self.df_automoviles = pd.concat([self.df_automoviles, nuevo_vehiculo], ignore_index=True)
            self.df_automoviles.to_csv(self.archivo_automoviles, index=False)

        elif tipo == 'camioneta':
            self.df_camionetas = pd.concat([self.df_camionetas, nuevo_vehiculo], ignore_index=True)
            self.df_camionetas.to_csv(self.archivo_camionetas, index=False)

        elif tipo == 'camion':
            self.df_camiones = pd.concat([self.df_camiones, nuevo_vehiculo], ignore_index=True)
            self.df_camiones.to_csv(self.archivo_camiones, index=False)

        elif tipo == 'tractocamion':
            self.df_tractocamiones = pd.concat([self.df_tractocamiones, nuevo_vehiculo], ignore_index=True)
            self.df_tractocamiones.to_csv(self.archivo_tractocamiones, index=False)

        print(f"Vehículo {tipo} agregado correctamente.")

    def mostrar_inventario(self, tipo):
        if tipo == 'automovil':
            print("Inventario de Automóviles:")
            print(self.df_automoviles)
        elif tipo == 'camioneta':
            print("Inventario de Camionetas:")
            print(self.df_camionetas)
        elif tipo == 'camion':
            print("Inventario de Camiones:")
            print(self.df_camiones)
        elif tipo == 'tractocamion':
            print("Inventario de Tractocamiones:")
            print(self.df_tractocamiones)

    def menu(self):
        while True:
            print("\nMenú del Concesionario:")
            print("1. Agregar Automóvil")
            print("2. Agregar Camioneta")
            print("3. Agregar Camión")
            print("4. Agregar Tractocamión")
            print("5. Mostrar Inventario de Automóviles")
            print("6. Mostrar Inventario de Camionetas")
            print("7. Mostrar Inventario de Camiones")
            print("8. Mostrar Inventario de Tractocamiones")
            print("9. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.agregar_vehiculo('automovil')
            elif opcion == '2':
                self.agregar_vehiculo('camioneta')
            elif opcion == '3':
                self.agregar_vehiculo('camion')
            elif opcion == '4':
                self.agregar_vehiculo('tractocamion')
            elif opcion == '5':
                self.mostrar_inventario('automovil')
            elif opcion == '6':
                self.mostrar_inventario('camioneta')
            elif opcion == '7':
                self.mostrar_inventario('camion')
            elif opcion == '8':
                self.mostrar_inventario('tractocamion')
            elif opcion == '9':
                print("Saliendo del sistema del concesionario.")
                exit()
            else:
                print("Opción no válida. Por favor, seleccione una opción correcta.")

while True: 
    concesionario = Concesionario()



























