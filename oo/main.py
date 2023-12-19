def cria_conta(numero, titular, saldo, limite):
    conta = {
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite
    }
    return conta


def depositar(conta, valor):
    conta["saldo"] += valor


def sacar(conta, valor):
    conta["saldo"] -= valor


def imprimir_extrato(conta):
    print("Seu saldo é de {}".format(conta["saldo"]))


conta_1 = {
    "numero": 123,
    "titular": "Clebinho",
    "saldo: ": -10000,
    "limite: ": 1000
}

conta_2 = {
    "numero": 456,
    "titular": "Beltrana",
    "saldo: ": 9999,
    "limite: ": 1000
}

conta_3 = cria_conta(879, "Ciclana", 5000, 10000)

print("Conta 1: ", conta_1)
print("Conta 2: ", conta_2)
print("Conta 3: ", conta_3)

depositar(conta_3, 1000)  # antes: 5000 depois: 6000
print(conta_3["saldo"])
sacar(conta_3, 2000)  # antes: 6000 depois: 4000
print(conta_3["saldo"])
imprimir_extrato(conta_3)
