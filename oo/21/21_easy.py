import random
class Jogadores():
    def __init__(self, nome, idade, fichas, cartas):
        self.__nome = nome
        self.__idade = idade
        self.__fichas = fichas
        self.__cartas = cartas

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_fichas(self):
        return self.__fichas

class Jogo():
    def __init__(self, baralho, az, queen, king, j, cartas_jogadas):
        self.__cartas_jogadas = None
        self.__baralho = baralho[az, 2, 3, 4, 5, 6, 7, 8, 9, 10, queen, king, j]
        self.__az = 1
        self.__queen = 10
        self.__king = 10
        self.__j = 10

    def cartas(self):
        self.__cartas_jogadas = []

    def distribuir_cartas(self, cartas):
        random_cards = random.randint(1, 10)

    def menu(self):
        print("Bem vindo ao jogo 21.")
        print("Escolha uma das opções [1] Jogar | [2] Sair")
        opcao = int(input("Digite a opção desejada:"))
        match opcao:
            case 1:
                jogo = Jogo()
                print(jogo)
            case 2:
                print("Você saiu do jogo.")
                exit()
        jogadoresJogando = int(input("Quantos jogadores vão jogar: "))
        for i in range(jogadoresJogando):
            nome = input(f"Jogador {i+1}, qual seu nome?")
            idade = int(input(f"Jogador {nome}, qual sua idade?"))
            print(f'Dados do jogador {i+1}:\n'
                  f'Nome: {nome}\n'
                  f'Idade: {idade}\n'
                  f'Cartas: ') #Cartas}\n')


jogador1 = Jogadores('xuxu', 20, 500, [])
jogador2 = Jogadores('maçã', 25, 260, [])
Jogo()
