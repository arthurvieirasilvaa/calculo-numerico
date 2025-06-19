import math
import numpy as np

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
        return

    n = m-1
    print(f"{n} subintervalos")
    h = (b-a) / n

    print("\nMétodo do trapźeio:")
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
        return
    
    n = m-1
    print(f"{n} subintervalos")

    if n % 2 != 0:
        print("O número de subintervalos deve ser par!\n")

    h = (b-a) / n

    print("\nMétodo de Simpson (1/3):")
    x = np.linspace(a, b, m)
    print(f"Pontos utilizados x = {x}")

    res = f(x[0])
    for i in range(1, n, 2):
        res += 4 * f(x[i]) # índices ímpares

    for i in range(2, n-1, 2):
        res += 2 * f(x[i]) # índices pares com exceção de f[x0] e f[xn]
    
    res += f(x[n])
    return (h/3) * res


# Inicializando as variáveis:

# 1)

# Intervalo de integração:
a = 0
b = 2

print(f"Intervalo [a, b] = [{a}, {b}]")

# Método do trapézio:

# Número de pontos:
m1 = 2
m2 = 5
m3 = 13

analitico = integral_analitica1(a, b)
print(f"Integral analítica: {analitico}")

res_trapezio = metodo_trapezio(f1, a, b, m1)
print(f"Resultado da integral com o método do trapézio: {res_trapezio}")
erro_trapezio = abs(analitico - res_trapezio)
print(f"Erro de truncamento para o método do trapézio: {erro_trapezio}")

res_trapezio = metodo_trapezio(f1, a, b, m2)
print(f"Resultado da integral com o método do trapézio: {res_trapezio}")
erro_trapezio = abs(analitico - res_trapezio)
print(f"Erro de truncamento para o método do trapézio: {erro_trapezio}")

res_trapezio = metodo_trapezio(f1, a, b, m3)
print(f"Resultado da integral com o método do trapézio: {res_trapezio}")
erro_trapezio = abs(analitico - res_trapezio)
print(f"Erro de truncamento para o método do trapézio: {erro_trapezio}")

# 1° Método de Simpson:

# Número de pontos:
m1 = 3

res_simpson = metodo_simpson(f1, a, b, m1)
print(f"Resultado da integral com o 1° método de Simpson: {res_simpson}")
erro_simpson = abs(analitico - res_simpson)
print(f"Erro de truncamento para o 1° método de Simpson: {erro_simpson}")

res_simpson = metodo_simpson(f1, a, b, m2)
print(f"Resultado da integral com o 1° método de Simpson: {res_simpson}")
erro_simpson = abs(analitico - res_simpson)
print(f"Erro de truncamento para o 1° método de Simpson: {erro_simpson}")

res_simpson = metodo_simpson(f1, a, b, m2)
print(f"Resultado da integral com o 1° método de Simpson: {res_simpson}")
erro_simpson = abs(analitico - res_simpson)
print(f"Erro de truncamento para o 1° método de Simpson: {erro_simpson}")


# 2)

# Intervalo de integração:
a = 0
b = 20

print(f"Intervalo [a, b] = [{a}, {b}]")

# Método do trapézio:

# Número de pontos:
m1 = 2
m2 = 5
m3 = 99
m4 = 599
m5 = 10001

analitico = integral_analitica1(a, b)
print(f"Integral analítica: {analitico}")

res_trapezio = metodo_trapezio(f2, a, b, m1)
print(f"Resultado da integral com o método do trapézio: {res_trapezio}")
erro_trapezio = abs(analitico - res_trapezio)
print(f"Erro de truncamento para o método do trapézio: {erro_trapezio}")

res_trapezio = metodo_trapezio(f2, a, b, m2)
print(f"Resultado da integral com o método do trapézio: {res_trapezio}")
erro_trapezio = abs(analitico - res_trapezio)
print(f"Erro de truncamento para o método do trapézio: {erro_trapezio}")

res_trapezio = metodo_trapezio(f2, a, b, m3)
print(f"Resultado da integral com o método do trapézio: {res_trapezio}")
erro_trapezio = abs(analitico - res_trapezio)
print(f"Erro de truncamento para o método do trapézio: {erro_trapezio}")

res_trapezio = metodo_trapezio(f2, a, b, m4)
print(f"Resultado da integral com o método do trapézio: {res_trapezio}")
erro_trapezio = abs(analitico - res_trapezio)
print(f"Erro de truncamento para o método do trapézio: {erro_trapezio}")

res_trapezio = metodo_trapezio(f2, a, b, m5)
print(f"Resultado da integral com o método do trapézio: {res_trapezio}")
erro_trapezio = abs(analitico - res_trapezio)
print(f"Erro de truncamento para o método do trapézio: {erro_trapezio}")

# 1° Método de Simpson:

res_simpson = metodo_simpson(f2, a, b, m1)
print(f"Resultado da integral com o 1° método de Simpson: {res_simpson}")
erro_simpson = abs(analitico - res_simpson)
print(f"Erro de truncamento para o 1° método de Simpson: {erro_simpson}")

res_simpson = metodo_simpson(f2, a, b, m2)
print(f"Resultado da integral com o 1° método de Simpson: {res_simpson}")
erro_simpson = abs(analitico - res_simpson)
print(f"Erro de truncamento para o 1° método de Simpson: {erro_simpson}")

res_simpson = metodo_simpson(f2, a, b, m3)
print(f"Resultado da integral com o 1° método de Simpson: {res_simpson}")
erro_simpson = abs(analitico - res_simpson)
print(f"Erro de truncamento para o 1° método de Simpson: {erro_simpson}")

res_simpson = metodo_simpson(f2, a, b, m4)
print(f"Resultado da integral com o 1° método de Simpson: {res_simpson}")
erro_simpson = abs(analitico - res_simpson)
print(f"Erro de truncamento para o 1° método de Simpson: {erro_simpson}")

res_simpson = metodo_simpson(f2, a, b, m5)
print(f"Resultado da integral com o 1° método de Simpson: {res_simpson}")
erro_simpson = abs(analitico - res_simpson)
print(f"Erro de truncamento para o 1° método de Simpson: {erro_simpson}")