import numpy as np
from numpy import linalg


# Função utilizada para criar a matriz de coeficientes A:
def criar_matriz():
    A = np.array([[4, -3, 1],
                 [2, 4, -2],
                 [4, 3, 3]])
    
    return A


# Função utilizada para criar o vetor dos termos constantes b:
def criar_vetor():
    b = np.array([29, -18, 3])

    return b


# Função utilizada para implementar o Método de Jacobi utilizando coeficiente de relaxação:
def jacobi(A, b, n, TOL, MAX_ITERACOES, c):
    print("\n========= Método de Jacobi =========\n")

    x0 = np.zeros(n)
    x = np.zeros(n)

    print(f"Coeficiente de relaxação: {c}")
    print(f"x inicial: {x}")

    contador = 1
    while contador <= MAX_ITERACOES:
        for i in range(n):
            soma = b[i]
            for j in np.concatenate((np.arange(0, i), np.arange(i+1, n))):
                soma -= A[i, j] * x0[j]
            
            x_novo = soma / A[i, i]
            x[i] = (1 - c) * x0[i] + c * x_novo

        # Critério de parada:
        erro = linalg.norm(x-x0, np.inf) / linalg.norm(x, np.inf)
        if erro <= TOL:
            return x
        
        print(f"\nIteração {contador}:")
        print(f"\tx = {x}")
        print(f"\tErro: {erro}")
        
        x0 = np.copy(x)
        contador += 1

    return x


# Função utilizada para implementar o Método de Gauss-Seidel utilizando coeficiente de relaxação:
def gauss_seidel(A, b, n, TOL, MAX_ITERACOES, c):
    print("\n========= Método de Gauss-Seidel =========\n")

    x0 = np.zeros(n)
    x = np.zeros(n)


    contador = 1
    while contador <= MAX_ITERACOES:
        for i in np.arange(n):
            soma = b[i]
            for j in np.concatenate((np.arange(0, i), np.arange(i+1, n))):
                soma -= A[i, j] * x[j] # utiliza o valor mais atual de x e não x0
        
            x_novo = soma / A[i, i]
            x[i] = (1 - c) * x[i] + c * x_novo

        # Critério de parada:
        erro = linalg.norm(x-x0, np.inf) / linalg.norm(x, np.inf)
        if erro <= TOL:
            return x
        
        print(f"\nIteração {contador}:")
        print(f"\tx = {x}")
        print(f"\tErro: {erro}")
        
        x0 = np.copy(x)
        contador += 1

    return x


# Criando os dados de entrada:
A = criar_matriz()
b = criar_vetor()
n = A.shape[0] # obtendo as dimensões da matriz A

TOL = pow(10, -4) # definindo o critério para a tolerância
MAX_ITERACOES = 50 # definindo o número máximo de iterações

# Método de Jacobi:

# Método de Jacobi sem coeficiente de relaxação, isto é, c = 1:
x = jacobi(A, b, n, TOL, MAX_ITERACOES, 1)
print(f"\nSolução final encontrada para o Método de Jacobi: {x}")

# Método de Jacobi com coeficiente de relaxação c = 0.3:
x = jacobi(A, b, n, TOL, MAX_ITERACOES, 0.3)
print(f"\nSolução final encontrada para o Método de Jacobi: {x}")

# Método de Jacobi com coeficiente de relaxação c = 0.5:
x = jacobi(A, b, n, TOL, MAX_ITERACOES, 0.5)
print(f"\nSolução final encontrada para o Método de Jacobi: {x}")

# Método de Jacobi com coeficiente de relaxação c = 1.5:
x = jacobi(A, b, n, TOL, MAX_ITERACOES, 1.5)
print(f"\nSolução final encontrada para o Método de Jacobi: {x}")

# Método de Gauss-Seidel:

# Método de Gauss-Seidel sem coeficiente de relaxação, isto é, c = 1:
x = gauss_seidel(A, b, n, TOL, MAX_ITERACOES, 1)
print(f"\nSolução final encontrada para o Método de Gauss-Seidel: {x}")

# Método de Gauss-Seidel com coeficiente de relaxação c = 0.3:
x = gauss_seidel(A, b, n, TOL, MAX_ITERACOES, 0.3)
print(f"\nSolução final encontrada para o Método de Gauss-Seidel: {x}")

# Método de Gauss-Seidel com coeficiente de relaxação c = 0.5:
x = gauss_seidel(A, b, n, TOL, MAX_ITERACOES, 0.5)
print(f"\nSolução final encontrada para o Método de Gauss-Seidel: {x}")

# Método de Gauss-Seidel com coeficiente de relaxação c = 1.5:
x = gauss_seidel(A, b, n, TOL, MAX_ITERACOES, 1.5)
print(f"\nSolução final encontrada para o Método de Gauss-Seidel: {x}")
