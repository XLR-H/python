class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} é {}.".format(self.__titular, self.__saldo))

    def deposito(self, valor):
        self.__saldo += valor
        print("Deposito de {} efetuado com sucesso, seu Saldo agora é {}.".format(valor, self.__saldo))

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saque(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("Saque de {} efetuado com sucesso, seu Saldo agora é {}.".format(valor, self.__saldo))
        else:
            print("O valor de {} ultrapassou o limite.".format(valor))


    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)
        print("Transferência de {} efetuado com sucesso.".format(valor))

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def cod_banco():
        return "001"