import numpy as np
from numpy import linalg

def criar_matriz():
    A = np.array([[3, -4, 1], 
                 [1, 2, 2], 
                 [4, 0, -3]], dtype=float)
    # A = np.array([[0.1, -3, 4, 7, 4, 14], 
    #             [-2, 4, 2, 5, -5, 21],
    #              [1, 200, 3, -3, 3, -4],
    #              [-1, 5, 4, 22, 7, -8],
    #              [-55, -1, 35, 1, 11, 0.2]])
    return A


def criar_vetor():
    B = np.array([9, 3, -2], dtype=float)
    # B = np.array([14, 26, 19, -5, 7, -4])
    return B


def eliminacao_gaussiana(A, B):
    n = A.shape[0] # obtendo o número de elementos da matriz A

    # Eliminação:
    for k in range(n-1):
        for i in range(k+1, n):
            m = A[i][k]/A[k][k]
            A[i][k] = 0
            
            for j in range(k+1, n):
                A[i][j] -= m * A[k][j]
            
            B[i] -= m * B[k]

    # Solucionando o sistema triangular superior:
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma += A[i][j] * x[j]

        x[i] = (B[i] - soma) / A[i][i]

    return x

A = criar_matriz()

B = criar_vetor()
x = eliminacao_gaussiana(A.copy(), B.copy())

print(f"Solução: {x}")