import math
def f(y, t):
    #EDO a calcular
    return 2*y*t

def sp(t):
    #Solucion particular para evaluar el error
    return math.exp(t*t - 1)

def RK3(y, t, h):
    # Metodo Runge Kutta orden 3
    k1 = h*f(y, t)
    k2 = h*f(y + k1, t + h)
    return y + (0.5 * (k1 + k2))

def main():
    h=0.1 # Paso
    y0 = 1 # valor iniciar
    t0 = 1 # valor de x para y0
    tf=1.5 # abcisa del valor buscado
    t = t0
    y = y0
    while (t<= tf): # incrementa hasta llegar al valor buscado
        y = RK3(y, t, h)
        t += h # incrementa un paso
    yp = sp(tf) # valor exacto
    err = (yp - y) / yp # error
    print("y(%s)=%s y2(%s)=%s error=%s" %(tf, y, tf, yp, err))

main()