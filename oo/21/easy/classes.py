import random


class Jogadores():
    def __init__(self, nome, idade, cartas):
        self.__nome = nome
        self.__idade = idade
        self.__fichas = 0
        self.__cartas = cartas

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_fichas(self):
        return self.__fichas

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def set_fichas(self, ficha):
        self.__fichas = ficha


class Jogo():
    def __init__(self, baralho, cartas_jogadas):
        self.__cartas_jogadas [] = None
        self.__baralho = baralho[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.__az = 1
        self.__queen = 10
        self.__king = 10
        self.__j = 10

    def cartas(self):
        self.__cartas_jogadas = []

    def distribuir_cartas(self, cartas):
        random_cards = random.randint(1, 10)

    def regras(self):
        print("REGRAS BLACKJACK GAME!")

    def menu(self):
        print("Bem vindo ao nosso BlackJack Game.")
        print("Escolha uma das opções:\n "
              "[1] Jogar | [2] Regras\n"
              "[3] Sair")
        opcao = int(input("Digite a opção desejada:"))
        match opcao:
            case 1:
                jogo = Jogo()
                print(jogo)
            case 2:
                print(self.regras())
            case 3:
                print("Saindo do jogo.")
                exit()

        jogadoresJogando = int(input("Quantos jogadores vão jogar: "))
        for i in range(jogadoresJogando):
            nome = input(f"Jogador {i + 1}, qual seu nome?")
            idade = int(input(f"Jogador {nome}, qual sua idade?"))
            print(f'Dados do jogador {i + 1}:\n'
                  f'Nome: {nome}\n'
                  f'Idade: {idade}\n'
                  f'Cartas: ')  # Cartas}\n')


print(Jogo())
