import numpy as np
import math


# Função da alternativa a):
def func1(x):
    return 5*math.log(x) - 2 + 0.4*x


# Derivada da função da alternativa a):
def derivada1(x):
    return 5/x + 0.4


# Função da alternativa b):
def func2(x):
    return x - ((x**5 - 26) / (5 * x**4))


# Derivada da função da alternativa b):
def derivada2(x):
    return 1 - ((x**5 + 104) / (5 * x**5))


# Método da Bisseção:
def bissecao(f, a, b):
    fa = f(a)
    fb = f(b)

    # Verificando se há uma raiz no intervalo [a, b] fornecido:
    if fa * fb > 0:
        print(f"Não existe raiz no intervalo [{a}, {b}].")

    else:
        i = 1
        # Enquanto o número máximo de iterações não for atingido:
        while i <= MAX_ITERACOES:
            x = (a+b)/2 # obtém o valor de x
            fx = f(x)

            # Imprindo a iteração atual:
            print(f"Iteração {i}:")
            print(f"\tIntervalo [{a}, {b}]\n\tx = {x}\n\tf(x) = {fx}")

            # Verifica a condição de parada:
            if abs(fx) < E2 or ((b-a)/2) < E1:
                print("\nResultado final:")
                print(f"\tNúmero de iterações: {i}\n\tx = {x}\n\tf(x) = {fx}")
                break
            
            # A raiz está no novo intervalo [a, x]:
            if fa * fx < 0:
                b = x
                fb = fx

            # A raiz está no novo intervalo [b, x]
            else:
                a = x
                fa = fx

            i += 1 # atualiza para a próxima iteração


# Método de Newton-Raphson:
def newton_raphson(f, derivada, x0):
    pass


# Método da Secante:
def secante():
    pass


# Constantes utilizadas:
MAX_ITERACOES = 50
E1 = 1e-5
E2 = 1e-7
