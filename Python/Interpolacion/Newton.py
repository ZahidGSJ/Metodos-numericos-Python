from pprint import pprint
def Newton(dat):
    # Implementación del interpolador de Newton
    # Entradas:
    # dat -- lista de puntos (x, y) en el plano
    #
    # Salidas:
    # F -- tabla de diferencias divididas
    # P -- función de interpolación

    n = len(dat)
    F = [[0 for x in dat] for x in dat] # crear tabla nula

    for i, p in enumerate(dat): # condiciones iniciales
        F[i][0] = p[1]

    for i in range(1, n): # tabla de diferencias divididas
        for j in range(1, i+1):
            F[i][j] = (F[i][j-1]-F[i-1][j-1])/(dat[i][0]-dat[i-j][0])

    def L(k, x):
        # Implementación funciones L_k(x)
        out = 1
        for i, p in enumerate(dat):
            if i <= k:
                out *= (x - p[0])
        return out

    def P(x):
        #Implementación polinomio P(x)
        newt = 0
        for i in range(1, n):
            newt += F[i][i]*L(i-1, x)
        return newt + F[0][0]
    return F, P

datost = [(-1, 3), (0, -4), (1, 5), (2, -6)]
T, P = Newton(datost)
print("Tabla de diferencias divididas:")
pprint(T)
print("Evaluar el polinomio en x = 0:")
print(P(0))

datosf = [(2, 1/2), (11/4, 4/11), (4, 1/4)]
T, P = Newton(datosf)
print("Tabla de diferencias divididas:")
pprint(T)
print("Evaluar el polinomio en x = 3:")
print(P(3))
