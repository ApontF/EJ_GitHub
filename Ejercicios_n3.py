
'''1. Diseñe una función llamada area_perimtero_rectangulo(base, altura) que devuelva el perimetro y área del 
rectangulo a partir de una base y una altura.'''

# def area_perimtero_rectangulo(base, altura):
#     perimetro = 2*(base+altura)
#     area = base*altura
#     print(f'El area es {area} y el perimetro es {perimetro}')

# def menu():
#     while True:
#         op = input('Marque: 1. Seguir\n\t2. Salir\n')
#         if op == '1':
#             # Para cerrar el ciclo
#             return 1
#         elif op == '2':
#             exit()
#         else:
#             print("!!!Ingrese valores adecuados!!!")
            
# while True:
#     a = input('Ingrese la base del rectangulo: ')
#     b = input('Ingrese la altura del rectangulo: ')
#     try:
#         a = float(a)
#         b = float(b)
#         area_perimtero_rectangulo(a, b)
#     except ValueError:
#         print('!!!Ingrese valores numericos!!!')
#         continue

#     # Para cerrar el ciclo
#     if menu() == 1:
#         pass
#     else:
#         exit()
        
       
'''2. Diseñe una función llamada area_perimetro_circulo(radio) que devuelva el perimetro y área de un círculo a partir de un radio.'''
    
# import math as mt
# def area_perimetro_circulo(radio):
#     perimetro = 2*mt.pi*radio
#     area = mt.pi*radio**2
#     print(f'El area es {round(area,3)} y el perimetro es {round(perimetro,3)}')

# def menu():
#     while True:
#         op = input('Marque: 1. Seguir\n\t2. Salir\n')
#         if op == '1':
#             # Para cerrar el ciclo
#             return 1
#         elif op == '2':
#             exit()
#         else:
#             print("!!!Ingrese valores adecuados!!!")
            
# while True:
#     a = input('Ingrese el radio del circulo: ')
#     try:
#         a = float(a)
#         area_perimetro_circulo(a)
#     except ValueError:
#         print('!!!Ingrese valores numericos!!!')
#         continue

#     # Para cerrar el ciclo
#     if menu() == 1:
#         pass
#     else:
#         exit()  


'''3. Diseñe una función hallar_mayor_menor(a,b) que tome como argumento dos números y devuelva el mayor y menor de ellos.'''

# def hallar_mayor_menor():
#     numeros = []
#     for i in range(2):
#         num = input('Ingrese un número: ')
#         numeros.append(num)
#     print(f'El número mayor es: {max(numeros)}')

# def menu():
#     while True:
#         op = input('Marque: 1. Seguir\n\t2. Salir\n')
#         if op == '1':
#             # Para cerrar el ciclo
#             return 1
#         elif op == '2':
#             exit()
#         else:
#             print("!!!Ingrese valores adecuados!!!")

# while True:   
#     hallar_mayor_menor()
#     menu()




'''4. Definir una función inversa() que calcule la inversión de una cadena. #Por ejemplo print 
palabra_inversa('universidad industrial de santander') su programa entrega 'rednatnas ed lairtsudni dadisrevinu'''

# def inversa():
#     palabra = input('Ingrese un texto: ')
#     pala = list(palabra)
#     pala.reverse()
#     a = ''.join(pala) # Une la lista de nuevo en un string
#     print(a)

# def menu():
#     while True:
#         op = input('Marque: 1. Seguir\n\t2. Salir\n')
#         if op == '1':
#            return 1
#         elif op == '2':
#             exit()
#         else:
#             print("!!!Ingrese valores adecuados!!!")
                       
# while True:   
#     inversa()
#     menu()


'''5. Diseñe un programa que tenga varias funciones, entre estas un menú para seleccionar que operación se debe realizar. 
Elabore funciones que nos permita calcular: la suma, resta, multiplicación, división, potencia, porcentaje y raices. Según 
la operación su programa debe permitir un número N de operaciones.'''

# def sumar(a, b):
#     return a + b

# def restar(a, b):
#     return a - b

# def multiplicar(a, b):
#     return a * b

# def dividir(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Error: División por cero"

# def potencia(a, b):
#     return a ** b

# def porcentaje(a, b):
#     return (a * b) / 100

# def mostrar_menu():
#     print("Seleccione una operación:")
#     print("1. Suma")
#     print("2. Resta")
#     print("3. Multiplicación")
#     print("4. División")
#     print("5. Potencia")
#     print("6. Porcentaje")
#     print("7. Salir")

# def main():
#     while True:
#         mostrar_menu()
#         opcion = input("Ingrese el número de la operación que desea realizar: ")
        
#         if opcion == '7':
#             print("Saliendo del programa...")
#             break
        
#         if opcion in ['1', '2', '3', '4', '5', '6']:
#             a = float(input("Ingrese el primer número: "))
#             b = float(input("Ingrese el segundo número: "))
        
#         if opcion == '1':
#             print(f"Resultado: {sumar(a, b)}")
#         elif opcion == '2':
#             print(f"Resultado: {restar(a, b)}")
#         elif opcion == '3':
#             print(f"Resultado: {multiplicar(a, b)}")
#         elif opcion == '4':
#             print(f"Resultado: {dividir(a, b)}")
#         elif opcion == '5':
#             print(f"Resultado: {potencia(a, b)}")
#         elif opcion == '6':
#             print(f"Resultado: {porcentaje(a, b)}")
#         else:
#             print("Opción no válida. Intente de nuevo.")

# while True:
#     menu()



'''6. Diseñe un programa que permita establecer la relación entre dos números ingresados y se cumplan las siguientes relaciones relación(a,b). 
Si el primer número es mayor que el segundo, debe devolver "True". Si el primer número es menor que el segundo, debe devolver "False" y Si ambos números son iguales, 
debe devolver un "Empate".'''

# def relacion(a, b):
#     if a > b:
#         return "True"
#     elif a < b:
#         return "False"
#     else:
#         return "Empate"

# # Ejemplo de uso
# numero1 = float(input("Ingresa el primer número: "))
# numero2 = float(input("Ingresa el segundo número: "))

# resultado = relacion(numero1, numero2)
# print(f"La relación entre {numero1} y {numero2} es: {resultado}")

#EJERCICIO 7
# def separar(lista):
#     pares = []
#     impares = []
    
#     for numero in lista:
#         if numero % 2 == 0:
#             pares.append(numero)
#         else:
#             impares.append(numero)
    
#     pares.sort()
#     impares.sort()
    
#     return pares, impares

# # Ejemplo de uso
# lista_numeros = [3, 8, 2, 7, 5, 4, 6, 1, 9]
# pares, impares = separar(lista_numeros)

# print(f"Números pares: {pares}")
# print(f"Números impares: {impares}")



'''7. Diseñe un algoritmo que realice el proceso de ordenar una lista dada con números enteros y estos se repartan en dos listas pares e impares respectivamente. 
Cree una función Separar(lista). Utilice los comandos nombrelista.sort() para ordenar la lista y nombrelista.append()'''

# def Separar(lista):
#     pares = []
#     impares = []

#     for num in lista:
#         if num % 2 == 0:
#             pares.append(num)
#         else:
#             impares.append(num)
    
#     pares.sort()
#     impares.sort()

#     return pares, impares


# lista_numeros = [5, 2, 9, 1, 6, 8, 3]
# pares, impares = Separar(lista_numeros)

# print(f"Lista de números pares: {pares}")
# print(f"Lista de números impares: {impares}")


































