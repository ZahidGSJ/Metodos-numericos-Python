from math import *

def f(x):
    funcion = cos(x) - x**3;
    return funcion

def df(x):
    return -sin(x) - 3*pow(x, 2)

def Rhapson(x0, tolerancia, n):
    for i in range(n):
        x1 = x0 - f(x0) / df(x0)
        if(abs(x1 - x0)< tolerancia):
            print('Iteracion', i + 1, '=', x1, end=' ')
            print('Es la mejor aproximacion de la raiz')
            return
        x0 = x1
        print('Iteracion', i + 1, '=', x1)

Rhapson(pi, 0.0000001, 10)

