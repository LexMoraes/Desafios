#Definindo função para comprimir string
def compress_string(entrada):
    comprimir = ''  # String comprimida que será construída
    current_char = entrada[0]  # Caractere atual sendo processado
    count = 1  # Contador de repetições do caractere atual

    # Percorre a string de entrada, começando do segundo caractere
    for i in range(1, len(entrada)):
        # Se o caractere atual for igual ao caractere anterior
        if entrada[i] == current_char:
            count += 1  # Incrementa o contador de repetições
        else:
            # Se o caractere atual for diferente do anterior
            # Adiciona a substring comprimida à string comprimida final
            compressed += compress_substring(current_char, count)
            # Atualiza o caractere atual e reinicia o contador de repetições
            current_char = entrada[i]
            count = 1

    # Adiciona a última substring comprimida à string comprimida final
    compressed += compress_substring(current_char, count)

    return compressed  # Retorna a string comprimida


def compress_substring(char, count):
    if count == 1:
        return char  # Retorna o caractere se ele não se repetir
    elif count == 2:
        return char * 2  # Retorna o caractere repetido duas vezes
    else:
        return f"[{char}]{count}"  # Retorna a substring comprimida


# Casos de teste
test_cases = [
    'I_am_WhatWhat_is_WhatWhat',
    # Adicione mais casos de teste aqui
]

# Testa a função de compressão para cada caso de teste
for index, input_str in enumerate(test_cases):
    print(f"Caso {index + 1}:")
    print(f"String original: {input_str}")
    print(f"String comprimida: {compress_string(input_str)}")
    print("------------------------------------")