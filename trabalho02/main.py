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

    print("\n=========== Método da Bisseção ===========")

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
            print(f"\nIteração {i}:")
            print(f"\tIntervalo [{a}, {b}]\n\tx = {x}\n\tf(x) = {fx}")

            # Verifica as condições de parada:
            if ((b-a)/2) < E1 or abs(fx) < E2:
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
    x = x0

    print("\n=========== Método de Newton-Rapshon ===========")

    i = 1
    # Enquanto o número máximo de iterações não for atingido:
    while i <= MAX_ITERACOES:
        fx = f(x)
        f_linha = derivada(x) # obtém a derivada da função no ponto x
        
        # Se a derivada da função em um ponto for 0, o algoritmo se encerra:
        try:
            delta_x = -fx/f_linha 
        except ZeroDivisionError:
            print(f"O valor da derivada da função no ponto {x} é 0!\n")
            break

        # Imprindo a iteração atual:
        print(f"\nIteração {i}:")
        print(f"\tx = {x}\n\tf(x) = {fx}\n\tValor absoluto do delta_x = {delta_x}")

        # Verifica as condições de parada:
        if abs(delta_x) < E1 or abs(fx) < E2:
            break

        x = x + delta_x # obtém o valor do próximo x
        i += 1 # atualiza para a próxima iteração


# Método da Secante:
def secante():
    pass


# Constantes utilizadas:
MAX_ITERACOES = 50
E1 = 1e-5
E2 = 1e-7
