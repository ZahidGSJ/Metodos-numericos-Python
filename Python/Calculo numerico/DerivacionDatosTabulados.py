import numpy as np
from tabulate import tabulate

valoraevaluar = 1
h = 0.5
DR = 6**2  # La derivada de la funcion

#funcion
def f(x):
    return ((2)*(x)**3)

# Progresiva (hacia adelante)
def fpf(x0, h):
    return (f(x0 + h) - f(x0)) / h
# Centrado
def fpc(x0, h):
    return (f(x0 + h) - f(x0 - h)) / (2*h)
# Hacia regresivo (Hacia atras)
def fpb(x0, h):
    return (f(x0) - f(x0 - h)) / h

def error(DR, valoraevaluar , h):
    return (abs(DR - fpf(valoraevaluar, h)) / DR) * 100 #Ecuacion porcentual

def DerivadaTab():
    print("Progresiva: ")
    print(fpb(valoraevaluar, h))
    print("Centrado: ")
    print(fpc(valoraevaluar, h))
    print("Regresiva: ")
    print(fpb(valoraevaluar, h))
    print("\n")

    print("=== Tabulacion de resultados Progresiva ===")
    Table_Porcentual = [["0.5", fpf(valoraevaluar, 0.5), error(DR, valoraevaluar, 0.5)], ["0.05", fpf(valoraevaluar, 0.05), error(DR, valoraevaluar, 0.05)], ["0.01", fpf(valoraevaluar, 0.01), error(DR, valoraevaluar, 0.01)]]
    print(tabulate(Table_Porcentual, headers= ["Tamaño h", "Derivada aproxmidad", "Error (%)"], tablefmt= "francy_grid"))

    print("\n")
    print("=== Tabulacion de resultados Centrado ===")
    Tabla_centrado = [["0.5", fpc(valoraevaluar, 0.5), error(DR, valoraevaluar, 0.5)], ["0.05", fpc(valoraevaluar, 0.05), error(DR, valoraevaluar, 0.05)], ["0.01", fpc(valoraevaluar, 0.01), error(DR, valoraevaluar, 0.01)]]
    print(tabulate(Tabla_centrado, headers= ["Tamaño h", "Derivada aproxmidad", "Error (%)"], tablefmt= "francy_grid"))

    print("\n")
    print("=== Tabulacion de resultados Regresiva ===")
    Tabla_regresiva = [["0.5", fpb(valoraevaluar, 0.5), error(DR, valoraevaluar, 0.5)], ["0.05", fpb(valoraevaluar, 0.05), error(DR, valoraevaluar, 0.05)], ["0.01", fpb(valoraevaluar, 0.01), error(DR, valoraevaluar, 0.01)]]
    print(tabulate(Tabla_regresiva, headers= ["Tamaño h", "Derivada aproxmidad", "Error (%)"], tablefmt= "francy_grid"))

DerivadaTab()

