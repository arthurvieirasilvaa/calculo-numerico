import numpy as np
from numpy import linalg


# Função utilizada para criar a matriz A da letra a):
def criar_matriz1():
    A = np.array([[3, -4, 1], 
                 [1, 2, 2], 
                 [4, 0, -3]], dtype=float)
    return A


# Função utilizada para criar o vetor B da letra a):
def criar_vetor1():
    B = np.array([9, 3, -2], dtype=float)
    return B


# Função utilizada para criar a matriz A da letra b):
def criar_matriz2():
    A = np.array([[0.1, -3, 4, 7, 4, 14], 
                [-2, 4, 2, 5, -5, 21],
                [1, 200, 3, -3, 3, -4],
                [-1, 5, 4, 22, 7, -8],
                [4, 8, 7, 10, -9, 1],
                [-55, -1, 35, 1, 11, 0.2]])
    return A


# Função utilizada para criar o vetor B da letra b):
def criar_vetor2():
    B = np.array([14, 26, 19, -5, 7, -4])
    return B


# Função utilizada para realizar a Eliminação de Gauss sem pivoteamento:
def eliminacao_gaussiana(A, B):
    n = A.shape[0] # obtendo o número de elementos da matriz A

    # Eliminação:
    for k in range(n-1): # percorre as colunas
        for i in range(k+1, n): # percorre as linhas que estão abaixo de k
            m = A[i][k]/A[k][k] # obtém o multiplicador da linha
            A[i][k] = 0
            
            # Atualizando a linha:
            for j in range(k+1, n):
                A[i][j] -= m * A[k][j]
            
            B[i] -= m * B[k] # atualizando o vetor B

    # Solucionando o sistema triangular superior:
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma += A[i][j] * x[j]

        x[i] = (B[i] - soma) / A[i][i]

    return x


# Função utilizada para realizar a fatoração LU com pivoteamento parcial:
def fatoracaoLU_pivoteamento_parcial(A, B):
    n = A.shape[0] # obtendo o número de elementos da matriz A

    # Criando as matrizes identidade:
    P = np.eye(n)
    U = A.copy().astype(float)
    L = np.eye(n)

    for k in range(n): # percorre as colunas
        maior_linha = k + np.argmax(abs(U[k:, k])) # encontrando a linha com o maior |A[i, j]|, i >= j   

        if maior_linha != k:
            # Trocando as linhas:
            U[[k, maior_linha], :] = U[[maior_linha, k], :]
            P[[k, maior_linha], :] = P[[maior_linha, k], :]
            L[[k, maior_linha], :k] = L[[maior_linha, k], :k]
        
        # Zerando os elementos abaixo do pivô:
        for i in range(k+1, n):
            L[i, k] = U[i, k] / U[k, k] # obtendo o multiplicador de uma linha
            U[i, k:] -= L[i, k] * U[k, k:] # atualizando a linha

    y = np.zeros(n)
    Pb = P @ B # Produto PB
    
    # Solucionando Ly = Pb
    for i in range(n):
        soma = 0
        for j in range(i):
            soma += L[i][j] * y[j]
        
        y[i] = (Pb[i] - soma) / L[i][i]

    x = np.zeros(n)

    # Solucionando Ux = y:
    for i in range(n-1, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma += U[i][j] * x[j]

        x[i] = (y[i] - soma) / U[i][i]

    return x


# Eliminação de Gauss sem pivoteamento:
print("\n############### Eliminação de Gauss sem pivoteamento ###############\n")

# a)
A1 = criar_matriz1()
B1 = criar_vetor1()

x1 = eliminacao_gaussiana(A1.copy(), B1.copy())
erro1 = np.linalg.norm(A1 @ x1 - B1)
print(f"\tSolução a): {x1}")
print(f"\t||Ax - B||: {erro1}")

# b)
A2 = criar_matriz2()
B2 = criar_vetor2()

x2 = eliminacao_gaussiana(A2.copy(), B2.copy())
erro2 = np.linalg.norm(A2 @ x2 - B2)
print(f"\tSolução b): {x2}")
print(f"\t||Ax - B||: {erro2}")

# Fatoração LU com pivoteamento parcial:
print("\n############### Fatoração LU com pivoteamento parcial ###############\n")

# a)
A1 = criar_matriz1()
B1 = criar_vetor1()

x1 = fatoracaoLU_pivoteamento_parcial(A1.copy(), B1.copy())
erro1 = np.linalg.norm(A1 @ x1 - B1)
print(f"\tSolução a): {x1}")
print(f"\t||Ax - B||: {erro1}")

# b)
A2 = criar_matriz2()
B2 = criar_vetor2()

x2 = fatoracaoLU_pivoteamento_parcial(A2.copy(), B2.copy())
erro2 = np.linalg.norm(A2 @ x2 - B2)
print(f"\tSolução b): {x2}")
print(f"\t||Ax - B||: {erro2}")
