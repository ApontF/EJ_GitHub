

'''
Diseñe un programa aplicando POO para un concesionario de autos (automóviles, camionetas, camiones, tractocamiones), tenga en cuenta
las características en común y cree las clases necesarias, por ejemplo modelos, tipo de pintura, cantidades de unidades en inventario. 
'''

import pandas as pd

class consesionario:
    def __init__(self, hola, direccion, telefono, email):
        self.hola = hola
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        
    def __str__(self):
        return f"Nombre: {self.hola}\nDirección: {self.direccion}\nTelefono: {self.telefono}\nCorreo: {self.email}"
    
    def __repr__(self):
        return f"Nombre: {self.hola}\nDirección: {self.direccion}\nTelefono: {self.telefono}\nCorreo: {self.email}"
    