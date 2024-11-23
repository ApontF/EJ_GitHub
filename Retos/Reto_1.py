''' 1. Cálculo de Resistencia Equivalente en Circuitos
Contexto: Un estudiante de ingeniería desea calcular la resistencia equivalente de un circuito con resistencias en paralelo y en serie. 
Se quiere construir una aplicación que permita ingresar los valores de resistencia, seleccionar el tipo de conexión (serie o paralelo) 
y visualizar la resistencia equivalente. También se debe mostrar la gráfica de la relación entre la resistencia total y el número de 
resistencias agregadas al circuito.

Objetivo: Utilizar sympy para resolver las ecuaciones de resistencia equivalente en circuitos en serie y paralelo. 
Crear una interfaz con tkinter para ingresar los valores de resistencia y seleccionar el tipo de conexión. Utilizar numpy para calcular 
la resistencia equivalente y analizar la variación al agregar más resistencias. Representar la gráfica de resistencia total vs número 
de resistencias con matplotlib. '''



import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la resistencia equivalente en serie
def resistencia_serie(resistencias):
    return np.sum(resistencias)

# Función para calcular la resistencia equivalente en paralelo
def resistencia_paralelo(resistencias):
    return 1 / np.sum(1 / np.array(resistencias))

# Función para calcular la resistencia equivalente según el tipo de conexión
def calcular_resistencia_equivalente():
    resistencias = [float(r) for r in entrada_resistencias.get().split(',')]
    tipo_conexion = tipo.get()

    if not resistencias:
        messagebox.showerror("Error", "Debe ingresar al menos una resistencia.")
        return

    if tipo_conexion == "Serie":
        resistencia_eq = resistencia_serie(resistencias)
    elif tipo_conexion == "Paralelo":
        resistencia_eq = resistencia_paralelo(resistencias)
    else:
        messagebox.showerror("Error", "Seleccione el tipo de conexión.")
        return

    etiqueta_resultado.config(text=f"Resistencia Equivalente: {resistencia_eq:.2f} Ω")
    plot_resistencia_vs_num_resistencias(resistencias, tipo_conexion)

# Función para graficar la resistencia equivalente vs número de resistencias
def plot_resistencia_vs_num_resistencias(resistencias, tipo_conexion):
    resistencias_totales = []
    for i in range(1, len(resistencias) + 1):
        if tipo_conexion == "Serie":
            res_eq = resistencia_serie(resistencias[:i])
        else:
            res_eq = resistencia_paralelo(resistencias[:i])
        resistencias_totales.append(res_eq)

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(resistencias) + 1), resistencias_totales, marker='o')
    plt.title(f"Resistencia Total vs Número de Resistencias ({tipo_conexion})")
    plt.xlabel("Número de Resistencias")
    plt.ylabel("Resistencia Equivalente (Ω)")
    plt.grid(True)
    plt.show()

# Crear la interfaz de usuario con tkinter
ventana = tk.Tk()
ventana.title("Cálculo de Resistencia Equivalente")

# Entrada de resistencias
etiqueta_resistencias = ttk.Label(ventana, text="Ingresa las resistencias (separadas por coma):")
etiqueta_resistencias.grid(column=0, row=0, padx=10, pady=10)

entrada_resistencias = ttk.Entry(ventana)
entrada_resistencias.grid(column=1, row=0, padx=10, pady=10)

# Selección de tipo de conexión (serie o paralelo)
etiqueta_tipo = ttk.Label(ventana, text="Tipo de conexión:")
etiqueta_tipo.grid(column=0, row=1, padx=10, pady=10)

tipo = tk.StringVar()
combo_tipo = ttk.Combobox(ventana, textvariable=tipo, values=["Serie", "Paralelo"], state="readonly")
combo_tipo.grid(column=1, row=1, padx=10, pady=10)

# Botón para calcular resistencia equivalente
boton_calcular = ttk.Button(ventana, text="Calcular Resistencia Equivalente", command=calcular_resistencia_equivalente)
boton_calcular.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = ttk.Label(ventana, text="Resistencia Equivalente: ")
etiqueta_resultado.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Ejecutar la ventana de la aplicación
ventana.mainloop()