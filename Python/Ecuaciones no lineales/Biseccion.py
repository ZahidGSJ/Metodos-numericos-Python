# Método de Biseccion
import numpy as np

def f(x):
    return np.sin(2 *x + 1) - 3 *x /5 + 1

a = 0
b = 2

def biseccion(f,a, b, N = 100, emax = 1e-10):
    x = (a + b) / 2
    for i in range(N):
        if f(x) * f(b) < 0:
            a = x
        elif f(x) * f(a) < 0:
            b = x
        else:
            break
        xold = x
        x = (a + b) / 2
        e = abs((x - xold)/x)
        if e < emax:
            break
        print(i,  x, f(x),'{:%}'.format(e))

biseccion(f, a, b)