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
            if abs(((b-a)/2)) < E1 or abs(fx) < E2:
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
            print(f"O valor da derivada da função no ponto é 0!\n")
            break

        # Imprindo a iteração atual:
        print(f"\nIteração {i}:")
        print(f"\tx = {x}\n\tf(x) = {fx}\n\tValor absoluto do delta_x = {abs(delta_x)}")

        # Verifica as condições de parada:
        if abs(delta_x) < E1 or abs(fx) < E2:
            break

        x = x + delta_x # obtém o valor do próximo x
        i += 1 # atualiza para a próxima iteração


# Método da Secante:
def secante(f, x0, x1):
    print("\n=========== Método da Secante ===========")

    i = 1
    # Enquanto o número máximo de iterações não for atingido:
    while i <= MAX_ITERACOES:
        fx0 = f(x0) # fx_n-1
        fx1 = f(x1) # fxn

        # Se o denominador fxn - fx_n-1 em um ponto for 0, o algoritmo se encerra:
        try:
            delta_x = -(fx1 * ((x1 - x0) / (fx1 - fx0)))
        except ZeroDivisionError:
            print(f"O valor de fxn - fx_n-1 no ponto é 0!\n")
            break

        x = x1 + delta_x # obtém o valor do x_n+
        fx = f(x)

        # Imprindo a iteração atual:
        print(f"\nIteração {i}:")
        print(f"\tx_n-1 = {x0}\n\txn = {x1}\n\tx_n+1 = {x}\n\tf(x) = {fx}\n\tValor absoluto do delta_x = {abs(delta_x)}")

        # Verifica as condições de parada:
        if abs(delta_x) < E1 or abs(fx) < E2:
            break

        # Atualizando os próximos valores:
        x0 = x1
        x1 = x

        i += 1 # atualiza para a próxima iteração

# Constantes utilizadas:
MAX_ITERACOES = 50
E1 = 1e-5
E2 = 1e-7

# Obtendo os resultados finais:

# Método da Bisseção:
bissecao(func1, 1, 2)
bissecao(func2, -2, -1)

# Método de Newton-Rapshon:
newton_raphson(func1, derivada1, 1)
newton_raphson(func2, derivada2, -2)

# Método da Secante:
secante(func1, 1, 1.5)
secante(func2, -2, -1.5)