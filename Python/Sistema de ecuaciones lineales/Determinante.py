import numpy as np

a = np.array([[-2.0, 4.0, 5.0], [6.0, 7.0, -3.0], [3.0, 0.0, 2.0]])
n = len(a)

def Determinante(a):
    detA = a[0, 0]
    for k in range(0, n-1):
        for i in range(k + 1, n):
            if a[i, k] != 0:
                la = a[i, k] / a[k, k]
                a[i, k + 1 : n] = a[i, k + 1 : n] - la * a[k, k + 1 : n]
        detA = a[k + 1, k + 1] * detA
    print("El determinante de la matriz es: ", detA)

Determinante(a)