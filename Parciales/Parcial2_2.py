import pandas as pd
from datetime import datetime

class Administrador:
    def __init__(self):
        self.__J_ingreso = {'J_usuario': 'admin', 'F_contraseña': 'admin1'}

    def __pedir_datos(self):
        J_usuario = input("Ingrese el usuario de administrador: ")
        F_contraseña = input("Ingrese la contraseña de administrador: ")
        return J_usuario, F_contraseña

    def acceso(self):
        J_usuario, F_contraseña = self.__pedir_datos()

        if J_usuario == self.__J_ingreso['J_usuario'] and F_contraseña == self.__J_ingreso['F_contraseña']:
            print("\n✅ Acceso de administrador concedido ✅\n")
            return True
        else:
            print("\n❌ Usuario o contraseña de administrador incorrectos ❌\n")
            return False

class Producto:
    def __init__(self, J_codigo, F_nombre, J_precio, F_cantidad):
        self.J_codigo = J_codigo
        self.F_nombre = F_nombre
        self.J_precio = J_precio
        self.F_cantidad = F_cantidad

    def vender(self, cantidad_vendida):
        def procesar_venta():
            if cantidad_vendida <= self.F_cantidad:
                self.F_cantidad -= cantidad_vendida
                print(f"Venta realizada: {cantidad_vendida} unidades de {self.F_nombre}")
            else:
                print("😓 Stock insuficiente para la venta 😓")
        
        procesar_venta()

class Electronico(Producto):
    def __init__(self, J_codigo, F_nombre, J_precio, F_cantidad, garantia, marca):
        super().__init__(J_codigo, F_nombre, J_precio, F_cantidad)
        self.garantia = garantia
        self.marca = marca

class Alimento(Producto):
    def __init__(self, J_codigo, F_nombre, J_precio, F_cantidad, fecha_vencimiento):
        super().__init__(J_codigo, F_nombre, J_precio, F_cantidad)
        self.fecha_vencimiento = fecha_vencimiento

class Inventario:
    def __init__(self, archivo_productos='Parciales/Archivos/productos.csv'):
        self.archivo_productos = archivo_productos

        try:
            self.df_productos = pd.read_csv(self.archivo_productos)
        except FileNotFoundError:
            self.df_productos = pd.DataFrame(columns=['Codigo', 'Nombre', 'Tipo', 'Precio', 'Cantidad', 'Garantia', 'Marca', 'FechaVencimiento'])
            self.df_productos.to_csv(self.archivo_productos, index=False)

        self.menu()

    def agregar_producto(self):
        def solicitar_datos(tipo_opcion):
            if tipo_opcion == '1':
                tipo = 'Electronico'
                J_codigo = input("Ingrese el código del producto: ")
                F_nombre = input("Ingrese el nombre del producto: ")
                J_precio = float(input("Ingrese el precio del producto: "))
                F_cantidad = int(input("Ingrese la cantidad en stock: "))
                garantia = int(input("Ingrese la garantía en meses: "))
                marca = input("Ingrese la marca del producto: ")
                return Electronico(J_codigo, F_nombre, J_precio, F_cantidad, garantia, marca), tipo
            elif tipo_opcion == '2':
                tipo = 'Alimento'
                J_codigo = input("Ingrese el código del producto: ")
                F_nombre = input("Ingrese el nombre del producto: ")
                J_precio = float(input("Ingrese el precio del producto: "))
                F_cantidad = int(input("Ingrese la cantidad en stock: "))
                fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
                return Alimento(J_codigo, F_nombre, J_precio, F_cantidad, fecha_vencimiento), tipo

        print("\nSeleccione el tipo de producto:")
        print("\t1. Electrónico")
        print("\t2. Alimento")
        tipo_opcion = input("Ingrese el número correspondiente al tipo de producto: ").strip()

        if tipo_opcion in ['1', '2']:
            producto, tipo = solicitar_datos(tipo_opcion)
            nuevo_producto = pd.DataFrame({
                'Codigo': [producto.J_codigo],
                'Nombre': [producto.F_nombre],
                'Tipo': [tipo],
                'Precio': [producto.J_precio],
                'Cantidad': [producto.F_cantidad],
                'Garantia': [producto.garantia if hasattr(producto, 'garantia') else None],
                'Marca': [producto.marca if hasattr(producto, 'marca') else None],
                'FechaVencimiento': [producto.fecha_vencimiento if hasattr(producto, 'fecha_vencimiento') else None]
            })

            self.df_productos = pd.concat([self.df_productos, nuevo_producto], ignore_index=True)
            self.df_productos.to_csv(self.archivo_productos, index=False)
            print("✅ Producto agregado correctamente ✅")
        else:
            print("❌ Opción no válida. Volviendo al menú principal. ❌")
        
        self.menu()

    def mostrar_stock(self):
        def mostrar_detalles():
            for index, producto in self.df_productos.iterrows():
                if producto['Tipo'] == 'Electronico':
                    print(f"Codigo: {producto['Codigo']}, Nombre: {producto['Nombre']}, Tipo: {producto['Tipo']}, Precio: {producto['Precio']}, Cantidad: {producto['Cantidad']}, Garantía: {producto['Garantia']} meses, Marca: {producto['Marca']}")
                elif producto['Tipo'] == 'Alimento':
                    print(f"Codigo: {producto['Codigo']}, Nombre: {producto['Nombre']}, Tipo: {producto['Tipo']}, Precio: {producto['Precio']}, Cantidad: {producto['Cantidad']}, Fecha de vencimiento: {producto['FechaVencimiento']}")

        mostrar_detalles()
        self.menu()

    def realizar_venta(self):
        def procesar_venta():
            codigo_producto = input("Ingrese el código del producto a vender: ")
            F_cantidad = int(input("Ingrese la cantidad a vender: "))

            if codigo_producto in self.df_productos['Codigo'].values:
                index = self.df_productos[self.df_productos['Codigo'] == codigo_producto].index[0]
                stock_actual = self.df_productos.at[index, 'Cantidad']

                if stock_actual >= F_cantidad:
                    self.df_productos.at[index, 'Cantidad'] -= F_cantidad
                    self.df_productos.to_csv(self.archivo_productos, index=False)
                    print(f"Venta realizada: {F_cantidad} unidades de {self.df_productos.at[index, 'Nombre']}")
                else:
                    print("😓 Stock insuficiente para la venta 😓")
            else:
                print("😓 Producto no encontrado en el inventario 😓")
        
        procesar_venta()
        self.menu()

    def menu(self):
        def mostrar_opciones():
            print("\nMenu:")
            print("\t1. Agregar Producto")
            print("\t2. Mostrar Stock")
            print("\t3. Realizar Venta")
            print("\t4. Salir")

        mostrar_opciones()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            self.agregar_producto()
        elif opcion == '2':
            self.mostrar_stock()
        elif opcion == '3':
            self.realizar_venta()
        elif opcion == '4':
            print("👋 Gracias por usar el sistema de inventario 👋")
            exit()
        else:
            print("Opción no válida, por favor intente de nuevo.")

while True:
    print("\n😊 Bienvenido al sistema de inventario de TIENDA SMART 😊\n")
    admin = Administrador()
    if admin.acceso():
        Inventario()
    else:
        print("❌ Acceso denegado ❌")


