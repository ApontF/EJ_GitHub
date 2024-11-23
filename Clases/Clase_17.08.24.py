#Clase 07/08/2024

import math as m #Para el alias
#from math import pi #Sirve para solo importar esa función

# import math
##radio = float(input("Ingrese el radio del círculo: "))
##area = round(m.pi * radio**2,3)
##perimetro = round(2 * m.pi * radio,3)
##circunferencia = round(2 * m.pi * radio)
##print(f'La circunferencia es {circunferencia}, el area es {area}, el radio es {radio} y el perimetro es {perimetro}')


##a = int(input('Ingerese un número entero: '))
##aa = int(input('Ingerese un número sobre la cual elevar el número: '))
##print(pow(a,aa))


#TUPLAS
## Las tuplas !NO SON EDITABLES¡
l = ('Felipe',2024,'Circuitos',2.7) #Tener en cuenta que para mostrar es solo []
print(l)
for i in l: #Recorrer la tupla
 print(i)
t = ('Hola', 27, (1.4,'Jeider',56))
print(t[2][0]) # 27 in t, para evrificar si esta en la tupla
#Cambiar un dato de las tuplas
a, b, c,d = l
d = 5.0
l = a, b, c, d
print(l)


#LISTAS
##l1 = ['Felipe',2024,'Circuitos',2.7]
##l2 = [9,-5,67,-3,2,21]
##l1.append('Daniel') #Agrega al final
##l1.insert(1, 'Richard') #Inserta en esa posición
##l1.remove(2024) #Remueve el elemento
##l1.pop(2) #Remueve el elemento y lo muestra
##l2.sort() #Organiza los números
##lista = [0, 1, 2, 3, 4]
##lista2 = [5, 6, 7]
##lista3 = ['a', 'o']
##li = []
##li.append(lista)
##li.append(lista2)
##li.append(lista3)
##for i in li:
## print(i)


#DICCIONARIO
di = {2024:'Felipe', 4.8:'Programación II'}
di[12.44] = 'ya casi' #Así se agrega un elemento al diccionario
