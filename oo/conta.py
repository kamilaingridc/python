class Conta():  # cria uma classe sempre com maiúscula
    # função construtora
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__poupanca = 0

    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def get_titular(self):
        return self.__titular

    def set_limite(self, valor):
        self.__limite = valor

    def imprimir_extrato(self):
        print("Saldo R${},00 do titular {}.".format(self.get_saldo(), self.get_titular()))
        # a chave é subtituida pelo valor colocado em format

    @property
    def poupanca(self):
        return self.__poupanca

    @poupanca.setter
    def poupanca(self, valor):
        if valor <= 0:
            print("Infelizmente não é possível poupar um valor negativo.")
        else:
            self.__poupanca = valor

    def __verificar_saque(self, valor):
        if valor <(self.__saldo + self.__limite):
            return True
        else:
            return False

    def sacar(self, valor):
        if self.__verificar_saque(valor):
            self.__saldo -= valor
        else:
            print("Infelizmente você não possui saldo e limite para o saque em questão.")


conta_clebinho = Conta(123, "Clebinho", -10000, 100)  # cria nova conta com novos parametros
conta_beltrana = Conta(456, "Beltrana", 5000, 1000)

print("Valor da poupança: ", conta_clebinho.poupanca)
conta_clebinho.poupanca = 10
print("Valor da poupança: ", conta_clebinho.poupanca)

conta_beltrana.sacar(1)

conta_clebinho.depositar(10000)  # antes -10000 depois: 0
conta_clebinho.imprimir_extrato()

conta_beltrana.sacar(1000)  # antes: 5000 depois: 4000
conta_beltrana.imprimir_extrato()

conta_clebinho.transferir(conta_beltrana, 1000)
conta_clebinho.imprimir_extrato()  # antes 0 depois -1000
conta_beltrana.imprimir_extrato()  # antes 4000 depois 5000

conta_clebinho.set_limite(9999)
print(conta_clebinho.get_limite())

# conta_clebinho._Conta__saldo = 1000
# print(conta_clebinho._Conta__saldo)
