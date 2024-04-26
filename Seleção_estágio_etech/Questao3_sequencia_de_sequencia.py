# Definindo função para gerar N numeros
def generate_sequence(num):
    # Inicializando uma lista vazia para armazenar a sequência
    sequence = []

    # Inicializando uma variável acumuladora para acompanhar a contagem total
    total_count = 0
    # Guardando o antigo valor de total_count em uma variável auxiliar
    aux = total_count

    # Itera de 0 até N (inclusive)
    for i in range(num + 1):
        # Adiciona i cópias do valor i à lista sequence
        sequence.extend([i] * i)

        # Atualiza a contagem total
        total_count = total_count + i

    # criando uma variável para contar os dígitos da lista desde o zero:
    sequencia = (aux, *sequence)

    # Imprime a contagem total e a sequência
    print(f"Caso {num}: {len(sequencia)} números")
    print(aux, *sequence)

    # Imprime uma linha em branco
    print()


# Atribuição de entrada do valor de N
N = int(input("Digite um número: "))

if 0 <= N <= 200:
    generate_sequence(N)
else:
    print("Entrada inválida")
