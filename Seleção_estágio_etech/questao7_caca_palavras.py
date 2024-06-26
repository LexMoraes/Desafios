#tentativa 2: refatorando código no QPython

def procurar_palavras_na_matriz(matriz, palavras):
    M = len(matriz)  # Obtém o número de linhas da matriz
    P = len(matriz[0])  # Obtém o número de colunas da matriz

    # Verificando as palavras
    for word in palavras:
        word_lower = word.lower()  # Converte a palavra para minúsculas
        found = False  # Flag para indicar se a palavra foi encontrada
        # Verificar diagonal principal
        for i in range(min(M, P)):
            # Verifica se a palavra está na diagonal principal ou invertida
            if matriz[i][i].lower() == word_lower or matriz[i][i][::-1].lower() == word_lower:
                print(f"1 Palavra \"{word}\" na diagonal principal")
                found = True
                break
            # Verificar acima da diagonal principal
            elif i < M and i < P:
                for j in range(i + 1, M):
                    # Verifica se a palavra está acima da diagonal principal ou invertida
                    if matriz[j][i].lower() == word_lower or matriz[j][i][::-1].lower() == word_lower:
                        print(f"3 Palavra \"{word}\" acima da diagonal principal")
                        found = True
                        break
            # Verificar abaixo da diagonal principal
            elif i < M and i < P:
                for j in range(i + 1, P):
                    # Verifica se a palavra está abaixo da diagonal principal ou invertida
                    if matriz[i][j].lower() == word_lower or matriz[i][j][::-1].lower() == word_lower:
                        print(f"2 Palavra \"{word}\" abaixo da diagonal principal")
                        found = True
                        break
        # Se a palavra não foi encontrada, imprime que é inexistente
        if not found:
            print(f"4 Palavra \"{word}\" inexistente")


# Leitura da entrada

print("Digite um valor para 'N', 'M' e 'P' (separados por espaço) : ")
print("N: número de palavras para verificar.")
print("M: número de linhas do caça palavras.")
print("P: número de colunas do caça palavras.")
N, M, P = map(int, input().split())  # Lê três inteiros da entrada: N, M e P

print("Digite a quantidade de linhas a serem verifocadas no caça palavras: ")
# Criar a matriz lendo as próximas M linhas da entrada
matriz = [input().split() for _ in range(M)]

print("Digite palavras a serem pesquisadas entre as existentes no caça palavras:  ")
# Ler as palavras a serem procuradas, lendo as próximas N linhas da entrada
palavras = [input().strip() for _ in range(N)]

# Chamar a função para procurar as palavras na matriz
procurar_palavras_na_matriz(matriz, palavras)
