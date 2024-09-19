from dbm import error

from actions import QuestionOne, QuestionThree, QuestionFour, QuestionTwo, QuestionFive


class MenuView:
    def __init__(self):
        pass

    def show_menu(self):
        print("Qual questão do desafio você deseja testar?")
        print("1. Sequência de Fibonacci.")
        print("2. Encontrar vogal 'a'.")
        print("3. Repetição de soma.")
        print("4. Lógica de sequências.")
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
                    question_one = QuestionOne(num=num)
                    question_one.validade_num()
                    question_one.check_fibonacci()
                    self.show_menu()
                    self.menu_option()
                case '2':
                    print('')
                    print('Esse é o programa da questão 2 em funcionamento!')
                    print('Esta parte do programa mostra quantas vogais "a" existem na string inserida!')
                    enter = input('Insira aqui uma string para verificar: ')
                    question_two = QuestionTwo(enter)
                    question_two.count_a_vowels()
                    self.show_menu()
                    self.menu_option()
                case '3':
                    question = QuestionThree()
                    question.result_three()
                    self.show_menu()
                    self.menu_option()
                case '4':
                    question = QuestionFour()
                    question.result_four()
                    self.show_menu()
                    self.menu_option()
                case '5':
                    question = QuestionFive()
                    question.result_five()
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

