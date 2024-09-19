from view import *


# Módulo para desenvolver a lógica e chamadas entre todas as questões do teste.


# Classe para trabalhar a lógica da questão 1 - sequência de Fibonacci.
class FibonacciActions:
    def __init__(self, num):
        self.fib_sequence = [0, 1]
        self.num = num

    def validade_num(self):
        while True:
            try:
                self.num = int(self.num)
                break
            except ValueError:
                print("O valor informado não é um número inteiro.")
                num = input("Insira o valor novamente aqui: ")
                self.num = num
                self.validade_num()
            return
        return self.num

    def fibonacci(self, num):
        while self.fib_sequence[-1] < num:
            self.fib_sequence.append(self.fib_sequence[-1] + self.fib_sequence[-2])
        return self.fib_sequence

    def check_fibonacci(self):
        self.fibonacci(self.num)
        if self.num in self.fib_sequence:
            print(f"O número {self.num} existe na sequência de Fibonacci.")
            print("Sequência até o número informado:", self.fib_sequence)
        else:
            print(f"O número {self.num} não existe na sequência de Fibonacci.")

class QuestionTwo:
    def __init__(self, input_string):
        self.input_string = input_string
        self.count = None

    def count_a_vowels(self):
        input_string = self.input_string
        # Converte a string para minúsculas para facilitar a contagem
        input_string = input_string.lower()
        # Conta o número de ocorrências da vogal 'a'
        count = input_string.count('a')
        print(f'Existem {count} vogais "a" na string')
        return


class QuestionThree:
    def __init__(self):
        pass

    def result_three(self):
        print('''3) Observe o trecho de código abaixo: int INDICE = 12,\n SOMA = 0, K = 1; enquanto K < INDICE \nfaça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
        ''')
        indice = 12
        soma = 0
        k = 1
        while k < indice:
            k = k + 1
            soma = soma + k
        print(f'O resultado da soma [e: {soma}')


class QuestionFour:
    def __init__(self):
        pass
    def result_four(self):
        print('4) Resposta(R):')
        print('')
        print('Progressão aritmética de 2.')
        print('a) 1, 3, 5, 7, ___. R: 9')
        print('')
        print('Progressão geométrica de 2.')
        print('b) 2, 4, 8, 16, 32, 64, ___. R: 128')
        print('')
        print('Quadrados perfeitos')
        print('c) 0, 1, 4, 9, 16, 25, 36, ___. R:')
        print('')
        print('Quadrados perfeitos, apenas pares, iniciando com 2²')
        print('d) 4, 16, 36, 64, ___. R:')
        print('')
        print('Encadeamento do próximo valor = atual + anterior (Fibonacci)')
        print('e) 1, 1, 2, 3, 5, 8, ___. R: 13')
        print('')
        print('Após o 16, é necessário abstrair os valores anteriores, considerando progressão é de 1, em 1')
        print('f) 2,10, 12, 16, 17, 18, 19, ___. R: 20')

