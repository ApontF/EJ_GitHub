#EJEMPLOS DE ENCAPSULAMIENTO: 
# ENCAPSULAMIENTO: Ocultamiento de datos del estado interno
#para proteger la integridad del objeto.
#atributos públicos (se pueden ver) y privados(no se pueden ver facilmente)



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

##class Persona():
##
##    def _init_ (self, codigo, nombre, edad):
##        self.__codigo= codigo 
##        self.__nombre= nombre   
##        self.edad= edad
##
##
##    def saludar (self):
##        print ('hola' , self.nombre)
##



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


''''''

## comentarios
##podemos acceder a un atributo privado asi:
##nombreobjeto.nombreclase_nombreatributo
#ejemplo: a.Banco_dinero     

##creación de objetos para probar el programa
#p1=Persona(1,'julian',12)
#p2=Persona(122222,'hector', 15)
#print (p1.Persona_codigo)
#print (p1.Persona_nombre)
#print (p1.edad)
#
#print (p2.Persona_codigo)
#print (p2.Persona_nombre)
#print (p2.edad)
#
#p1.nombre = 'hector julian'
#p1.saludar()



'''Ejercicio sin pandas'''

# class Banco():
#     def __init__(self):
#         print('!!!Usuario, ingrese los siguientes datos para continuar!!! ')
#         self.nombre = input('Ingrese su nombre y apellidos: ')
#         self.direccion = input('Ingrese su dirección: ')
#         self.telefono = int(input('Ingrese su numero telefonico: '))
#         self.tipocuenta = input('Ingrese tipo de cuenta: ')
#         self.__dinero = 50000.0 #float(input('ingrese dinero de apertura cuenta: '))
#         self.Menu()

        
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

#     def Menu(self):
#         while True:
#             print("\nMenu:")
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


































