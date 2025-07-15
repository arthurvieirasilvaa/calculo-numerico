import numpy as np

def f(t, y):
    return y + np.exp(2*t) + np.sin(t) + np.cos(t)


def euler_simpes(f, t0, x0, tf, n):
    h = (tf - t0) / n
    x = np.zeros(n)
    t = np.zeros(n)

    x[0] = x0
    t[0] = t0
    for i in range(1, n):
        x[i] = x[i-1] + h * f(t[i-1], x[i-1])
        t[i] = t[i-1] + h   
    
    return x, t


