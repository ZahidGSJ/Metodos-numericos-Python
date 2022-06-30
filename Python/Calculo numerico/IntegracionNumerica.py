import numpy as np

# Funcion
def f(x):
    return x**2 - 4*x

def Integracion(a, b, N):
    # Intervalos
    a = 0
    b = 4

    N = 4
    x = np.linspace(a, b, N)
    # Distancia entre cada dato
    dx = (b - a) / (N - 1)
    y = f(x)

    # Regla del trapecio
    resultado = dx*(y[0]+2*np.sum(y[1:-1]) + y[N-1])/2
    print(resultado)
    print("El area es de: ", abs(resultado))

Integracion()