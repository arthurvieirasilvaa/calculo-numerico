import numpy as np

# Função utilizada para calcular a Tabela de Diferenças Divididas:
def diferencas_divididas(x, y):
    n = len(x)
    t = []
    t.append(y)

    passo = 1 # deslocamento inicial no vetor x
    for i in range(n-1):
        ordem = [] # armazena a ordem das diferenças
        for j in range(len(t[i])-1):
            diferenca = (t[i][j+1] - t[i][j]) / (x[j+passo] - x[j])
            ordem.append(diferenca)
        t.append(ordem)
        passo += 1 # atualiza o deslocamento no vetor x
    
    return t


# Função utilizada para estimar valor y de um dado ponto x utilizando a fórmula de Newton:
def interpolacao_newton(x, t, x_val):
    p = 0 # valor inicial da aproximação de f(x)
    grau = 0 # grau atual do polinômio

    print(f"Ponto estimado: {x_val}")

    for i in range(len(t)):
        for j in range(grau): 
            t[i][0] *= (x_val - x[j]) # calcula o produto presente na fórumala de Newton
        grau += 1 # atualiza o grau do polinômio
        p += t[i][0] # atualiza a aproximação de f(x)
        # print(f"Função P_{i}(x) = {p} incremento = {t[i][0]}") arrumar

    return p

def interpolacao_lagrange(x, y, X_ESTIMADO):
    n = len(x)
    
    y_encontrado = 0
    for i in range(n):
        l = 1
        for j in range(n):
            if i != j:
                l *= (X_ESTIMADO-x[j]) / (x[i]-x[j])
        
        y_encontrado += y[i] * l

    return y_encontrado


X_ESTIMADO = 5.2 # valor de x que deseja-se estimar

# Valores de x e y para a alternativa a)
xa = np.array([0, 2, 4, 6, 8, 10])
ya = np.array([0.9, 2, 2.8, 3.1, 5.9, 6], dtype="double")

# t = diferencas_divididas(x, y)
# p = interpolacao_newton(x, t, x_val)

y_encontrado = interpolacao_lagrange(xa, ya, X_ESTIMADO)
print(f"f({X_ESTIMADO}) = {y_encontrado}")