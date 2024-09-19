from dbm import error

from actions import FibonacciActions, QuestionThree, QuestionFour, QuestionTwo


class MenuView:
    def __init__(self):
        pass

    def show_menu(self):
        print("Qual questão do desafio você deseja testar?")
        print("1. Sequência de Fibonacci.")
        print("2. Contagem da vogal 'a'.")
        print("3. Laço de repetição.")
        print("4. Descubra a lógica e complete.")
        print("5. Enígma da lâmpada.")
        print("0. Sair do programa.")

    def menu_option(self):
        self.option = input("Escolha um número do menu: ").strip()
        while self.option != 0:
            match self.option:
                case '1':
                    print('')
                    print('Esse é o programa da questão 1 em funcionamento!')
                    print('Esta parte do programa deduz se o número informado faz parte da sequência de Fibonacci!')
                    print('Insira um número para verificar a existência na sequência de Fibonacci!')
                    num = input('Insira aqui: ')
                    question_one = FibonacciActions(num=num)
                    question_one.validade_num()
                    question_one.check_fibonacci()
                    print('')
                    self.show_menu()
                    self.menu_option()
                case '2':
                    print('')
                    print('Esse é o programa da questão 2 em funcionamento!')
                    print('Esta parte do programa mostra quantas vogais "a" existem na string inserida!')
                    enter = input('Insira aqui uma string para verificar: ')
                    question_two = QuestionTwo(enter)
                    question_two.count_a_vowels()
                    print('')
                    self.show_menu()
                    self.menu_option()
                case '3':
                    question = QuestionThree()
                    question.result_three()
                    print('')
                    self.show_menu()
                    self.menu_option()
                case '4':
                    question = QuestionFour()
                    question.result_four()
                    print('')
                    self.show_menu()
                    self.menu_option()
                case '5':
                    print('5) Resposta:')
                    print('Passo 1 - Ativar um dos interruptores')
                    print('Passo 2 - Aguardar alguns minutos.')
                    print('Passo 3 - Desligar o interruptor ativado')
                    print('Passo 4 - Ativar outro interruptor.')
                    print('Passo 5 - Checar as salas para verificar as lâmpadas: quente, fria e ligada')
                    print('A lâmpada mais quente; primeiro interruptor ativado.')
                    print('A lâmpada mais fria; interruptor que não foi ativado.')
                    print('A lâmpada ligada; último interruptor ativado.')
                    print('')
                    self.show_menu()
                    self.menu_option()
                case '0':
                    print("Saindo do programa...")
                    return
                case _:
                    print('')
                    print("!ERROR! - Escolha inválida")
                    print('')
                    self.show_menu()
                    self.menu_option()
                    return
            break

