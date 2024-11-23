'''CLASE FIJA'''

# class Persona():
    
#     nombre = 'Felipe'
#     apellido = 'Aponte'
#     trabajo = 'Estudiante'
    
#     def mostrar(self):
#         print(f'Su nombre es {self.nombre} con apellido {self.apellido} y su trabajon es {self.trabajo}')

#     def si(self):
#         print('I am the monda')

# a = Persona()
# a.mostrar()
# a.si()
# print(a.nombre)




'''CLASE: A LOS OBJETOS ASIGNELE NOMBRE Y NOTA'''

# class Alumno:
#     def __init__(self):
#         self.nombre = input('Ingrese nombre: ')
#         self.nota = int(input('Ingrese nota: '))
#         self.menu()

#     def imprimir(self):
#         print("Nombre:", self.nombre)
#         print("Nota:", self.nota)


#     def resultado(self):
#         if self.nota < 5:
#             print("El alumno ha suspendido")
#         else:
#             print("El alumno ha aprobado")

#     def menu(self):
#         self.imprimir()
#         self.resultado()

# # Crear una instancia de Alumno
# a = Alumno()




'''CLASE CALCULADORA'''

# # Código usando el constructor: 
# while True:
#     try:
#         class Calculadora:

#             def __init__(self): #Metodo constructor
#                 self.valor1=int(input("Ingrese el primer valor: "))
#                 self.valor2=int(input("Ingrese el segundo valor: "))
#                 self.menu()

#             def suma(self):
#                 suma=self.valor1+self.valor2
#                 print("El resultado de la suma de los valores es: ",suma)

#             def resta(self):
#                 resta=self.valor1-self.valor2
#                 print("El resultado de la resta de los valores es: ",resta)

#             def multiplicacion(self):
#                 pro=self.valor1*self.valor2
#                 print("El resultado de la multiplicación de los valores es: ",pro)

#             def division(self):
#                 div=self.valor1/self.valor2
#                 print("El resultado de la división de los valores es: ",div)

#             def imprimir(self):
#                 print("Los valores son: ")
#                 print("Valor 1: ",self.valor1)
#                 print("Valor 2: ",self.valor2)

#             def menu(self):
#                 op = input('Digite:\n\t1.Suma\n\t2.Resta\n\t3.Multiplicación\n\t4.Division\n\t5.Imprimir\n\t6.Salir\nIngrese la opción: ')
#                 if op == '1':
#                     self.suma()
#                 elif op == '2':
#                     self.resta()
#                 elif op == '3':
#                     self.multiplicacion()
#                 elif op == '4':
#                     self.division()
#                 elif op == '5':
#                     self.imprimir()
#                 elif op == '6':
#                     exit()
#         while True:
#             calcular = Calculadora()
#     except ValueError:
#         print('!!!DIGITE BIEN ESA VERGA!!!')




'''Ejercicio de clase'''
#Realizar un programa que conste de una clase llamada Alumno
#que tenga como atributos el nombre, apellidos, código y la nota del alumno.
#Definir los métodos para inicializar sus atributos, imprimirlos y 
#mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
    def __init__(self):
        self.nombre = 'Felipe'
        self.apellido = 'Aponte'
        self.codigo = '2235070'
        self.nota = 5

    def aprobado(self):
        if self.nota > 3:           
            print("Su nota es: ",self.nota)
            print('Usted ha aprobado')

    def imprimir(self):
        print("Los valores son: ")
        print("Su nombre es: ",self.nombre)
        print("Su apellido es: ",self.apellido)
        print("Su codigo es: ",self.codigo)

a = Alumno()
a.imprimir()
a.aprobado()


































