#Definindo função para descriptografia de entrada
def descriptografar(mensagem):
    #Parte 1 - Deslocando os caracteres da metade em diante da mensagem
    metade = len(mensagem) // 2
    mensagem = list(mensagem)
    for i in range(metade, len(mensagem)):
        troca = mensagem[i]
        if troca.isalpha():
            mensagem[i] = chr(ord(troca) - 1)

    #Parte 2 - Invertendo linha
    mensagem = ''.join(reversed(mensagem))

    #Parte 3 - Deslocando letras
    resultado = []
    for troca in mensagem:
        if troca.isalpha():
            resultado.append(chr(ord(troca) - 3))
        else:
            resultado.append(troca)

    return ''.join(resultado)

# Atribuindo entrada
entrada = input("Digite o texto criptografado: ")
print("Texto descriptografado:", descriptografar(entrada))