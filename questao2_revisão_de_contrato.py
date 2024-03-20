def valor_contrato():

    while True:

        # Atribuindo valores a entrada das variáveis
        d, n = map(int( input("Informe o dígito ruim e o valor negociado em contrato (separados por espaço)".split())))

        # iniciando bloco de laço
        if d == 0 and n == 0:
            break

        # Inicializa o resultado
        resultado = 0
        produto = 1

        # Processando cada dígito do número
        while n > 0:
            digito = n % 10
            if digito != d:
                resultado += digito * produto
                produto *= 10
            n //= 10

        # Imprime o resultado
        print(resultado)


if __name__ == "__valor_contrato__":
    valor_contrato(resultado)
