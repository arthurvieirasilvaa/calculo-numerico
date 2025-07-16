import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return y + np.exp(2*t) + np.sin(t) + np.cos(t)


def y_exata(t):
    return np.exp(2*t) - np.cos(t)


def euler_simpes(f, t0, y0, tf, n):
    h = (tf - t0) / n
    y = np.zeros(n+1)
    t = np.zeros(n+1)

    y[0] = y0
    t[0] = t0
    for i in range(1, n+1):
        y[i] = y[i-1] + h * f(t[i-1], y[i-1])
        t[i] = t[i-1] + h   
    
    return y, t


def euler_melhorado(f, t0, y0, tf, n):
    h = (tf - t0) / n
    y = np.zeros(n+1)
    t = np.zeros(n+1)

    y[0] = y0
    t[0] = t0
    for i in range(1, n+1):
        y_previsao = y[i-1] + h * f(t[i-1], y[i-1])
        y[i] = y[i-1] + (h/2) * (f(t[i-1], y[i-1]) + f(t[i-1]+h, y_previsao))
        t[i] = t[i-1] + h
    
    return y, t


def plotar_grafico(y, t, titulo, alternativa):
    t_plot = np.linspace(0, 2, 200)
    y_plot = y_exata(t_plot)

    plt.figure(figsize=(10,6))
    
    plt.plot(t_plot, y_plot, 'bo--', label='Solução Exata', linewidth=2, markersize=5)
    plt.plot(t, y, 'ro--', label=titulo, linewidth=2, markersize=5)
    plt.xlabel('t')
    plt.ylabel('y(t)')
    
    plt.title(f'Comparação: {titulo} x Solução Exata')
    plt.legend()
    
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(f"grafico_{alternativa}")
    plt.show()


# Valores utilizados nos Métodos de Euler:
t0 = 0
y0 = 0
tf = 2

# a) Método de Euler Simples com 16 passos (subintervalos):
print("\n========= Método de Euler Simples (16 passos) =========\n")
ya, ta = euler_simpes(f, t0, y0, tf, 16)
print(f"t = {ta}\n y = {ya}")

# b) Método de Euler Melhorado com 8 passos:
print("\n========= Método de Euler Melhorado (8 passos) =========\n")
yb, tb = euler_melhorado(f, t0, y0, tf, 8)
print(f"t = {tb}\n y = {yb}")

# c) Método de Euler Simples com 64 passos (subintervalos):
print("\n========= Método de Euler Simples (64 passos) =========\n")
yc, tc = euler_simpes(f, t0, y0, tf, 64)
print(f"t = {tc}\n y = {yc}")

# d) Método de Euler Melhorado com 32 passos:
print("\n========= Método de Euler Melhorado (32 passos) =========\n")
yd, td = euler_melhorado(f, t0, y0, tf, 32)
print(f"t = {td}\n y = {yd}")

valor_exato = y_exata(tf)
print(f"\nValor exato de y(2) = {valor_exato}")

plotar_grafico(ya, ta, "Método de Euler Simples com 16 passos", "a")
plotar_grafico(yb, tb, "Método de Euler Melhorado com 8 passos", "b")
plotar_grafico(yc, tc, "Método de Euler Simples com 64 passos", "c")
plotar_grafico(yd, td, "Método de Euler Melhorado com 32 passos", "d")
