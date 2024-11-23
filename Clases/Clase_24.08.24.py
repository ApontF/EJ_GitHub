##Clase_24.08.2024

## EJ.1 Pide, año nacimiento, mayor o menor de edad
# nombre = input('Por favor digite su nombre: ')
# fecha = int(input('Ingrese año de nacimiento: '))
# edad = 2024-fecha
# if edad >= 18:
#     print(f'{nombre} usted es Mayor de edad')
# else:
#     print(f'{nombre} usted es Menor de edad')
# print(f'{nombre} usted tiene {edad} años')


## EJ.2 Digite lados del triangulo
# tipo='a'
# while True:
#     try:
#         a = float(input('Digite un lado del angulo: '))
#         b = float(input('Digite un lado del angulo: '))
#         c = float(input('Digite un lado del angulo: '))
#         if a+b>c and a+c>b and b+c>a:
#             if a==b and a==c and b==c:
#                 tipo='equilatero'
#                 break               
#             elif a != b != c:
#                 tipo = 'escaleno'
#                 break
#             else:   
#                 tipo = 'isoceles'
#                 break
#         else:
#             print('No es un triangulo')
#             break
#     except ValueError:
#         print('Digite valores numericos')
# print(f'Los datos pertenecen a un triangulo {tipo}')


## Calcule medidad geometricas
# import math
# print('''PERIMETRO Y AREA DE FIGURAS GEOMETRICAS
# MARQUE: 1.Cuadrado
#         2.Triangulo
#         3.Circunferencia
#         4.Rombo''')
# op = input('Ingrese la opcion a trabajar: ')
# if op == '1':
#     l1 = float(input('Ingrese el lado del cuadrado: '))
#     peri = l1*4
#     area = l1*l1
#     print(f'El perimetro del cuadrado es {peri} y el area es {area}')
# elif op == '2':
#     ##REVISAR DATOS DEL TRIANGULO
#     while True:
#         try:
#             l1 = float(input('Ingrese un lado del triangulo: '))
#             l2 = float(input('Ingrese un otro del triangulo: '))
#             l3 = float(input('Ingrese un otro del triangulo: '))


#             ###### !!!!REVISAAAAAAAAR !!!!!!!!!!!
#             # while True:
#             #     try:
#             #         if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
#             #             break
#             #     except:
#             #         print('!!DIGITE VALORES QUE GENEREN UN TRIANGULO!!')


#             s = (l1+l2+l3)/2
#             area = round(math.sqrt(s*(s-l1)*(s-l2)*(s-l3)),3)
#             peri = round(l1+l2+l3,3)
#             print(f'El perimetro del triangulo es {peri} y el area es {area}')
#         except ValueError:
#             print('!!DIGITE VALORES ADECUADOS!!')
# elif op == '3':
#     l1 = float(input('Ingrese el radio del circulo: '))
#     area = round((math.pi*l1)**2,3)
#     peri = round(2*math.pi*l1,3)
#     print(f'El perimetro del circulo es {peri} y el area es {area}')
# elif op == '4':
#     ##REVISAR DATOS DEL ROMBO
#     l1 = float(input('Ingrese la diagonal mayor: '))
#     l2 = float(input('Ingrese la diagonal menor: '))
#     area = round(l1*l2,3)
#     peri = round(l1*2+l2*2,3)
#     print(f'El perimetro del circulo es {peri} y el area es {area}')   

    

## EJ:3 Cajero

# cajero = input('Ingrese una de las opciones: Retiro, Consulta, Tra, Recibos: ')
# match cajero: 
#     case 'Retiro':
#         plata = int(input('Cuanto va a retirar: '))
#         print('!Retiro exitoso!')
#     case 'Consulta':
#         print('Su saldo es: $150.000.000')
#     case 'Tra':
#         print('!Transferencia exitosa!')
#     case 'Recibo':
#         print('Agua, luz, celular, internet')


# lista = ['Bancolombia', 'Davivienda', 'BBVA', 'Bogota']
# a = str(input('Ingrese un banco: '))
# b = a in lista #Como resultado dara TRUE o FALSE
# if b == True:
#     print('Si tenemos convenio')
# else: 
#     print('No tenemos convenio actualmente')


'''WHILE'''

# l = [0]
# entrada = int(input('Ingrese un numero: '))
# posicion = 0

# while entrada >= l[posicion]:
#     l.append(entrada)
#     posicion += 1
#     entrada = int(input('Ingrese un numero: '))
#     while entrada <= l[posicion]:
#         print('Digite un numero correcto')
#         entrada = int(input('Ingrese un numero: '))


## PREGUNTAR SI SEGUIR EL PROGRAMA
# import math
# a=27
# while a == 27:
#     print('''PERIMETRO Y AREA DE FIGURAS GEOMETRICAS
#     MARQUE: 1.Cuadrado
#             2.Triangulo
#             3.Circunferencia
#             4.Rombo''')
#     op = input('Ingrese la opcion a trabajar: ')
#     if op == '1':
#         l1 = float(input('Ingrese el lado del cuadrado: '))
#         peri = l1*4
#         area = l1*l1
#         print(f'El perimetro del cuadrado es {peri} y el area es {area}')
#     elif op == '2':
#         ##REVISAR DATOS DEL TRIANGULO
#         while True:
#             try:
#                 l1 = float(input('Ingrese un lado del triangulo: '))
#                 l2 = float(input('Ingrese un otro del triangulo: '))
#                 l3 = float(input('Ingrese un otro del triangulo: '))
#                 s = (l1+l2+l3)/2
#                 area = round(math.sqrt(s*(s-l1)*(s-l2)*(s-l3)),3)
#                 peri = round(l1+l2+l3,3)
#                 print(f'El perimetro del triangulo es {peri} y el area es {area}')
#             except ValueError:
#                 print('!!DIGITE VALORES ADECUADOS!!')
#     elif op == '3':
#         l1 = float(input('Ingrese el radio del circulo: '))
#         area = round((math.pi*l1)**2,3)
#         peri = round(2*math.pi*l1,3)
#         print(f'El perimetro del circulo es {peri} y el area es {area}')
#     elif op == '4':
#         ##REVISAR DATOS DEL ROMBO
#         l1 = float(input('Ingrese la diagonal mayor: '))
#         l2 = float(input('Ingrese la diagonal menor: '))
#         area = round(l1*l2,3)
#         peri = round(l1*2+l2*2,3)
#         print(f'El perimetro del circulo es {peri} y el area es {area}')  
#     d = input('¿Desea seguir con el programa?: ')
#     if d.lower() == 'no':
#         a = 1



'''FOR'''

# for chao in range(1,10,3):
#     print(f'{chao}')

# lista = [13,15,20,22,14]
# for hoy in lista:
#     print(lista)


# a = int(input('Ingrese un numero: '))
# for contar in range(1,21):
#     print(f'{a}*{contar} = {a*contar}')
































