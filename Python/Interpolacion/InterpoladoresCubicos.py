from math import *

def InteporladoresCubicos(datos):
    # Entrada:
    # datos == lista de puntos en "x" y "y" en el plano ordenados por x

    # Salida:
    # a == vector de coeficientes constantes
    # b == vector de coeficientes lineales
    # c == vector de coeficientes cuadraticos
    # d == vector de coeficientes cubicos

    n = len(datos) - 1

    # Inicando los vectores aux
    A = [x[1] for x in datos]
    X = [x[0] for x in datos]
    H = [0.0 for x in range(n)]
    B = [0.0 for x in range(n + 1)]
    C = [0.0 for x in range(n + 1)]
    D = [0.0 for x in range(n + 1)]
    alpha = [0.0 for x in range(n)]
    mu = [0.0 for x in range(n + 1)]
    lo = [0.0 for x in range(n + 1)]
    z = [0.0 for x in range(n + 1)]

    # Creacion del vector 2
    for i in range(n):
        H[i] = X[i + 1] - X[i]

    # Vector n
    for i in range(1, n):
        alpha[i] = (3 / H[i] * (A[i + 1] - A[i]) - (3 / H[i - 1]) * (A[i] - A[i - 1]))

    # Dar solucion al sistema tridiagonal
    for i in range(1, n):
        lo[i] = 2 * (X[i + 1] - X[i - 1]) - H[i - 1] * mu[i - 1]
        mu[i] = H[i] / lo[i]
        z[i] = (alpha[i] - H[i - 1] * z[i - 1]) / lo[i]

    # Solucionar sistema tridiagonal
    for j in range(n - 1, -1, -1):
        C[j] = z[j] - mu[j] * C[j + 1]
        B[j] = (A[j + 1] - A[j]) / (H[j]) - H[j] * (C[j + 1] + 2 * C[j]) / 3
        D[j] = (C[j + 1] - C[j]) / (3 * H[j])

    # Retorna vectores A, B, C, D
    return A[:-1], B[:-1], C[:-1], D[:-1]

# Datos de prueba (1, 2), (2, 3), (3, 5)
DatosDePrueba = [[1, 2], [2, 3], [3, 5]]

# Llamada de la funcion
a, b, c, d = InteporladoresCubicos(DatosDePrueba)
print("Vectores de coeficientes:")
print("A =", a)
print("B =", b)
print("C =", c)
print("D =", d)

