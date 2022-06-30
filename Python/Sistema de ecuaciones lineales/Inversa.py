# Inversa de una matriz

def imprimir(A, titulo):
    print(titulo)
    for fila in A:
        for value in fila:
            print(f"{value:6.2f} ", end="")
        print()
    print("")


def inversion(A):
    num_filas = len(A)
    num_cols = len(A[0])

    m1 =  - 1
    n2 = num_cols * 2

    if num_filas != num_cols:
        print("Error: La matriz no es cuadrada. Por tanto, no es invertible.")
        return None

    # Construcción de la matriz A | I
    for idx_fila in range(num_filas):
        A[idx_fila] += [1 if idx_fila == j else 0 for j in range(num_filas)]

    imprimir(A, "Matriz ampliada inicial:")

    # Algoritmo - Triangularización superior

    for idx_col in range(num_cols):
        # Búsqueda de pivote
        print(f"Procesando columna {idx_col}")
        l = [(abs(A[idx_fila][idx_col]), idx_fila) for idx_fila in range(idx_col, num_filas) if A[idx_fila][idx_col] != 0]
        if len(l) == 0:
            print("Error: La matriz no es invertible.")
            return None

        idx_fila = min(l)[1]
        if idx_fila != idx_col:
            print(f"Intercambiar fila {idx_fila} con {idx_col}")
            A[idx_col], A[idx_fila] = A[idx_fila],  A[idx_col]
            imprimir(A, "Matriz intercambiada")

        # Triangularización superior
        for idx_fila in [idx for idx in range(idx_col + 1, num_filas) if A[idx][idx_col] != 0]:
            alpha = -A[idx_fila][idx_col] / A[idx_col][idx_col]
            print(f"Ajuste para fila {idx_fila} es {alpha}")
            for k in range(n2):
                A[idx_fila][k] += A[idx_col][k] * alpha
            imprimir(A, "Matriz ajustada")

    imprimir(A, "Matriz triangulación superior")

    # Algoritmo - Triangularización inferior

    for idx_col in range(1, num_cols):
        print(f"Procesando columna {idx_col}")
        for idx_fila in range(idx_col):
            alpha = -A[idx_fila][idx_col] / A[idx_col][idx_col]
            print(f"Fila {idx_fila}, factor {alpha}")
            for k in range(idx_col, n2):
                A[idx_fila][k] += A[idx_col][k] * alpha
            imprimir(A, "Ajustada")

    imprimir(A, "Matriz triangulación inferior")
    # Algoritmo - Transformación a la matriz identidad

    for idx_fila in range(num_filas):
        alpha = A[idx_fila][idx_fila]
        for idx_col in range(idx_fila, n2):
            A[idx_fila][idx_col] /= alpha

    imprimir(A, "Matriz identidad")

    inversa = []
    for fila in A:
        inversa.append(fila[num_cols:])

    return inversa

A = [[5, 8, 9], [2, 6, 6], [3, 1, 1]]
x = inversion(A)
imprimir(x, "Inversa")