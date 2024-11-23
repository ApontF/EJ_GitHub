'''
Haga un programa que tenga las siguientes clases:

1. Uisbarbosa
2. Vigilancia
3. Administrativos
4. Auxiliares  

En estas se pediran los siguientes atributos:
Nombre, Documento, Fecha de nacimiento, Profesion, Turno, Dependencia, Función, Horas trabajadas, Lugar, Salario

Dependiendo de cada clase use herencia
'''

import datetime
def edad_persona(fecha):
    d=datetime.datetime.strptime(fecha,'%d/%m/%Y')
    hoy=datetime.datetime.now()
    a=hoy.year-d.year
    if hoy.month<d.month or (hoy.month==d.month and hoy.day<d.day):
        a=a-1
    return a   

class Uisbarbosa():
    def __init__(self):
        self.nombre=input('Ingrese su nombre: ')
        self.documento=input('Ingrese su documento: ')
        self.naci=input('Ingrese su fecha de nacimiento (DD/MM/AAAA): ')
        self.edad=edad_persona(self.naci)
        self.profe=input('Ingrese su profesion: ')
        self.ht=10

    def imprimir(self):
        print ('Su nombre es ', self.nombre, ', y su edad es ', self.edad, ' años.\nSu documento es ', self.documento, ' , su fecha de nacimiento es ', self.naci, ' , su profesion es ', self.profe,' y sus horas trabajadas son ',self.ht)
        
class Vigilancia(Uisbarbosa):
    def __init__(self):
        super().__init__()
        self.turno=input('Ingrese su turno: ')
        self.lugar=input('Ingrese su lugar: ')
        self.ht=float(input('Ingrese su horas trabajadas: '))

    def sueldo(self):
        self.sal=self.ht*50000
        print('Su salario es de: ', self.sal)

    def imprimir(self):
        print('Su nombre es ', self.nombre, ', ', 'Edad ', self.edad, ' años\nSu documento es ', self.documento, ' , su fecha de nacimiento es ', self.naci, ' \nSu profesion es ', self.profe,'  , su turno es ', self.turno, ' , su lugar es ', self.lugar, '  ,sus horas trabajadas son ',self.ht,' y su salario es de ', self.sal)

class Administrativos(Uisbarbosa):
    def __init__(self):
        super().__init__()
        self.dep=input('Ingrese su dependencia: ')
        self.ht=float(input('Ingrese su horas trabajadas: '))

    def sueldo(self):
        self.sal=self.ht*75000
        print('Su salario es de: ', self.sal)

    def funciones(self):
        self.funcion=input('Ingrese su función: ')
        print('Su función es: ', self.funcion)

    def imprimir(self):
            print('Su nombre es ', self.nombre, ', ', 'Edad ', self.edad, ' años\nSu documento es ', self.documento, ' , su fecha de nacimiento es ', self.naci, ' \nSu profesion es ', self.profe,'  , su dependencia es ', self.dep,'  ,sus horas trabajadas son ',self.ht,' y su salario es de ', self.sal)

class Auxiliares(Vigilancia):
    def __init__(self):
        super().__init__()
        
    def funciones(self):
        self.funcion=input('Ingrese su función: ')
        print('Su función es: ', self.funcion)

while True:
    a = Uisbarbosa()

































