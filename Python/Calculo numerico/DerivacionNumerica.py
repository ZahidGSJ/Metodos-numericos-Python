import numpy as np

valoraevaluar = np.pi/2
h = 0.0001

def f(x):
    return np.sin(x**2) + 1

def Centrado():
    # Formula centrado
    aproximacion = (f(valoraevaluar + h) - f(valoraevaluar - h)) / (2*h)
    print("=== CENTRADO ===")
    print("El valor de h es: ", h)
    print("La primera derivada evaluada en el punto es ", aproximacion, "\n")

def Progresivo():
    # Formula progresivo
    aproximacion = (f(valoraevaluar + h) - f(valoraevaluar)) / h
    print("=== PROGRESIVO ===")
    print("El valor de h es: ", h)
    print("La primera derivada evaluada en el punto es ", aproximacion, "\n")


def Regresivo():
    # Formula regresivo
    aproximacion = (f(valoraevaluar) - f(valoraevaluar - h)) / h
    print("=== REGRESIVO ===")
    print("El valor de h es: ", h)
    print("La primera derivada evaluada en el punto es ", aproximacion)

Centrado()
Progresivo()
Regresivo()