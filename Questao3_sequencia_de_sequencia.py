#Definindo função para gerar N numeros
def generate_sequence(N):
    # Inicializando uma lista vazia para armazenar a sequência
    sequence = []

    # Inicializando uma variável acumuladora para acompanhar a contagem total
    total_count = 0
    # Guardando o antigo valor de total_count em uma variável auxiliar
    aux = total_count

    # Itera de 0 até N (inclusive)
    for i in range(N + 1):
        # Adiciona i cópias do valor i à lista sequence
        sequence.extend([i] * i)

        # Atualiza a contagem total
        total_count += i

    # Imprime a contagem total e a sequência
    print(f"Caso {N}: {total_count} números")

    print(aux, *sequence)
    
    # Imprime uma linha em branco
    print()

# Atribuição do valor de N
N = int(input("Digite um número: "))

if 0 <= N <= 200:
    generate_sequence(N)
else:
    print("Entrada inválida")