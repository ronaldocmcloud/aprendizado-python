class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo=0
        self.numero=numero
        self.titular=titular

    @property
    def get_saldo(self):
        return self.get_saldo

    def set_saldo(self, saldo):
        if (saldo<0):
            print("O saldo não pode ser negativo")
        else:
            self.get_saldo = saldo

    def saque(self, valor):
        if (self.saldo>=valor):
            self.saldo-=valor
            print("Saque realizado com sucesso")
        else:
            print("saldo insuficiente")

    def deposita(self,valor):
        self.saldo+=valor

    def extrato(self):
        print("Cliente: ",self.titular, "Saldo Atual: ",self.saldo)
