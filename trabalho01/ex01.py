numeros_binarios = ['0.1100001010001001', '110000.1010001001', '110110110.0101001', 
                    '1100100111111011.00', '0.00000000000001000111110101010']
numeros_decimais = []

for num_binario in numeros_binarios:
    # Dividindo as partes fracionária e inteira do número binário:
    partes = num_binario.split('.')
    inteira = partes[0]
    fracionaria = partes[1]

    num_inteiro = 0
    # Convertendo a parte inteira:
    for i in range(len(inteira)):
        num_inteiro += int(inteira[i]) * pow(2, len(inteira)-i-1)
    

    num_fracionaria = 0
    # Convertendo a parte fracionária:
    for i in range(len(fracionaria)):
        num_fracionaria += int(fracionaria[i]) * pow(2, -(i+1))

    num_inteiro = str(num_inteiro)
    num_fracionaria = str(num_fracionaria)
    num_fracionaria = num_fracionaria.replace('.', '')

    numeros_decimais.append(num_inteiro + "." + num_fracionaria)

for i in range(len(numeros_decimais)):
    print(f"{numeros_binarios[i]} = {numeros_decimais[i]}")
