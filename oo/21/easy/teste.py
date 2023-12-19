class Teste():
    def __init__(self, valor):
        self._x = valor

    def get_valor(self):
        # método getter paar retornar o valor do atributo x
        return self._x

    def set_valor(self, v):
        # método setter para atribuir um novo valor ao x
        self._x = v


teste = Teste(10)
print("Valor do objeto: ", teste.get_valor())

val = int(input("Digite um valor numérico: "))
teste.set_valor(val)
print("Valor do objeto apos atribução: ", teste.get_valor())
