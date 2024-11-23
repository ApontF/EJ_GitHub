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



''' PARTE TRES HERENCIA '''

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



































