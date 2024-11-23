import csv

def mostrar():
    with open("CSV/Archivos/Precipitaciones.csv", "r") as J_archivo:
        J_leer = csv.reader(J_archivo)
        for i in J_leer:
            print(i)


def mayores_meses():

    F_mes = int(input('Ingrese el mes a buscar el dato menor (en número): '))
    F_valor_mayor = -2000
    with open("CSV/Archivos/Precipitaciones.csv", "r") as J_archivo:
        J_leer = csv.reader(J_archivo)
        next(J_leer)  #Sin cabezas

        for i in J_leer:

            J_columna = float(i[F_mes]) #Para hacer eso filas
            if J_columna > F_valor_mayor:
                F_valor_mayor = J_columna
    #Cambio el print
    print(f'El valor mayor del mes {F_mes} es: {F_valor_mayor}')



def menores_meses():

    F_mes = int(input('Ingrese el mes a buscar el dato menor (en número): '))
    F_valor_menor = 2000
    with open("CSV/Archivos/Precipitaciones.csv", "r") as J_archivo:
        J_leer = csv.reader(J_archivo)
        next(J_leer)  #Sin cabezas

        for i in J_leer:

            J_columna = float(i[F_mes]) #Para hacer eso filas
            if J_columna < F_valor_menor:
                F_valor_menor = J_columna

    print(f'El valor menor del mes {F_mes} es: {F_valor_menor}')


def mayores_ciudades():
    J_ciudad = input('Ingrese la ciudad para buscar el dato mayor: ')
    F_valor_mayor = -2000  
    A_condición = False  

    with open("CSV/Archivos/Precipitaciones.csv", "r") as J_archivo:
        J_leer = csv.reader(J_archivo)
        next(J_leer)  #Sin cabezas

        for i in J_leer:
            if i[0].strip().lower() == J_ciudad.strip().lower():  
                A_condición = True  
                for j in i[1:-1]:  #Sin 1 columna
                    J_valor = float(j)
                    if J_valor > F_valor_mayor:
                        F_valor_mayor = J_valor
     
    if A_condición == True:  
        print(f'El valor mayor para la ciudad {J_ciudad} es: {F_valor_mayor}')
    else:
        print(f'La ciudad {J_ciudad} no existe en el CSV.')


def menores_ciudades():

    J_ciudad = input('Ingrese la ciudad para buscar el dato mayor: ')
    F_valor_menor = 2000  
    A_condición = False  

    with open("CSV/Archivos/Precipitaciones.csv", "r") as J_archivo:
        J_leer = csv.reader(J_archivo)
        next(J_leer)  #Sin cabezas

        for i in J_leer:
            if i[0].strip().lower() == J_ciudad.strip().lower():  
                A_condición = True  
                for j in i[1:-1]:  #Sin 1 columna
                    J_valor = float(j)
                    if J_valor < F_valor_menor:
                        F_valor_menor = J_valor
     
    if A_condición == True: 

        #Cambio el print 
        print(f'El valor menor para la ciudad {J_ciudad} es: {F_valor_menor}')
    else:
        print(f'La ciudad {J_ciudad} no existe en el CSV.')


def promedio_ciudades():

    J_ciudad = input('Ingrese la ciudad para calcular el promedio de precipitaciones: ')
    F_total = 0
    A_condición = False 

    with open("CSV/Archivos/Precipitaciones.csv", "r") as J_archivo:
        J_leer = csv.reader(J_archivo)
        next(J_leer)  #Sin cabeza

        for i in J_leer:
            if i[0].strip().lower() == J_ciudad.strip().lower():
                A_condición = True  
                F_total = float(i[13])
                F_total = round(F_total/12 ,3)

    if A_condición == True:  
        print(f'El promedio anual para la ciudad {J_ciudad} es: {F_total}')
    else:
        print(f'La ciudad {J_ciudad} no existe en el CSV.')


def menu():
    while True:
        print('### BIENVENIDO AL PROGRAMA ###')
        op = input('Marque: 1. Mostrar CSV\n\t2. Datos Mayores Meses\n\t3. Datos Menores Meses\n\t4. Datos Mayores Ciudades\n\t5. Datos Menores Ciudades\n\t6. Promedio del año\n\t7. Salir\nIngrese la opcion: ')
        print(f'\n')
        if op == '1':
            print('####### MOSTRAR CSV #######')
            mostrar()
            print(f'\n')

        elif op == '2':
            print('####### DATOS MAYORES MESES #######')
            mayores_meses()
            print(f'\n')

        elif op == '3':
            print('####### DATOS MENORES MESES #######')
            menores_meses()
            print(f'\n')

        elif op == '4':
            print('####### DATOS MAYORES CIUDADES #######')
            mayores_ciudades()
            print(f'\n')

        elif op == '5':
            print('####### DATOS MENORES CIUDADES #######')
            menores_ciudades()
            print(f'\n')

        elif op == '6':
            print('####### PROMEDIO DEL AÑO #######')
            promedio_ciudades()
            print(f'\n')        
        
        elif op == '7':
            exit()

        else:
            print("!!!Ingrese una opción valida!!!")

while True:   
    menu()

































