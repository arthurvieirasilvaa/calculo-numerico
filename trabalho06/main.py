import math
import numpy as np
from numpy.polynomial.legendre import leggauss

# Função utilizada para retornar a função f(x) utilizada no primeiro exercício:
def f1(x):
    return 3 + (4*x) - (3 * (x**2)) + (5 * (x**3)) - (x**4) + (4 * (x**5))


# Função utilizada para retornar a função f(x) utilizada no segundo exercício:
def f2(x):
    return math.sqrt(x)


# Função utilizada para calcular a integral analítica da função f(x) utilizada no primeiro exercício: 
def integral_analitica1(a, b):
    # Em relação ao valor de a:
    sol1 = (3 * a) + (2 * (a**2)) - (a**3) + ((5 * (a**4))/4) - ((a**5) / 5) + ((2 * (a**6)) / 3)

    # Em relação ao valor de b:
    sol2 = (3 * b) + (2 * (b**2)) - (b**3) + ((5 * (b**4))/4) - ((b**5) / 5) + ((2 * (b**6)) / 3)
    
    return sol2 - sol1

# Função utilizada para calcular a integral analítica da função f(x) utilizada no segundo exercício:
def integral_analitica2(a, b):
    return (((2* pow(b, 3/2)) - (2 * pow(a, 3/2))) / 3)


# Função utilizada para aproximar a integral da função f(x) com o método do trapézio:
def metodo_trapezio(f, a, b, m):
    if m < 2:
        print("Informe pelo menos 2 pontos!\n")
        return None

    n = m-1
    print(f"{n} subintervalos")

    h = (b-a) / n
    x = np.linspace(a, b, m)
    print(f"Pontos utilizados x = {x}")

    res = f(x[0])
    for i in range(1, n):
        res += 2 * f(x[i])

    res += f(x[n])

    return (h/2) * res


# Função utilizada para aproximar a integral da função f(x) com o método de Simpson (1/3):
def metodo_simpson(f, a, b, m):
    if m < 3:
        print("Informe pelo menos 3 pontos!\n")
        return None
    
    n = m-1
    print(f"{n} subintervalos")

    if n % 2 != 0:
        print("O número de subintervalos deve ser par!\n")
        return None

    h = (b-a) / n
    x = np.linspace(a, b, m)
    print(f"Pontos utilizados x = {x}")

    res = f(x[0])
    for i in range(1, n, 2):
        res += 4 * f(x[i]) # índices ímpares

    for i in range(2, n-1, 2):
        res += 2 * f(x[i]) # índices pares com exceção de f[x0] e f[xn]
    
    res += f(x[n])

    return (h/3) * res


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


# Função utilizada para imprimir a saída dos métodos de maneira formatada:
def imprime_saida(f, funcao_metodo, integral_analitica, a, b, lista_pontos, nome_metodo):
    analitico = integral_analitica(a, b)
    print(f"Integral analítica: {analitico}")
    
    print(f"\n============ {nome_metodo} ============\n")

    for pontos in lista_pontos:
        print(f"\nn = {pontos} pontos")
        res = funcao_metodo(f, a, b, pontos)

        if res is not None:
            print(f"\tResultado da integral com o {nome_metodo}: {res}")
            erro_absoluto = abs(analitico - res)
            print(f"\tErro Absoluto para o {nome_metodo}: {erro_absoluto}")


# Inicializando as variáveis:

# 1)

# Número de pontos para os métodos do exercício 1:
pontos_trapezio = [2, 5, 13]
pontos_simpson = [3, 5, 13]
pontos_gaussiana = [1, 2, 3]

# Intervalo de integração:
a = 0
b = 2

print(f"\nIntervalo [a, b] = [{a}, {b}]")

imprime_saida(f1, metodo_trapezio, integral_analitica1, a, b, pontos_trapezio, "método do trapézio")
imprime_saida(f1, metodo_simpson, integral_analitica1, a, b, pontos_simpson, "método de Simpson (1/3)")
imprime_saida(f1, quadratura_gaussiana, integral_analitica1, a, b, pontos_gaussiana, "método da Quadratura Gaussiana")

# 2)

# Número de pontos para os métodos do exercício 2:
pontos_trapezio_simpson = [2, 5, 99, 599, 10001]
pontos_gaussiana = [5, 10, 15, 20, 50, 100]

# Intervalo de integração:
a = 0
b = 20

print(f"\nIntervalo [a, b] = [{a}, {b}]")

imprime_saida(f2, metodo_trapezio, integral_analitica2, a, b, pontos_trapezio_simpson, "método do trapézio")
imprime_saida(f2, metodo_simpson, integral_analitica2, a, b, pontos_trapezio_simpson, "método de Simpson (1/3)")
imprime_saida(f2, quadratura_gaussiana, integral_analitica2, a, b, pontos_gaussiana, "método da Quadratura Gaussiana")
