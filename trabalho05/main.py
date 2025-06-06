import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt

# Função utilizada para calcular a Tabela de Diferenças Divididas:
def diferencas_divididas(x, y):
    n = len(x)
    T = np.zeros((n,n))
    T [:, 0] = y[:] # diferenças dividas de ordem 0 é o próprio y

    for k in range(1, n):
        for i in range(n-k):
            T[i][k] = (T[i+1, k-1] - T[i, k-1]) / (x[i+k] - x[i])
    
    return T 


# Função utilizada para estimar valor y de um dado ponto x utilizando a Interpolação de Newton:
def interpolacao_newton(x, X_ESTIMADO, T):
    n = len(x)

    p = 0
    for i in range(n):
        resp = 1
        for j in range(i):
            resp *= (X_ESTIMADO - x[j]) # calcula o produto presente na fórumala de Newton
        p += T[0][i] * resp # atualiza a aproximação de f(x)

    return p


# Função utilizada para estimar valor y de um dado ponto x utilizando a Interpolação de Lagrange:
def interpolacao_lagrange(x, y, X_ESTIMADO):
    n = len(x)
    
    p = 0
    for i in range(n):
        l = 1
        for j in range(n):
            if i != j:
                l *= (X_ESTIMADO-x[j]) / (x[i]-x[j])
        
        p += y[i] * l

    return p


# Função utilizada para obter os coeficientes a do polinômio interpolador na forma canônica:
def obter_coeficientes(x, y):
    vandermonde = np.vander(x, increasing=True) # gerando a matriz de Vandermonde
    
    # Retorna o vetor de coeficintes a, solucionando o sisteman Vandermonde x a = y 
    return linalg.solve(vandermonde, y)


# Função utilizada para plotar o gráfico com a função polinomial encontrada:
def plotar_grafico(x, y, a, alternativa):
    x_plot = np.linspace(min(x), max(x), 100)    
    
    y_plot = 0
    for i in range(len(a)):
        y_plot += a[i] * x_plot**i

    
    # Plota o polinômio e os pontos dados
    plt.figure(f'Figura {alternativa}')
    plt.plot(x_plot, y_plot, label="Polinômio Interpolador na forma canônica", color="blue", linewidth=3.0)
    plt.scatter(x, y, color="green", label="Valores de x fornecidos", linewidth=3.0)
    
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.grid(True)
    
    plt.savefig(f"grafico_{alternativa}")
    plt.show()


# Função utilizada para imprimir o polinômio interpolador na forma canônica de maneira formatada:
def imprimir_polinomio(a):
    p = f"P(x) = {a[0]:.3f} "

    for i in range(1, len(a)):
        if a[i] > 0:
            p += f"+ {a[i]:.3f}x^{i} "

        else:
            p += f"- {abs(a[i]):.3f}x^{i} "

    print(p)


X_ESTIMADO = 5.2 # valor de x que deseja-se estimar

# Valores de x e y para a alternativa a)
xa = np.array([0, 2, 4, 6, 8, 10])
ya = np.array([0.9, 2, 2.8, 3.1, 5.9, 6], dtype="double")

# Valores de x e y para a alternativa b)
xb = np.array([0, 2, 4, 6, 8])
yb = np.array([1, 9.389, 58.598, 409.429, 2988.958], dtype="double")

# Valores de x e y para a alternativa c)
xc = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])
yc = np.array([1, 7, 21, 22, 34, 34.5, 35, 64.5, 65], dtype="double")


# a)
print("\nA)")

# Interpolação de Lagrange:
print("\nInterpolação de Lagrange:")
p = interpolacao_lagrange(xa, ya, X_ESTIMADO)
print(f"\tP({X_ESTIMADO}) = {p}")

# Interpolação de Newton:
print("\nInterpolação de Newton:")
T = diferencas_divididas(xa, ya)
print("\tTabela de Diferenças Dividias:")
print(np.round(T, 5))

p = interpolacao_newton(xa, X_ESTIMADO, T)
print(f"\tP({X_ESTIMADO}) = {p}")

# Coeficientes a do polinômio interpolador na forma canônica:
a = obter_coeficientes(xa, ya)
print(f"\tCoeficientes a = [{a}]")
imprimir_polinomio(a)

plotar_grafico(xa, ya, a, 'a')

# b)
print("\nB)")

# Interpolação de Lagrange:
print("\nInterpolação de Lagrange:")
p = interpolacao_lagrange(xb, yb, X_ESTIMADO)
print(f"\tP({X_ESTIMADO}) = {p}")

# Interpolação de Newton:
print("\nInterpolação de Newton:")
T = diferencas_divididas(xb, yb)
print("\tTabela de Diferenças Dividias:")
print(np.round(T, 5))

p = interpolacao_newton(xb, X_ESTIMADO, T)
print(f"\tP({X_ESTIMADO}) = {p}")

# Coeficientes a do polinômio interpolador na forma canônica:
a = obter_coeficientes(xb, yb)
print(f"\tCoeficientes a = [{a}]")
imprimir_polinomio(a)

plotar_grafico(xb, yb, a, 'b')

# c)
print("\nC)")

# Interpolação de Lagrange:
print("\nInterpolação de Lagrange:")
p = interpolacao_lagrange(xc, yc, X_ESTIMADO)
print(f"\tP({X_ESTIMADO}) = {p}")

# Interpolação de Newton:
print("\nInterpolação de Newton:")
T = diferencas_divididas(xc, yc)
print("\tTabela de Diferenças Dividias:")
print(np.round(T, 5))

p = interpolacao_newton(xc, X_ESTIMADO, T)
print(f"\tP({X_ESTIMADO}) = {p}")

# Coeficientes a do polinômio interpolador na forma canônica:
a = obter_coeficientes(xc, yc)
print(f"\tCoeficientes a = [{a}]")
imprimir_polinomio(a)

plotar_grafico(xc, yc, a, 'c')
