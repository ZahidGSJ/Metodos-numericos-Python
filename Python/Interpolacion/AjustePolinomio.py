import numpy as np
import matplotlib.pyplot as plt


# Arrays con los valores de "x" y "y"
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])

y =np.array([432, 439, 442, 444, 446, 447, 449, 451, 453, 458, 463, 466, 468, 470, 472, 477, 479, 491, 516, 516, 521, 524,526 , 533, 541, 548, 555, 560, 563, 564])

def AjustePolinomio(x, y):
    n = len(x)

    # Sumatorias y demas operaciones correspondientes
    SumX = sum(x)
    SumY = sum(y)
    SumXX = sum(x**2)
    SumXY = sum(x*y)

    # ahora reemplazo en a_0 y a_1 y los imprimo  para visualizarlos
    a_0 = (SumXX * SumY - SumXY * SumX) / (n * SumXX - SumX ** 2)
    a_1 = (n * SumXY - SumX * SumY) / (n * SumXX - SumX ** 2)
    print(a_0, a_1)

    # Se generan valores para plotear la recta segun a_0 y a_1
    xa = np.linspace(0, 29, 100)
    ya = a_0 + a_1 * xa

    # Grafico de los puntos y la recta de ajuste
    plt.figure(1)
    plt.scatter(x, y, color='r')
    plt.grid(linestyle='dotted')
    plt.plot(xa, ya, color='b')
    plt.show()

AjustePolinomio(x, y)