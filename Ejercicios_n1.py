'''EJERCICIOS DE APLICACIONES'''

'''#1. Diseñe un programa en Python donde por pantalla se solicite: el nombre, apellido, edad, dirección, número de teléfono y genero. 
Al finalizar el ingreso de datos deben aparecer todos en pantalla. '''

# name = input('Por favor ingrese su nombre: ')
# last_name = input('Por favor ingrese su apellido: ')
# age = input('Por favor ingrese su edad: ')
# address = input('Por favor ingrese su direccion: ')
# number_phone = input('Por favor ingrese su telefono: ')
# gender = input('Por favor ingrese su genero: ')
# print(f'{'Su nombre es '}{name}{', su apellido es '}{last_name}{',su edad es '}{age}{', su direccion es '}{address}{', su numero de telefono es '}{number_phone}{'y su genero es'}{gender}')



'''#2. Diseñe un programa empleando Python donde pueda realizar las operaciones básicas matemáticas (suma, resta, multiplicación, división, 
raices, potencia y porcentajes). Su programa debe mostrar todas las operaciones y a medida que va mostrando en pantalla los resultados debe solicitar los 
siguientes datos sucesivamente. '''

# print('SUMA')
# a = float(input('Por favor digite un numero: '))
# b = float(input('Por favor digite otro numero: '))
# print(f'la suma es {a+b}')
# print('RESTA')
# c = float(input('Por favor digite un numero: '))
# d = float(input('Por favor digite otro numero: '))
# print(f'la resta es {c-d}')
# print('MULTIPLICACIoN')
# e = float(input('Por favor digite un numero: '))
# f = float(input('Por favor digite otro numero: '))
# print(f'la multiplicacion es {e*f}')
# print('RAICES')
# g = float(input('Por favor digite un numero: '))
# h = float(input('Por favor digite otro numero: '))
# print(f'la raiz {h} de {g} es {round(g**(1/h))}')
# print('POTENCIA')
# i = float(input('Por favor digite un numero: '))
# j = float(input('Por favor digite otro numero: '))
# print(f'la potencia de {i} elevado a {j} es {i**j}')
# print('PORCENTAJES')
# k = float(input('Por favor digite un numero: '))
# l = float(input('Por favor digite otro numero: '))
# print(f'El {k}% de {l} es {(k*l)/100}')



'''#3. Escriba un programa en Python donde cree tres variables y por pantalla solicite los números. Al finalizar el cargue de datos se 
debe calcular la media aritmética e imprimirla en pantalla.'''

# import math
# a = float(input('Por favor ingrese un numero: '))
# b = float(input('Por favor ingrese otro numero: '))
# c = float(input('Por favor ingrese otro numero: '))
# print(f'{'La media arimetica de los numeros '}{a}{' '}{b}{' y '}{c}{' es: '}{(a+b+c)/3}')



'''#4. Escriba un programa en Python que pida el peso (en kilogramos) y la altura (en metros) de una persona y que calcule su índice de masa corporal (imc). 
imc se calcula con la fórmula imc = peso / altura2'''

# weight = float(input('Por favor digite su peso en kg: '))
# height = float(input('Por favor digite su altura en metros: ')) 
# imc = weight/(height**2)
# print('El IMC suyo es de :', round(imc,3))



'''#5. Escriba un programa que pida una temperatura en grados Fahrenheit y que escriba esa temperatura en grados Celsius. La relación entre grados Celsius (C) 
y grados Fahrenheit (F) es la siguiente: C = (F - 32) / 1,8'''

# temp = float(input('Escriba la temperatura en grados Fahrenheir: '))
# print('La temperatura en grados Celsius es: ', round((temp-32)/1.8,3),'C')


'''#6. Escriba un programa que pida una temperatura en grados Fahrenheit y que escriba esa temperatura en grados Kelvin'''

# temp = float(input('Escriba la temperatura en grados Fahrenheir: '))
# c = round((temp-32)/1.8,3)
# print('La temperatura en Kelvin es: ',c+273.15,'K')



'''#7. Escriba un programa que pida una temperatura en grados Kelvin y que escriba esa temperatura en grados Celsius'''

# temp = float(input('Escriba la temperatura en Kelvin: '))
# print('La temperatura en grados Celsius es: ', round(temp-273.15,3),'K')



'''#8. Escriba un programa que pida una cantidad de segundos y que escriba cuántas horas, minutos y segundos son''' 

# # NOTA // dice el resultado de la division y % lo que sobra de la division
# total_seconds = float(input('Escriba los segundos a convertir: '))
# hours = total_seconds // 3600
# remaining_secods = total_seconds % 3600 
# minutes = remaining_secods // 60
# remaining_secods1 = remaining_secods % 60
# seconds = remaining_secods1
# print(f'Las horas son {hours}, los minutos son {minutes} y los segundos {seconds}')



'''#9. Elabore un programa que sirva para hallar el perimetro y área de  un triangulo rectángulo. Solicite todos los datos 
necesarios por pantalla y el usuario los debe ingresar. Al finalizar el programa debe imprimir la información de los mismos.'''

# import math
# cateto_a = float(input("Ingrese la longitud del primer cateto (a): "))
# cateto_b = float(input("Ingrese la longitud del segundo cateto (b): "))
# hipotenusa = round(math.sqrt(cateto_a**2 + cateto_b**2))
# area = (cateto_a * cateto_b) / 2
# perimetro = cateto_a + cateto_b + hipotenusa
# print(f'El cateto a es {cateto_a}, el cateto b es {cateto_b}, la hipotenusa es {hipotenusa}, el area es {area} y el perimetro es {perimetro}')



'''#10. Elabore un programa que sirva para hallar el perimetro y área de  un circulo. Solicite todos los datos necesarios por pantalla y el usuario los debe ingresar. 
Al finalizar el programa debe imprimir la información de los mismos. '''

# import math
# radio = float(input("Ingrese el radio del circulo: "))
# area = round(math.pi * radio**2,3)
# perimetro = round(2 * math.pi * radio,3)
# circunferencia = round(2 * math.pi * radio)
# print(f'La circunferencia es {circunferencia}, el area es {area}, el  area es {area}, el radio es {radio} y el perimetro es {perimetro}')










