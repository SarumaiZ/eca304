#Matheus Gonçalves Zaitune da Silva RA: 19.01247-0
#Gabriel Semitan RA: 19.00961-5

class cliente():
    def __init__(self, nome = "", CPF = ""):
        self.nome = nome
        self.__CPF = CPF
        self.__saldo = 0
        self.__limite = 1000
    def exibeCPF(self):
        print("\nCPF: %s\n" %self.__CPF)
    def exibeSaldo(self):
        if self.__saldo < 0:
            print("\nSeu saldo é: %i"%self.__saldo)
            print("Seu limite é: %i\n" %self.__limite)
        else:
            print("\nSeu saldo é: %i\n"%self.__saldo)
    def deposito(self, valor):
        self.__saldo+=valor
    def pagamento(self, valor):
        if self.__saldo>=0:
            total = self.__limite+self.__saldo
        else:
            total = self.__limite
        if (total>=valor):
            if self.__saldo<valor:
                if self.__saldo<=0:
                    self.__saldo-=valor
                    self.__limite-=valor
                    print("Você está usando o seu limite\n")
                else: 
                    dif = self.__saldo-valor
                    self.__saldo-=valor
                    self.__limite+=dif
                    print("Você entrou no limite\n")
            else:
                self.__saldo-=valor
        else:
            print("\nErro: dinheiro insuficiente\n")

p = cliente("Oswaldo", "512.067.778-22")
p.exibeCPF()
p.exibeSaldo()
p.deposito(500)
p.exibeSaldo()
p.pagamento(400)
p.exibeSaldo()
p.pagamento(300)
p.exibeSaldo()
p.pagamento(500)
p.exibeSaldo()
p.pagamento(300)
p.exibeSaldo()
p.pagamento(100)
p.deposito(1000)
p.exibeSaldo()
p.pagamento(1000)