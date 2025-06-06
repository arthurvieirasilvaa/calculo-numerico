import numpy as np

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


X_ESTIMADO = 5.2 # valor de x que deseja-se estimar

# Valores de x e y para a alternativa a)
xa = np.array([0, 2, 4, 6, 8, 10])
ya = np.array([0.9, 2, 2.8, 3.1, 5.9, 6], dtype="double")

T = diferencas_divididas(xa, ya)
p = interpolacao_newton(xa, X_ESTIMADO, T)
print(f"f({X_ESTIMADO}) = {p}")

p = interpolacao_lagrange(xa, ya, X_ESTIMADO)
print(f"f({X_ESTIMADO}) = {p}")
