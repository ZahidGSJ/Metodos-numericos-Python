# Ejercicio tomado del libro de Burden, Análisis numérico apartado 10.2, ejercicio 3 inciso c

from math import cos, sin, pi, exp, sqrt
import numpy as np

# introducir valores que se evualaran de la funcion
def Fs(x1, x2, x3):
    f1 = 3*x1-cos(x2*x3)-1/2
    f2 = x1**2-81*(x2+0.1)**2+sin(x3)+1.06
    f3 = exp(-x1*x2)+20*x3+(10*pi-3)/3
    return np.matrix([[f1], [f2], [f3]])

#Matriz Jacobiana
def JInv(x1, x2, x3):
    J = np.matrix([[3, x3*sin(x2*x3), x2*sin(x2*x3)], [2*x1, -162*(x2+0.1), cos(x3)], [-x2*exp(-x1*x2), -x1*exp(-x1*x2), 20]])
    JV = np.linalg.inv(J)
    return [J, JV]

def RhapsonMulti(x1, x2, x3, P0, k, tolerancia):
    print("k \t x1 \t \t x2 \t \t x3 \t \t (x(k)-x(k-1)")
    print("{0:1d} \t {1:1.4f} \t {2:1.4f} \t {3:1.4f} \t".format(k, x1, x2, x3))

    while k < 10:
        # Calcular vector F y matriz Jacobiana
        J, JI = JInv(x1, x2, x3)
        F = Fs(x1, x2, x3)
        Y = -JI * F
        # Vector x
        X = np.matrix(P0).T + Y

        # Actualizando valores
        x1, x2, x3 = float(X[0][0]), float(X[1][0]), float(X[2][0])

        # Calculo de la magnitud del vector
        magnitud = sqrt((x1 - P0[0]) ** 2 + (x2 - P0[1]) ** 2 + (x3 - P0[2]) ** 2)

        # Redifinir P0
        P0 = [x1, x2, x3]
        k += 1
        print("{0:1d} \t {1:1.6f} \t {2:1.6f} \t {3:1.6f} \t {4:1.6f}".format(k, x1, x2, x3, magnitud))

        # Calcular magnitud del vector "Y" y aplicar la tolerancia
        if sqrt(Y[0][0] ** 2 + Y[1][0] ** 2 + Y[2][0] ** 2) < Tolerancia:
            print("Cálculo exitoso:)")
            break


#Aproximacion lineal
P0 = [0.1, 0.1, -0.1]

# Valores de aproximacion por separado
x1, x2, x3 = P0

# valor de k
k= 0

Tolerancia = 0.0000000001

# Llamada de la funcion con sus respectivos parametros
RhapsonMulti(x1, x2, x3, P0, k, Tolerancia)