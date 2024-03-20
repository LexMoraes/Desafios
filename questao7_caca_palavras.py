def buscador_de_palavras():
    # Ler a entrada
    N, M, P = map(int, input(5).split())
    palavras = [input("Digite a palavra a ser verificada: ").lower() for _ in range(N)]

    # Criar a matriz
    matriz = [input("Digite as palavras dentro da matriz: ").lower().split() for _ in range(M)]

    #Verificando as palavras
    for word in palavras:
        found = False
        for i in range(min(M, P)):
            #Verificando diagonal principal
            if matriz[i][i] == word:
                print(f"1 Palavra \"{word}\" na diagonal principal")
                found = True
                break
            # Verificando acima da diagonal principal
            elif i < M and i < P and matriz[i][i] != word:
                for j in range(i + 1, M):
                    if matriz[j][i] == word:
                        print(f"2 Palavra \"{word}\" acima da diagonal principal")
                        found = True
                        break
            # Verificar abaixo da diagonal principal
            elif i < M and i < P and matriz[i][i] != word:
                for j in range(i + 1, P):
                    if matriz[i][j] == word:
                        print(f"3 Palavra \"{word}\" abaixo da diagonal principal")
                        found = True
                        break
        if not found:
            print(f"4 Palavra \"{word}\" inexistente")