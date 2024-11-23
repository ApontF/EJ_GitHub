'''
Haga un programa que nos permita gestionar una biblioteca digital, tenga en cuenta los siguientes datos:

Código: Código único de la biblioteca
Autor: Autor de la biblioteca
Tema: Tema de la biblioteca
Páginas: Número de páginas de la biblioteca
Cantidad: Número de libros en la biblioteca
Precio: Precio de la biblioteca
'''

import pandas as pd
import re

class Biblioteca:


    def __init__(self, archivo_libros='Archivos/libros.csv', archivo_usuarios='Archivos/usuarios.csv'):
        self.archivo_libros = archivo_libros
        self.archivo_usuarios = archivo_usuarios
        
        try:
            self.df_libros = pd.read_csv(self.archivo_libros)
        except FileNotFoundError:
            self.df_libros = pd.DataFrame(columns=['Código', 'Autor', 'Tema', 'Páginas', 'Cantidad', 'Precio'])
            self.df_libros.to_csv(self.archivo_libros, index=False)
        
        try:
            self.df_usuarios = pd.read_csv(self.archivo_usuarios)
        except FileNotFoundError:
            self.df_usuarios = pd.DataFrame(columns=['Nombre', 'Clave'])
            self.df_usuarios.to_csv(self.archivo_usuarios, index=False)
        
        self.Menu()

    def validar_codigo(self, codigo):
        """Valida que el código sea alfanumérico y tenga exactamente 6 caracteres"""
        if re.fullmatch(r'^[A-Za-z0-9]{6}$', codigo):
            return True
        else:
            print("Código inválido. Debe ser alfanumérico y tener exactamente 6 caracteres.")
            return False

    def AgregarLibro(self):
        codigo = input("Ingrese el código del libro (alfanumérico de 6 caracteres): ")
        if not self.validar_codigo(codigo):
            return  # Sale de la función si el código no es válido
        
        autor = input("Ingrese el autor: ")
        tema = input("Ingrese el tema: ")
        paginas = int(input("Ingrese el número de páginas: "))
        cantidad = int(input("Ingrese la cantidad de ejemplares: "))
        precio = float(input("Ingrese el precio: "))
        
        nuevo_libro = pd.DataFrame({
            'Código': [codigo],
            'Autor': [autor],
            'Tema': [tema],
            'Páginas': [paginas],
            'Cantidad': [cantidad],
            'Precio': [precio]
        })
        
        self.df_libros = pd.concat([self.df_libros, nuevo_libro], ignore_index=True)
        self.df_libros.to_csv(self.archivo_libros, index=False)
        print(f"Libro agregado correctamente en {self.archivo_libros}")
        print(self.df_libros)
        self.Menu()

    def EliminarLibro(self):
        codigo = input("Ingrese el código del libro que desea eliminar: ")
        if codigo in self.df_libros['Código'].values:
            self.df_libros = self.df_libros[self.df_libros['Código'] != codigo]
            self.df_libros.to_csv(self.archivo_libros, index=False)
            print("Libro eliminado correctamente.")
        else:
            print("Libro no encontrado.")
        self.Menu()

    def AgregarUsuario(self):
        nombre = input("Ingrese el nombre del usuario: ")
        clave = input("Ingrese la clave de seguridad: ")
        
        nuevo_usuario = pd.DataFrame({
            'Nombre': [nombre],
            'Clave': [clave]
        })
        
        self.df_usuarios = pd.concat([self.df_usuarios, nuevo_usuario], ignore_index=True)
        self.df_usuarios.to_csv(self.archivo_usuarios, index=False)
        print(f"Usuario agregado correctamente en {self.archivo_usuarios}")
        print(self.df_usuarios)
        self.Menu()

    def MostrarLibros(self):
        print("Lista de libros:")
        print(self.df_libros)
        self.Menu()

    def MostrarUsuarios(self):
        print("Lista de usuarios:")
        print(self.df_usuarios)
        self.Menu()

    def Menu(self):
        while True:
            print("\nMenu:")
            print("\t1. Agregar Libro")
            print("\t2. Eliminar Libro")
            print("\t3. Agregar Usuario")
            print("\t4. Mostrar Libros")
            print("\t5. Mostrar Usuarios")
            print("\t6. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.AgregarLibro()
            elif opcion == '2':
                self.EliminarLibro()
            elif opcion == '3':
                self.AgregarUsuario()
            elif opcion == '4':
                self.MostrarLibros()
            elif opcion == '5':
                self.MostrarUsuarios()
            elif opcion == '6':
                print("¡Gracias por usar el sistema de biblioteca!")
                exit()
            else:
                print("¡Opción inválida!")

# Iniciar el sistema de biblioteca
biblioteca = Biblioteca()