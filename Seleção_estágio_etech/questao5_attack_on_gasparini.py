def calcular_muralhas_necessarias(n, x, titans, p, m, g):
    muralhas_necessarias = 0
    alturas_muralhas = [0, 0, 0]  # Inicializa a altura das muralhas para cada tipo de titã

    for titan in titans.split(' '):
        if titan.upper() == 'P':
            if alturas_muralhas[0] < p:
                muralhas_necessarias += 1
                alturas_muralhas[0] = p
            else:
                alturas_muralhas[0] -= p
        elif titan.upper() == 'M':
            if alturas_muralhas[1] < m:
                muralhas_necessarias += 1
                alturas_muralhas[1] = m
            else:
                alturas_muralhas[1] -= m
        elif titan.upper() == 'G':
            if alturas_muralhas[2] < g:
                muralhas_necessarias += 1
                alturas_muralhas[2] = g
            else:
                alturas_muralhas[2] -= g
        else:
            raise ValueError(f'Tipo de titã inválido: {titan}')

    return muralhas_necessarias

# Entrada de dados
n, x = map(int, input("Digite a quantidade de titãs e o tamanho das muralhas (separados por espaço): ").split())
titans = input("Digite os tamanhos dos titãs (P, M ou G), separados por espaço: ")
p, m, g = map(int, input("Digite as alturas dos titãs pequenos, médios e grandes (separados por espaço): ").split())

# Chama a função para calcular as muralhas necessárias
resultado = calcular_muralhas_necessarias(n, x, titans, p, m, g)
print("O número mínimo de muralhas necessárias para parar os titãs é:",resultado)