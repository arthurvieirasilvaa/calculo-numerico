import numpy as np
import warnings

warnings.filterwarnings("ignore") # ingnora o warning de overflow no cast da terceira variável

# Primeiro número:
x = np.float64(5.21)
y = np.float32(x)

erro_relativo = abs((y-x) / y) 
precisao = int(abs(np.log10(erro_relativo)))

print("a)")
print(f"\tX = {x}")
print(f"\tY = {y}")
print(f"\tPrecisão: {precisao} dígitos")

# Segundo número:
x = np.float64(35 * pow(10, -95))
y = np.float32(x)

erro_relativo = abs(y-x) / abs(y) 
try:
    precisao = int(abs(np.log10(erro_relativo)))
except OverflowError:
    precisao = 0

print("b)")
print(f"\tX = {x}")
print(f"\tY = {y}")
print(f"\tPrecisão: {precisao} dígitos")
print("\tOcorreu um Underflow!")

# Terceiro número
x = np.float64(47.5 * pow(10, 112))
y = np.float32(x)

erro_relativo = abs(y-x) / abs(y)
try:
    precisao = int(abs(np.log10(erro_relativo)))
except ValueError:
    precisao = 0

print("c)")
print(f"\tX = {x}")
print(f"\tY = {y}")
print(f"\tPrecisão: {precisao} dígitos")
print("\tOcorreu um Overflow!")