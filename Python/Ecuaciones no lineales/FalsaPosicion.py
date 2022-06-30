def falsap(funcion, x_a, x_b, iteraciones=10, error_r=0.001):
    # Se inicializan las variables
    solucion = None
    contador = 0
    error_calculado = 101
    # Se evalua si la raiz esta dentro del intervalo
    if funcion(x_a) * funcion(x_b) <= 0:
        # Se procede a calcular la funcion
        while contador <= iteraciones and error_calculado >= error_r:
            contador = contador + 1
            solucion = x_b - ((funcion(x_b) * (x_b - x_a)) / (funcion(x_b) - funcion(x_a)))
            error_calculado = abs((solucion - x_a) / solucion) * 100
            # Se redefine el nuevo intervalo con los signos
            if funcion(x_a) * funcion(solucion) >= 0:
                x_a = solucion
            else:
                x_b = solucion

        print('la solucion aproximada es: {:.3f}'.format(solucion))
        print('encontrada en: {:.0f}'.format(contador) + ' iteraciones')
        print('con un error de:{:.3f}'.format(error_calculado) + '%')
    else:
        print('no existe solucion en ese intervalo')


falsap(lambda x: 4 * x ** 4 - 9 * x ** 2 + 1, 0, 1, 5, 5)