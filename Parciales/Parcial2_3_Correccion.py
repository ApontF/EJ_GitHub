import pandas as pd
from datetime import datetime

class AdministradorZoo:
    def __init__(self):
        self.__J_ingreso = {'J_usuario': 'admin', 'F_contraseña': 'admin1'}

    def __pedir_datos(self):
        J_usuario = input("Ingrese el usuario de administrador: ")
        F_contraseña = input("Ingrese la contraseña de administrador: ")
        return J_usuario, F_contraseña

    def acceso(self):
        J_usuario, F_contraseña = self.__pedir_datos()

        if J_usuario == self.__J_ingreso['J_usuario'] and F_contraseña == self.__J_ingreso['F_contraseña']:
            print("\n✅ Acceso de administrador concedido ✅\n")
            return True
        else:
            print("\n❌ Usuario o contraseña de administrador incorrectos ❌\n")
            return False

class Animal:
    def __init__(self, J_especie, F_edad, J_tamano, F_peso, J_altura, F_fecha_entrada, J_genero, J_alimento, F_horario_comida, F_vacunas, F_enfermedades):
        self.J_especie = J_especie
        self.F_edad = F_edad
        self.J_tamano = J_tamano
        self.F_peso = F_peso
        self.J_altura = J_altura
        self.F_fecha_entrada = F_fecha_entrada
        self.J_genero = J_genero
        self.J_alimento = J_alimento
        self.F_horario_comida = F_horario_comida
        self.F_vacunas = F_vacunas
        self.F_enfermedades = F_enfermedades

class AnimalTerrestre(Animal):
    def __init__(self, *args, habitat, patas):
        super().__init__(*args)
        self.habitat = habitat
        self.patas = patas

class AnimalAcuatico(Animal):
    def __init__(self, *args, tipo_agua, profundidad_max):
        super().__init__(*args)
        self.tipo_agua = tipo_agua
        self.profundidad_max = profundidad_max

class AnimalVolador(Animal):
    def __init__(self, *args, envergadura, altitud_max):
        super().__init__(*args)
        self.envergadura = envergadura
        self.altitud_max = altitud_max

class Zoo:
    def __init__(self, archivo_animales='animales.csv'):
        self.archivo_animales = archivo_animales

        try:
            self.df_animales = pd.read_csv(self.archivo_animales)
        except FileNotFoundError:
            self.df_animales = pd.DataFrame(columns=['Especie', 'Edad', 'Tamano', 'Peso', 'Altura', 'FechaEntrada', 'Genero', 'Alimento', 'HorarioComida', 'Vacunas', 'Enfermedades', 'Tipo', 'Atributos'])
            self.df_animales.to_csv(self.archivo_animales, index=False)

        self.menu()

    def agregar_animal(self):
        print("\nSeleccione el tipo de animal:")
        print("1. Terrestre")
        print("2. Acuático")
        print("3. Volador")
        tipo_animal = input("Seleccione una opción (1/2/3): ")

        J_especie = input("Ingrese la especie del animal: ")
        F_edad = int(input("Ingrese la edad del animal: "))
        J_tamano = input("Ingrese el tamaño del animal (Grande/Mediano/Pequeño): ")
        F_peso = float(input("Ingrese el peso del animal (en kg): "))
        J_altura = float(input("Ingrese la altura del animal (en metros): "))
        F_fecha_entrada = input("Ingrese la fecha de entrada al zoo (YYYY-MM-DD): ")
        J_genero = input("Ingrese el género del animal (Macho/Hembra): ")
        J_alimento = input("Ingrese el tipo de alimento del animal: ")
        F_horario_comida = input("Ingrese el horario de comida del animal (HH:MM, HH:MM): ")
        F_vacunas = input("Ingrese las vacunas del animal (separelas con comas): ")
        F_enfermedades = input("Ingrese las enfermedades del animal (separelas por comas): ")

        if tipo_animal == '1':  # Terrestre
            habitat = input("Ingrese el hábitat del animal: ")
            patas = int(input("Ingrese la cantidad de patas del animal: "))
            animal = AnimalTerrestre(J_especie, F_edad, J_tamano, F_peso, J_altura, F_fecha_entrada, J_genero, J_alimento, F_horario_comida, F_vacunas, F_enfermedades, habitat=habitat, patas=patas)
            atributos = f"Hábitat: {habitat}, Patas: {patas}"
            tipo = "Terrestre"

        elif tipo_animal == '2':  # Acuático
            tipo_agua = input("¿El animal vive en agua dulce o salada?: ")
            profundidad_max = float(input("Ingrese la profundidad máxima donde puede nadar (en metros): "))
            animal = AnimalAcuatico(J_especie, F_edad, J_tamano, F_peso, J_altura, F_fecha_entrada, J_genero, J_alimento, F_horario_comida, F_vacunas, F_enfermedades, tipo_agua=tipo_agua, profundidad_max=profundidad_max)
            atributos = f"Tipo de Agua: {tipo_agua}, Profundidad Máxima: {profundidad_max} m"
            tipo = "Acuático"

        elif tipo_animal == '3':  # Volador
            envergadura = float(input("Ingrese la envergadura del animal (en metros): "))
            altitud_max = float(input("Ingrese la altitud máxima que puede volar (en metros): "))
            animal = AnimalVolador(J_especie, F_edad, J_tamano, F_peso, J_altura, F_fecha_entrada, J_genero, J_alimento, F_horario_comida, F_vacunas, F_enfermedades, envergadura=envergadura, altitud_max=altitud_max)
            atributos = f"Envergadura: {envergadura} m, Altitud Máxima: {altitud_max} m"
            tipo = "Volador"

        else:
            print("Opción inválida. Intente de nuevo.")
            return self.agregar_animal()

        nuevo_animal = pd.DataFrame({
            'Especie': [animal.J_especie],
            'Edad': [animal.F_edad],
            'Tamano': [animal.J_tamano],
            'Peso': [animal.F_peso],
            'Altura': [animal.J_altura],
            'FechaEntrada': [animal.F_fecha_entrada],
            'Genero': [animal.J_genero],
            'Alimento': [animal.J_alimento],
            'HorarioComida': [animal.F_horario_comida],
            'Vacunas': [animal.F_vacunas],
            'Enfermedades': [animal.F_enfermedades],
            'Tipo': [tipo],
            'Atributos': [atributos]
        })

        self.df_animales = pd.concat([self.df_animales, nuevo_animal], ignore_index=True)
        self.df_animales.to_csv(self.archivo_animales, index=False)
        print("✅ Animal agregado correctamente ✅")

    def mostrar_animales(self):
        print("\nListado de animales en el zoológico:")
        print(self.df_animales)
        print()

    def menu(self):
        while True:
            print("\nMenu del Zoológico:")
            print("\t1. Agregar Animal")
            print("\t2. Mostrar Animales")
            print("\t3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.agregar_animal()
            elif opcion == '2':
                self.mostrar_animales()
            elif opcion == '3':
                print("👋 Gracias por usar el sistema del zoológico 👋")
                exit()
            else:
                print("Opción no válida, por favor intente de nuevo.")


while True:
    print("😊 Bienvenido al sistema de administración del zoológico 😊")
    admin_zoo = AdministradorZoo()
    if admin_zoo.acceso():
        Zoo()
    else:
        print("❌ Acceso denegado ❌")
