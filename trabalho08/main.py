import numpy as np

def f(t, y):
    return y + np.exp(2*t) + np.sin(t) + np.cos(t)


def euler_simpes(f, t0, y0, tf, n):
    h = (tf - t0) / n
    y = np.zeros(n)
    t = np.zeros(n)

    y[0] = y0
    t[0] = t0
    for i in range(1, n):
        y[i] = y[i-1] + h * f(t[i-1], y[i-1])
        t[i] = t[i-1] + h   
    
    return y, t


def euler_melhorado(f, t0, y0, tf, n):
    h = (tf - t0) / n
    y = np.zeros(n)
    t = np.zeros(n)

    y[0] = y0
    t[0] = t0
    for i in range(1, n):
        y_previsao = y[i-1] + h * f(t[i-1], y[i-1])
        y[i] = y[i-1] + (h/2) * (f(t[i-1], y[i-1]) + f(t[i-1]+h, y_previsao))
        t[i] = t[i-1] + h
    
    return y, t


# Valores utilizados nos Métodos de Euler:
t0 = 0
y0 = 0
tf = 2

# a) Método de Euler Simples com 16 passos (subintervalos):
print("\n========= Método de Euler Simples =========\n")
ya, ta = euler_simpes(f, t0, y0, tf, 16)
print(f"t = {ta}\n y = {ya}")

# b) Método de Euler Melhorado com 8 passos:
print("\n========= Método de Euler Melhorado =========\n")
yb, tb = euler_melhorado(f, t0, y0, tf, 8)
print(f"t = {tb}\n y = {yb}")

# c) Método de Euler Simples com 64 passos (subintervalos):
print("\n========= Método de Euler Simples =========\n")
yc, tc = euler_simpes(f, t0, y0, tf, 64)
print(f"t = {tc}\n y = {yc}")

# d) Método de Euler Melhorado com 32 passos:
print("\n========= Método de Euler Melhorado =========\n")
yd, td = euler_melhorado(f, t0, y0, tf, 32)
print(f"t = {td}\n y = {yd}")

valor_exato = np.exp(2*tf) - np.cos(tf)
print(f"\nValor exato de x(4) = {valor_exato}")