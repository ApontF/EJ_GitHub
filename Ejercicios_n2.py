
'''Ejercicios IF-ELIF-ELSE-FOR-WHILE'''

'''EJ.1 Empleando el condicional IF realice el diseño de un algoritmo que solicite por pantalla los datos de unos empleados:
Nombre y Apellido, documento de identidad, sueldo. Con estos datos su programa debe saber que personas ganan superior 
al salario mínimo y mostrar al finalizar la ejecución los datos del empleado e indicar si gana o no superior al salario mínimo en Colombia. '''

# n_workeds = input('Ingrese la cantidad de empleados: ') 
# list_workeds = []
# for i in range(int(n_workeds)):
#     name = input(f"Ingrese el Nombre de la persona {i+1}: ")
#     last_name = input(f"Ingrese el Apellido de la persona {i+1}: ")
#     id = input(f"Ingrese el n° Documento de la persona {i+1}: ")
#     salary = int(input(f"Ingrese el Salario de la persona {i+1}: "))
#     person = [name, last_name, id, salary] #Se crea una lista para guardar los datos anteriores
#     list_workeds.append(person)
# for i in range(int(n_workeds)):
#     if list_workeds[i][3] >= 1300000:
#         print(f'{list_workeds[i][0]} Usted gana el minimo')
#     else:
#         print(f'{list_workeds[i][0]} Usted no gana el minimo')



'''EJ.2 Construir un programa que calcule y muestre por pantalla las  raíces de la ecuación de segundo grado de coeficientes reales. El programa debe 
diferenciar los diferentes casos que puedan surgir: la existencia de dos raíces reales distintas, de dos raíces reales iguales y de dos raíces complejas. 
Nota: se recomienda el empleo de sentencias if_else [Ecuacion cuadratica]'''

# import math as m
# from math import sqrt 
# a=float(input('digite el coeficiente de la x^2: '))
# b=float(input('digite el coeficiente de la x: '))
# c=float(input('digite el cofeciente independiente: '))
# if(pow(b,2)-4*a*c)>0:
#      x1=round((-b+sqrt(pow(b,2)-4*a*c))/2*a,3)
#      x2=round((-b-sqrt(pow(b,2)-4*a*c))/2*a,3)
#      print(f'la primera raiz es: {x1}, la segunda raiz es: {x2}')
# elif (pow(b,2)-4*a*c)==0:
#     x1=round((-b+sqrt(pow(b,2)-4*a*c))/2*a,3)
#     x2=round((-b-sqrt(pow(b,2)-4*a*c))/2*a,3)
#     print(f'la  raiz es: {x1}')
# elif (pow(b,2)-4*a*c)<0:  
#      print(f'No tiene solucion')



'''EJ.3 Escribir un programa que solicite al usuario una letra. Al ingresarla por teclado si es una vocal, muestre el mensaje “es vocal”. 
Se debe validar que el usuario ingrese sólo un carácter. Al ingresar un string de más de un carácter, informarle que no se puede procesar el dato.'''

# num = [str(i) for i in range(10)] #Para que marque si es numero
# vocals = ['a','e','i','o','u']
# while True:
#     vocal = input('Ingrese un caracter: ')
#     if len(vocal) == 1:
#         if vocal in num:
#             print('Usted digitó un número')
#             break
#         elif vocal.lower() in vocals:
#             print('Usted digitó una vocal')
#             break
#         else:
#             print('Usted no digito una vocal')
#             break
#     else:
#         print('Digite solo un caracter')



'''EJ.4 Diseñe un programa empleando las condiciones if-elif-else. Dicho algoritmo debe ser para hacer un menú de acceso a una calculadora. 
Incluya todas las operaciones aritméticas, comparar números pares e impares , sacar porcentajes, hallar valores de razones trigonométricas.'''

# print('''PERIMETRO Y AREA DE FIGURAS GEOMETRICAS
# MARQUE: 1.Suma
#         2.Resta
#         3.Multiplicación
#         4.División
#         5.Comparar
#         6.Porcentajes
#         7.Razones Trigonometicas''')
# import math as m
# while True:
#     v0 = input('Ingrese la opción con la que desea trabajar: ')
#     if v0 == '1':
#         num1 = float(input('Ingrese un número: '))
#         num2 = float(input('Ingrese otro número: '))
#         print(f'La operacion {num1} + {num2} = {num1+num2}')
#         break
#     elif v0 == '2':
#         num1 = float(input('Ingrese un número: '))
#         num2 = float(input('Ingrese otro número: '))
#         print(f'La operacion {num1} - {num2} = {num1-num2}')
#         break
#     elif v0 == '3':
#         num1 = float(input('Ingrese un número: '))
#         num2 = float(input('Ingrese otro número: '))
#         print(f'La operacion {num1} * {num2} = {num1*num2}')
#         break
#     elif v0 == '4':
#         num1 = float(input('Ingrese un número: '))
#         num2 = float(input('Ingrese otro número: '))
#         print(f'La operacion {num1} / {num2} = {num1*(1/num2)}')
#         break
#     elif v0 == '5':
#         num1 = float(input('Ingrese un número: '))
#         if num1 % 2 == 0:
#             print(f'El número {num1} es un número par')
#             break
#         else:
#             print(f'El número {num1} es un número impar')
#             break
#     elif v0 == '6':
#         num1 = float(input('Ingrese un número: '))
#         num2 = float(input('Ingrese el porcentaje que desea sacar: '))
#         print(f'El  {num2}% de {num1} es {(num2/100)*num1}')
#         break
#     elif v0 == '7':
#         p = m.pi
#         print('Considere el numero en radianes, PARA ESCRIBIR EL NUMERO PI, escriba pi')
#         num1 = input('Ingrese un número: ')
#         t = int(num1)
#         razon = input('''Ingrese la opción de la razón trigonométrica a tratar: 
#         1.sin(x)
#         2.cos(x)
#         3.tan(x)\n''')
#         if razon == '1':
#             print(f'El sin({num1}) es {round(m.sin(t),3)}')
#             break
#         elif razon == '2':
#             print(f'El cos({num1}) es {round(m.cos(t),3)}')
#             break
#         else:
#             print(f'La tan({num1}) es {round(m.tan(t),3)}')
#             break
#     else:
#         print('DIGITE UNA OPCIÓN ADECUADA')



'''EJ.5 Escriba un programa que me permita cambiar unidades de longitud. Su programa debe solicitar escoger en que unidad va ingresar la medida y en que unidad 
la quiere visualizar en pantalla, su programa debe disponer de conversiones (metro, kilómetros, centímetros, millas, yardas, pies o pulgadas). 
Ejemplo: pida una distancia en pulgadas o pies y que escriba esa distancia en centímetros. Se recuerda que una pulgada son 2,54 cm y un pie son doce pulgadas.'''

# print('''INGRESE EL TIPO DE DATO DE SU MEDIDA INICIAL:
# 1.Metro
# 2.Kilometros
# 3.Centimetros
# 4.Millas
# 5.Yardas
# 6.Pies
# 7.Pulgadas\n''')

# opciones = ['1','2','3','4','5','6','7']
# while True:
#     v0 = input('Ingrese el tipo de dato: ')
#     if v0 in opciones:
#         break
#     else:
#         print('!INGRESE UNA OPCION VALIDA!!')
 
# while True:
#     try:
#         d0 = float(input('Ingrese el valor de la medida: '))
#         break  # Si la conversión a float es exitosa, salimos del bucle
#     except ValueError:
#         print('!!INGRESE UN VALOR NUMERICO')
# print('\n')

# #Transformamos todo a metros
# if v0 == '1':
#     f0 = d0
# elif v0 == '2':
#     f0 = d0*1000
# elif v0 == '3':
#     f0 = d0/100
# elif v0 == '4':
#     f0 = d0*1609.34 
# elif v0 == '5':
#     f0 = d0*0.9144
# elif v0 == '6':
#     f0 = d0*0.3048
# elif v0 == '7':
#     f0 = d0*0.0254

# #NOTA f0 esta en metros

# print('''INGRESE LA MEDIDA A LA QUE DESEA CONVERTIR:
# 1.Metro
# 2.Kilometros
# 3.Centimetros
# 4.Millas
# 5.Yardas
# 6.Pies
# 7.Pulgadas\n''')

# while True:
#     v1 = input('Ingrese el tipo que quiere como respuesta: ')
#     if v1 in opciones:
#         break
#     else:
#         print('!INGRESE UNA OPCION VALIDA!!')
# print('\n')

# if v1 == '1':
#     f1 = f0
# elif v1 == '2':
#     f1 = f0/1000
# elif v1 == '3':
#     f1 = f0*100
# elif v1 == '4':
#     f1 = f0/1609.34 
# elif v1 == '5':
#     f1 = f0*1.09361
# elif v1 == '6':
#     f1 = f0*3.28084
# elif v1 == '7':
#     f1 = f0*39.3701

# print(f'La conversion da {f1}')



'''EJ.6 Escriba un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A, candidato B, candidato C y voto 
en blanco. Según el candidato elegido (A, B, C ó Voto blanco) se le debe imprimir el mensaje “Usted ha votado por el candidato #”. 
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.'''


# print('''INGRESE EL Candidato por el que desea votar:
# 1.Candidato A
# 2.Candidato B
# 3.Candidato C
# 4.Voto en blanco\n''')

# opciones = {
#     '1':'Candidato A','2':'Candidato B','3':'Candidato C','4':'Voto en blanco'}
# while True:
#     voto = input('Ingrese la opción a votar: ')
#     if voto in opciones:
#         break
#     else:
#         print('!!OPCIÓN ERRONEA!!')

# print(f'Usted ha votado por {opciones[voto]}') #Aquí decimos la clave



'''EJ.7 Diseñe un algoritmo que le permita crear una lista con nombres de estudiantes (N nombres), su programa debe permitir buscar si los nombres están 
contenidos en la lista, la consulta solicita nombres y verifica si están o no. Recomiendo uso for e if'''

# while True:
#     try:
#         n = int(input('Ingrese la cantidad de nombres que desea: '))
#         break  # Si la conversión a int es exitosa, salimos del bucle
#     except ValueError:
#         print('!!INGRESE UN NUMERO VALIDO!!')

# lista = []
# for i in range(n):
#     name = input(f'Ingrese el {i+1}° nombre: ')
#     lista.append(name)
# print(lista)

# search = input('Ingrese el nombre que desea consultar: ')

# if search in lista:
#     for j in range(n):
#         if search == lista[j]:
#             print(f'El nombre se encuenta en la posicion {j+1} de la lista')
# else:
#     print(f'El nombre {search} no se encuentra en la lista de estudiantes ingresada')




'''EJ.8 Escribir un programa que permita al usuario ingresar por teclado 5 números enteros, que pueden ser positivos o negativos. Al finalizar, 
mostrar la sumatoria de los números negativos y el promedio de los positivos. Recuerde que no es posible dividir por cero, por lo que es necesario 
evitar que el programa arroje un error si no se ingresaron números positivos.'''


# lista_p = []
# lista_n = []

# for i in range(5):
#     while True:
#         try:
#             num = int(input(f'Ingrese el {i+1}° número: '))
#             if num < 0:
#                 lista_n.append(num)
#                 break
#             else:
#                 lista_p.append(num)
#                 break                
#         except ValueError:
#             print('!!SOLO NUMEROS ENTEROS!!')

# print(f'La suma de los numeros negativos es: {sum(lista_n)}')
# print(f'El promedio de los numeros postivos es: {round(sum(lista_p)/len(lista_p),3)}')



'''EJ.9 Escriba un programa que pida números enteros mientras sean cada vez más grandes, al digitar un número menor que el anterior debe imprimir 
un mensaje diciendo que ese número es menor y terminar el programa usando while.'''

# a = [0]
# while True:
#     try:
#         entrada = int(input('Ingrese un numero: '))
#         break
#     except ValueError:
#         print('!!DIGITE UN NUMERO ENTERO!!')

# posicion = 0
# while entrada >= a[posicion]:
#     a.append(entrada)
#     posicion += 1
#     entrada = int(input('Ingrese un numero: '))
#     while entrada <= a[posicion]:
#         print('!!TIENE QUE DIGITAR UN NUMERO MAYOR!!')
#         break



'''EJ.10 Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuántas letras mayúsculas tiene.'''

# a = 'si'
# while True:
#     if a.lower() == 'si':
#         s = input('Ingrese una cadena: ')
#         Mayus = 0
#         for i in s:
#             if i.isupper():
#                 Mayus += 1
#         print(f'La cadena {s} tiene {Mayus} mayúsculas')
                  
#         a = input('¿Desea ingresar otra cadena? (si/no): ').lower()
#         if a == 'no':
#             break
#         elif a != 'si':
#             print('Ingrese una opción válida.')
#     else:
#         print('Ingrese una opción válida.')



'''EJ.11 Diseñe un algoritmo que permita jugar piedra, papel y tijera. Su programa debe tener dos modos: jugar contra el pc o multijugador(dos jugadores). 
Tenga en cuenta que pueden existir empates. Su programa debe solicitar el ID del jugador y permitir varias rondas hasta que no se desee jugar más, 
así mismo debe llevar un contador de puntos para al finalizar la partida decir quien es el ganador.'''

# import random

# def obtener_eleccion_jugador():
#     eleccion = input("Elige piedra, papel o tijera: ").lower()
#     while eleccion not in ["piedra", "papel", "tijera"]:
#         print("Elección no válida. Intenta de nuevo.")
#         eleccion = input("Elige piedra, papel o tijera: ").lower()
#     return eleccion

# def obtener_eleccion_computadora():
#     return random.choice(["piedra", "papel", "tijera"])

# def determinar_ganador(eleccion1, eleccion2):
#     if eleccion1 == eleccion2:
#         return "empate"
#     elif (eleccion1 == "piedra" and eleccion2 == "tijera") or \
#          (eleccion1 == "papel" and eleccion2 == "piedra") or \
#          (eleccion1 == "tijera" and eleccion2 == "papel"):
#         return "jugador1"
#     else:
#         return "jugador2"

# def jugar_ronda(jugador1, jugador2, modo):
#     if modo == "pc":
#         eleccion1 = obtener_eleccion_jugador()
#         eleccion2 = obtener_eleccion_computadora()
#         print(f"La computadora eligió: {eleccion2}")
#     else:
#         print(f"Turno de {jugador1}")
#         eleccion1 = obtener_eleccion_jugador()
#         print(f"Turno de {jugador2}")
#         eleccion2 = obtener_eleccion_jugador()
    
#     ganador = determinar_ganador(eleccion1, eleccion2)
#     if ganador == "empate":
#         print("Es un empate.")
#     elif ganador == "jugador1":
#         print(f"{jugador1} gana esta ronda.")
#     else:
#         print(f"{jugador2} gana esta ronda.")
    
#     return ganador

# def main():
#     print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
#     modo = input("Elige el modo de juego (pc/multijugador): ").lower()
#     while modo not in ["pc", "multijugador"]:
#         print("Modo no válido. Intenta de nuevo.")
#         modo = input("Elige el modo de juego (pc/multijugador): ").lower()
    
#     jugador1 = input("Ingresa el ID del Jugador 1: ")
#     jugador2 = "Computadora" if modo == "pc" else input("Ingresa el ID del Jugador 2: ")
    
#     puntos_jugador1 = 0
#     puntos_jugador2 = 0
    
#     while True:
#         ganador = jugar_ronda(jugador1, jugador2, modo)
#         if ganador == "jugador1":
#             puntos_jugador1 += 1
#         elif ganador == "jugador2":
#             puntos_jugador2 += 1
        
#         print(f"Puntuación: {jugador1} {puntos_jugador1} - {jugador2} {puntos_jugador2}")
        
#         jugar_otra = input("¿Quieres jugar otra ronda? (s/n): ").lower()
#         if jugar_otra != "s":
#             break
    
#     print("Juego terminado.")
#     if puntos_jugador1 > puntos_jugador2:
#         print(f"{jugador1} es el ganador con {puntos_jugador1} puntos.")
#     elif puntos_jugador2 > puntos_jugador1:
#         print(f"{jugador2} es el ganador con {puntos_jugador2} puntos.")
#     else:
#         print("El juego terminó en empate.")

# if __name__ == "__main__":
#     main()
































