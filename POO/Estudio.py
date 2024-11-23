class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Clase derivada
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.salario = salario

    def mostrar_salario(self):
        print(f"{self.nombre} gana {self.salario} al año.")


empleado1 = Empleado("Ana", 28, 50000)
empleado1.saludar()
empleado1.mostrar_salario()


''' POLIMORFISMO '''


''' PARTE UNO '''
# #POLIMORFISMO con método

# class Pepino():
#     def tipo(self):
#         print('vegetal')

#     def color(self):
#         print('verde')

# class Banano():
#     def tipo(self):
#         print('fruta')

#     def color(self):
#         print('amarillo')

# a = Pepino()
# b = Banano()
# a.tipo()
# b.tipo()




''' PARTE DOS POLIMORFISMO'''

# import math

# class Triangulo():
#     def __init__(self):
#         self.l1 = float(input('Ingrese el lado 1: '))
#         self.l2 = float(input('Ingrese el lado 2: '))
#         self.l3 = float(input('Ingrese el lado 3: '))

#     def Peri(self):
#         print(f'El perimetro de la figura es: {self.l1 + self.l2 + self.l3}')

#     def Area(self):
#         s = (self.l1 + self.l2 + self.l3) / 2
#         area = (s * (s - self.l1) * (s - self.l2) * (s - self.l3)) ** 0.5
#         print(f'El area del triangulo es: {area}')

# class Rectangulo():
#     def __init__(self):
#         self.l1 = float(input('Ingrese la base de la figura: '))
#         self.l2 = float(input('Ingrese la altura de la figura: '))

#     def Peri(self):
#         print(f'El perimetro de la figura es: {2 * self.l1 + 2 * self.l2}')

#     def Area(self):
#         area = self.l1 * self.l2
#         print(f'El area del rectangulo es: {area}')

# class Circulo():
#     def __init__(self):
#         self.l1 = float(input('Ingrese el radio del circulo: '))

#     def Peri(self):
#         print(f'El perimetro de la figura es: {2 * math.pi * self.l1}')

#     def Area(self):
#         area = math.pi * self.l1 ** 2
#         print(f'El area del circulo es: {area}')

# # Ejemplo de uso:
# # triangulo = Triangulo()
# # triangulo.Peri()
# # triangulo.Area()

# # rectangulo = Rectangulo()
# # rectangulo.Peri()
# # rectangulo.Area()

# # circulo = Circulo()
# # circulo.Peri()
# # circulo.Area()



''' HERENCIA '''

# class Persona():

#     def __init__(self):
#         self.nombre=input('Ingrese su nombre: ')
#         self.edad=int(input('Ingrese su edad: '))
#         self.ht=10
#         self.imprimir()
        
#     def imprimir(self):
#         print(f'Su nombre es {self.nombre}, edad {self.edad} años y tiene {self.ht} horas trabajadas ')

# # Aquí se esta heredando de persona     
# class Sueldo(Persona):
#     def __init__(self):
#         super().__init__()#heredo atributos
#         self.ht=float(input('Horas trabajadas: '))

#     def pago(self):
#         sueldot=self.ht*79000
#         print(sueldot)
        
# # Aquí se esta heredando de persona y de sueldo
# class Vida(Sueldo):
#     def __init__(self):
#         super().__init__()
#         self.actividad=input('Describa que actividad fisica realiza: ')

#     def imprimir2(self):
#         print(self.actividad)

# # Aquí no hay herencias  
# class Persona1():
#     def __init__(self):
#         self.nombre=input('Ingrese su nombre: ')
#         self.edad=int(input('Ingrese su edad: '))

#     def imprimir(self):
#         print ('su nombre es ', self.nombre, ' ', 'edad ', self.edad, ' años')


# a = Persona()
# a.imprimir()
# a1 = Sueldo()
# a1.imprimir()
# a1.pago()



# # otra forma
# # declaramos la clase persona
# class Persona2():
#    # declaramos el metodo __init__
#    def __init__(self):
#        self.nombre=input("Ingrese el nombre: ")
#        self.edad=int(input("Ingrese la edad: "))


#    # declaramos el metodo mostrar
#    def mostrar(self):
#        print("Nombre: ",self.nombre)
#        print("Edad: ",self.edad)


# # declaramos la clase persona
# class Persona3():
#    def __init__(self,nombre, edad):
#        self.nombre=nombre
#        self.edad=edad

#    def imprimir(self):
#        print('su nombre es ', self.nombre, ' ', 'edad ', self.edad, ' años')

        

''' HERENCIA '''



# # Herencia: recuerden que pueden heredar de cualquier clase
# class Persona1():
#    def __init__(self):
#        self.nombre=input('Ingrese su nombre: ')
#        self.edad=int(input('Ingrese su edad: '))

#    def imprimir(self):
#        print ('su nombre es ', self.nombre, ' ', 'edad ', self.edad, ' años')
# # forma 1 
# class Empleado(Persona1): #clase heredada de Persona1
#    def __init__(self):
#        super().__init__() #super es una función para llamar los atributos de la clase padre
#        self.sueldo=float(input('Ingrese su salario: '))

#    def imprimir(self):
#        super().imprimir()
#        print ('El salario es de: ', self.sueldo)

#    def impuestos(self):
#        if self.sueldo>1000000:
#            impuesto=self.sueldo*0.19
#            print(' señor ', self.nombre, ' debe pagar impuestos por un valor de $ ', impuesto)

#        else:
#            print (' señor ', self.nombre,'no debe pagar impuestos')


# class Persona3():
#    def __init__(self,nombre, edad):
#        self.nombre=nombre
#        self.edad=edad

#    def imprimir(self):
#        print('su nombre es ', self.nombre, ' ', 'edad ', self.edad, ' años')


# # forma 2
        
# class Empleado1(Persona3):
#    def __init__(self, nombre, edad, sueldo):
#        Persona3.__init__(self, nombre, edad)#informando que heredo
#        self.sueldo=sueldo #float(input('ingrese su salario '))

#    def impuestos (self):
#        if self.sueldo>1000000:
#            impuesto=self.sueldo*0.19
#            print('señor ', self.nombre, ' debe pagar impuesto por un valir de $ ', impuesto)
#        else:
#            print('señor ', self.nombre, 'no debe pagar impuesto')

# # HERENCIA Y POLIMORFISMO

# class Empresa():
#    def seccion(self):
#        print('Bienvenido a la empresa de programación orientada a objetos')

# class financiera(Empresa): #depende de la clase Empresa
#    def seccion(self):
#        print('Acá se lleva la contabilidad de la empresa')

# class talentohumano(Empresa):  #depende de la clase Empresa
#    def seccion(self):
#        print ('Acá se hacen las entrevistas y contrata el personal')


# emp1=Empresa()
# emp2=financiera()
# emp3=talentohumano()
# emp1.seccion()
# emp2.seccion()
# emp3.seccion()



'''Ejercicio 1 de encapsulamiento'''

# class Cliente():
#     def __init__(self):
#         self.nombre = input('nombre')
#         self.tipocuenta = input('tipo de cuenta')
#         self.__codigo = 1234 #encapsula el dato

#     def __cuenta(self):
#         print('cuenta de procesamiento')
           
#     def getcodigo(self):  #con este método busca el código encapsulado
#         return self.__codigo

# cli=Cliente()
# '''Asi puedo ver el objeto oculto'''
# print(cli._Cliente__codigo) #puede ver el código guardado ->1234
# cli._Cliente__cuenta() #->cuenta de procesamiento



'''Ejercicio 2 de encapsulamiento'''

class Persona():

   def _init_ (self, codigo, nombre, edad):
       self.__codigo= codigo 
       self.__nombre= nombre   
       self.edad= edad


   def saludar (self):
       print ('hola' , self.nombre)




'''Ejercicio 3 de encapsulamiento'''

# import pandas as pd

# class Banco():
#     def __init__(self, archivo_csv = 'Archivos/banco.csv'):
#         self.archivo_csv = archivo_csv
#         try:
#             self.df = pd.read_csv(self.archivo_csv)
#         except FileNotFoundError:
#             self.df = pd.DataFrame(columns=['Nombre', 'Dirección', 'Telefono', 'Tipo Cuenta', 'Contraseña'])
#             self.df.to_csv(self.archivo_csv, index=False)
#         self.Verificar()

#     def Agregar(self):
#         nombre = input("Ingresa su nombre: ")
#         direccion = input('Ingrese su dirección: ')
#         telefono = int(input('Ingrese su numero telefonico: '))
#         tipocuenta = input('Ingrese tipo de cuenta: ')
#         contraseña = input('Ingrese su contraseña: ')
#         self.__dinero = 50000.0 #float(input('ingrese dinero de apertura cuenta: '))

#         # Crear un DataFrame con la nueva fila
#         nuevo_dato = pd.DataFrame({'Nombre': [nombre], 'Dirección': [direccion], 'Telefono': [telefono], 'Tipo Cuenta': [tipocuenta], 'Contraseña': [contraseña]})
#         # Agregar la nueva fila al DataFrame existente
#         self.df = pd.concat([self.df, nuevo_dato], ignore_index=True)
#         # Guardar los cambios en el archivo CSV
#         self.df.to_csv(self.archivo_csv, index=False)

#         print(f"Datos guardados correctamente en {self.archivo_csv}")
#         print(self.df)
      
#     def Recibo(self):
#         print(self.nombre, self.direccion, self.telefono, self.tipocuenta, self.__dinero)
#         return (self.nombre, self.direccion, self.telefono, self.tipocuenta, self.__dinero)

#     def Retiro(self):
#         try:
#             retiro = float(input('Ingrese el valor que desea retirar: '))
#             if retiro > self.__dinero:
#                 print('!!!SALDO INSUFICIENTE!!!')
#             else:
#                 self.__dinero -= retiro
#                 print(f'!!!RETIRO EXITOSO!!! Usted ahora tiene: {self.__dinero}$ COP')
#         except ValueError:
#             print('!!!INGRESE UN VALOR VALIDO!!!')
#         self.Menu()

#     def Consignar(self, valor):

#         self.__dinero += valor


#     def Verificar(self):
#         print('!!!BIENVENIDO AL BANCO!!!')
#         nombre = input('Ingrese su nombre: ')
#         contraseña = input('Ingrese su contraseña: ')
#         if nombre in self.df['Nombre'].values and contraseña in self.df['Contraseña'].values:
#             print('!!!USTED ES UN USUARIO REGISTRADO!!!')
#             self.Menu()            
#         else:
#             print('!!!USTED NO ES UN USUARIO REGISTRADO, REGISTRESE!!!')
#             self.Agregar()


#     def Menu(self):
#         while True:
#             print("\nMenu:")
#             print("\t1. Agregar")
#             print("\t1. Recibo")
#             print("\t2. Retirar")
#             print("\t3. Consignar")
#             print("\t4. Salir")
#             op = input("Seleccione una opción: ")
#             if op == '1':
#                 self.Recibo()
#             elif op == '2':
#                 self.Retiro()
#             elif op == '3':
#                 self.Consignar()
#             elif op == '4':
#                 exit()
#             else:
#                 print("Opción no válida. Por favor, intente nuevamente.")

# while True:
#     a = Banco()


