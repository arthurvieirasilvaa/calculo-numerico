import numpy as np

# Armazenando os valores nas variáveis de 32 bits:
x32 = np.float32(1/5)
y32 = np.float32(0.19999)

print("Valor aproximado (32 bits):")
print(f"\tx = {x32}")
print(f"\ty = {y32}")

# Armazenando os valores nas variáveis de 64 bits:
x64 = np.float64(1/5)
y64 = np.float64(0.19999)

print("Valor real (64 bits):")
print(f"\tx = {x64}")
print(f"\ty = {y64}")

# a)
print("\na)")
soma32 = x32 + y32
soma64 = x64 + y64

print(f"\t(32 bits): x + y = {soma32}")
print(f"\t(64 bits): x + y = {soma64}")

erro_abs = abs(soma64 - soma32)
erro_rel = erro_abs / abs(soma64)

print(f"\tErro absoluto = {erro_abs}")
print(f"\tErro relativo = {erro_rel}")

# b)
print("\nb)")
dif32 = x32 - y32
dif64 = x64 - y64

print(f"\t(32 bits): x - y = {dif32}")
print(f"\t(64 bits): x - y = {dif64}")

erro_abs = abs(dif64 - dif32)
erro_rel = erro_abs / abs(dif64)

print(f"\tErro absoluto = {erro_abs}")
print(f"\tErro relativo = {erro_rel}")

# c)
print("\nc)")
mult32 = x32 * y32
mult64 = x64 * y64

print(f"\t(32 bits): x * y = {mult32}")
print(f"\t(64 bits): x * y = {mult64}")

erro_abs = abs(mult64 - mult32)
erro_rel = erro_abs / abs(mult64)

print(f"\tErro absoluto = {erro_abs}")
print(f"\tErro relativo = {erro_rel}")

# d)
print("\nd)")
div32 = x32 / y32
div64 = x64 / y64

print(f"\t(32 bits): x / y = {div32}")
print(f"\t(64 bits): x / y = {div64}")

erro_abs = abs(div64 - div32)
erro_rel = erro_abs / abs(div64)

print(f"\tErro absoluto = {erro_abs}")
print(f"\tErro relativo = {erro_rel}")
