
import csv

'''Modos de apertura de archivos:'''

#'r':
# Modo de lectura. Este es el modo por defecto. Abre el archivo para leer su contenido. 
# Si el archivo no existe, se lanzará un error FileNotFoundError.

# 'w':
# Modo de escritura. Abre el archivo para escritura. Si el archivo ya existe, su contenido se sobrescribirá. 
# Si no existe, se creará un nuevo archivo.

# 'a':
# Modo de adición. Abre el archivo para agregar contenido al final. 
# Si el archivo no existe, se creará uno nuevo.

# 'b':
# Este modo se puede usar junto con los anteriores (por ejemplo, 'rb' o 'wb') para 
# abrir archivos en formato binario.

# '+':
# Este modo permite tanto la lectura como la escritura. Por ejemplo, 'r+' abre el 
# archivo para lectura y escritura, sin sobrescribir el contenido.

'''MOSTRAR'''

# with open('CSV/Archivos/notes.csv') as nt: #Pilas la ruta absoluta y local
#     reader1 = csv.reader(nt)
#     for fila in reader1: #Fila es como un iterador
#         print(f'Nombre:{fila[0]}  Nota 1:{fila[1]}  Nota 2:{fila[2]}  Nota 3:{fila[3]} ')


# with open('CSV/Archivos/demo.csv') as ej:
#     reader1 = csv.reader(ej)
#     for fila in reader1: #Fila es como un iterador
#         print(f'{fila[0]}  {fila[1]}  {fila[2]} ')



'''CREACIÓN Y ESCRITURA DE DATOS'''

# file = open('CSV/Archivos/file.txt', 'w')
# contenido = 'HOla Jhon'
# file.write(contenido)
# file.close()



'''CREACIÓN Y ESCRITURA DE DATOS'''

# file = open('CSV/Archivos/file.txt', 'r')

# #print(file.readline()) #Solo la primera fila
# #print(file.readlines()) #Todas las filas

# line = file.readlines()
# print(line)
# file.close()



'''LECTURA DE ARCHIVOS CSV'''

# with open('CSV/Archivos/personas.csv', 'r', newline='') as f:
#     leer = csv.reader(f, delimiter=';')
#     for i in leer:
#         print(f'1er Apellido:{i[0]}  2do Apellido:{i[1]}  Nombre:{i[2]}  Nacido en:{i[3]} ')



'''ESCRITURA DE ARCHIVOS EN CSV'''

# personas = [
#     ['Palacios','Rivas','Adan','Cdmx'],
#     ['Palacios','Rivas','Argelia','Queretaro'],
#     ['Torres','Palacios','Sandra','Tijuana'],
#     ['Torres','Palacios','Andres','Sinaloa'],
#     ]

# with open('CSV/Archivos/personas.csv', 'w', newline='') as f:
#     escribir = csv.writer(f, delimiter=';')
#     # escribir.writerow(personas) #Solo una fila
#     escribir.writerows(personas) #Todas las filas




# # CON ENCABEZADOS
# with open("CSV/Archivos/Demo.csv", "r") as my_file:
#     # pass the file object to reader()
#     file_reader = csv.reader(my_file)
#     # do this for all the rows
#     for i in file_reader:
#         # print the rows
#         print(i)


# # SIN ENCABEZADOS
# with open("CSV/Archivos/Demo.csv", "r") as my_file:
#     file_csv = csv.reader(my_file)
#     head = next(file_csv)
#     # check if the file is empty or not
#     if head is not None:
#         # Iterate over each row
#         for i in file_csv:
#             # print the rows
#             print(i)


# # Devuelve cada fila como un diccionario.
# with open("CSV/Archivos/Demo.csv", "r") as my_file:
#     # passing file object to DictReader()
#     csv_dict_reader = csv.DictReader(my_file)
#     # iterating over each row
#     for i in csv_dict_reader:
#         # print the values
#         print(i)


'''Estudio EJERCICIO DE JHON'''


archivo1 = 'CSV/Archivos/csv1.csv'
archivo2 = 'CSV/Archivos/csv2.csv'
archivo3 = 'CSV/Archivos/csv3.csv'


def csv1mostrar():
    with open(archivo1, 'r',  newline='') as csv1:
        mostrar=csv.reader(csv1, delimiter=';')
        for i in mostrar:
            print(f'CODIGO:{i[0]},NOMBRE:{i[1]},EDAD:{i[2]}')

def csv2mostrar():
    with open(archivo2, 'r',  newline='') as csv2:
        mostrar=csv.reader(csv2, delimiter=';')
        for i in mostrar:
            print(f'CODIGO:{i[0]},NOMBRE:{i[1]},EDAD:{i[2]}')

def csv3mostrar():
    with open(archivo3, 'r',  newline='') as csv3:
        mostrar=csv.reader(csv3, delimiter=';')
        for i in mostrar:
            print(f'CODIGO:{i[0]},NOMBRE:{i[1]},EDAD:{i[2]}')

def csv1():
    with open(archivo1, 'a',  newline='') as i:
        escri=csv.writer(i, delimiter=';') 
        CODIGO=input('Digite el codigo del estudiante: \nIngrese la opcion: ')  
        NOMBRE=input('Digite el nombre del estudiante: \nIngrese la opcion: ')
        EDAD=int(input('Digite la edad del estudiante: \nIngrese la opcion: '))
        escri.writerow([CODIGO,NOMBRE,EDAD])
    print('Datos almacenados con éxito\n')
    opc=input('Digite:\n\t1.Para añadir otro elemto\n\t2.Para ver el csv\n\t3.Salir: \n')
    if(opc=='1'):
            with open(archivo1, 'a',  newline='') as i:
                csv1()
    elif(opc=='2'):
        csv1mostrar()
    elif(opc=='3'):
        menu()

def csv2():
    with open(archivo2, 'r',  newline='') as csv2:
        mostrar=csv.reader(csv2, delimiter=';')
        for i in mostrar:
            print(f'CODIGO:{i[0]},NOMBRE:{i[1]},EDAD:{i[2]}')
    opc=input('Digite:\n\t1.Para ver de nuevo el csv\n\t2.Salir:\n')
    if opc=='1':
        csv2mostrar()
    elif opc=='2':
        menu()

def csv3():
        # Leer las filas del archivo CSV
    with open(archivo3, 'r', newline='') as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter=';')
        filas = list(lector)  # Convertir las filas en una lista para modificar

    # Modificar el valor
    elemento_amodificar=input('Digite el nombre a modificar: \n')
    for fila in filas:  # Iterar sobre cada fila
        if fila[1] == elemento_amodificar: 
            elemento = input('Digite el nuevo nombre:\n')
            fila[1] = elemento  # Modificar el nombre
            print('Nombre registrado')
            break  # Terminar la búsqueda después de la primera coincidencia
        else:
            print('Nombre no encontrado')
            csv3()

    # Sobrescribir el archivo CSV con los datos modificados
    with open(archivo3, 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv, delimiter=';')
        escritor.writerows(filas)  # Sobrescribir con las filas modificadas
        opc=input('Digite:\n\t1.Para ver el csv\n\t2.Salir\n')
    if opc=='1':
        csv3mostrar()
    elif opc=='2':
        menu()

def menu():
    while True:
        opc=input('Digite:\n\t1.para hacer el csv1\n\t2.para ver el csv2\n\t3.para modificar el csv3\n') 
        if(opc=='1'):
            csv1()
        elif(opc=='2'):
            csv2()
        elif(opc=='3'):
            csv3()
        else:
            print('opcion incorrecta')


while True:
    menu()






































