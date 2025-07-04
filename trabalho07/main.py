import numpy as np
from numpy.polynomial.legendre import leggauss
import matplotlib.pyplot as plt

# Função utilizada para retornar a função f(x) utilizada (caso contínuo):
def f(x):
    return np.sin(x)


# Função utilizada para aproximar a integral da função f(x) com o método da Quadratura Gaussiana:
def quadratura_gaussiana(f, a, b, n):
    if n <= 0:
        print("O número de pontos precisa ser pelo menos 1.")
        return None

    # Obtendo os vetores dos nós (x) e dos pesos (w):
    nos, pesos = leggauss(n)

    # Transformando do intervalo [a, b] para [-1, 1]:
    x_novo = ((b-a) / 2) * nos + ((a+b) / 2)
    f_novo = f(x_novo)

    soma = np.sum(pesos * f_novo)
    
    return ((b-a) / 2) * soma


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


# Função utilizada para solucionar o método dos mínimos quadrados (caso discreto) e aproximar uma função f(x):
def minimos_quadrados_discreto(x, y, k):
    A = np.zeros((k+1, k+1))
    B = np.zeros(k+1)
    n = len(x)

    # Gerando a matriz A:
    for i in range(k+1):
        for j in range(k+1):
            for x_i in x:
                A[i, j] += pow(x_i, i+j)

    # Gerando o vetor b:
    for i in range(k+1):
        for x_i, y_i in zip(x, y):
            B[i] += pow(x_i, i) * y_i

    return A, B


# Função utilizada para solucionar o método dos mínimos quadrados (caso contínuo) e aproximar uma função f(x):
def minimos_quadrados_continuo(f, a, b):
    A = np.zeros((k+1, k+1))
    B = np.zeros(k+1)

    # Gerando a matriz A:
    for i in range(k+1):
        for j in range(k+1):
            funcao_integrada = lambda x: pow(x, i+j)
            A[i, j] = quadratura_gaussiana(funcao_integrada, a, b, 20)
        
    # Gerando o vetor b:
    for i in range(k+1):
        funcao_integrada = lambda x: f(x) * pow(x, i)
        B[i] = quadratura_gaussiana(funcao_integrada, a, b, 20)

    return A, B


# Função utilizada para imprimir o polinômio obtido de maneira formatada:
def imprimir_polinomio(x):
    p = f"P(x) = {x[0]:.3f} "

    for i in range(1, len(x)):
        if x[i] > 0:
            p += f"+ {x[i]:.3f}x^{i} "

        else:
            p += f"- {abs(x[i]):.3f}x^{i} "

    print(f"{p}")


# Função utilizada para obter o resultado de P(x) em um determinado ponto:
def P(a, xp):
    p = a[-1]
    
    for i in range(len(a)-2, -1, -1):
        p = p*xp+a[i]

    return p 


# Definindo os valores utilizados:

# Caso discreto:

valores_x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16], dtype=float)
valores_y = np.array([1, 7, 21, 22, 34, 34.5, 35, 64.5, 65], dtype=float)
k_discreto = 2 # grau do polinômio

A_discreto, B_discreto = minimos_quadrados_discreto(valores_x, valores_y, k)

# Imprimindo a saída:
print("\n========= Mínimos Quadrados (caso discreto) =========\n")
print(f"\nValores de x: {valores_x}")
print(f"\nValores de y: {valores_y}")
print(f"\nPolinômio de grau: {k_discreto}")
print("\nMatriz A:")
print(A_discreto)
print("\nVetor b:")
print(B_discreto)

coeficientes_discreto = eliminacao_gaussiana(A_discreto, B_discreto)
print("\nVetor de coeficientes obtido:")
print(coeficientes_discreto)

print("\nFunção aproximada:")
imprimir_polinomio(coeficientes_discreto)

# Caso contínuo:

print("\n========= Mínimos Quadrados (caso contínuo) =========\n")
a = 0
b = np.pi()/2
k_continuo = 3 # grau do polinômio

A, B = minimos_quadrados_continuo(f, a, b)

print(f"\nIntervalo [a, b] = {[a, b]}")
print(f"\nPolinômio de grau: {k}")
print("\nMatriz A:")
print(A)
print("\nVetor b:")
print(B)

coeficientes = eliminacao_gaussiana(A, B)
print("\nVetor de coeficientes obtido:")
print(coeficientes)

print("\nFunção aproximada:")
imprimir_polinomio(coeficientes)

print("\nTeste para alguns pontos:")
print(f"\tP(0) = {P(coeficientes, 0)} e f(0) = {f(0)}")
print(f"\tP(0.2) = {P(coeficientes, 0.2)} e f(0.2) = {f(0.2)}")
print(f"\tP(0.5) = {P(coeficientes, 0.5)} e f(0.5) = {f(0.5)}")
print(f"\tP(0.8) = {P(coeficientes, 0.8)} e f(0.8) = {f(0.8)}")
print(f"\tP(1) = {P(coeficientes, 1)} e f(1) = {f(1)}")
