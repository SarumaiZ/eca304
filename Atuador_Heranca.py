# Matheus Gonçalves Zaitune da Silva RA: 19.01247-0
# Gabriel Semitan RA: 19.00961-5

class Dispositivo():
    def __init__(self, nome):
        self.nome = nome

    def retornaID(self):
        return self.nome


class Atuador(Dispositivo):
    def __init__(self, nome, estado):
        super().__init__(nome)
        if estado >= 1:
            self.estado = 1
        if estado <= 0:
            self.estado = 0

    def exibeEstado(self):
        if self.estado == 0:
            print("Nome: {0} Estado: Desligado".format(self.nome))
        else:
            print("Nome: {0} Estado: Ligado".format(self.nome))


class LED(Atuador):
    def __init__(self, nome, estado):
        super().__init__(nome, estado)

    def liga(self):
        self.estado = 1

    def desliga(self):
        self.estado = 0


class motor(Atuador):
    def __init__(self, nome, estado):
        super().__init__(nome, estado)

    def atribuiDirecao(self, dir):
        self.direcao = dir

    def atribuiVelocidade(self, vel):
        if vel > 255:
            self.velocidade = 255
            self.estado = 1
        elif vel <= 0:
            self.velocidade = 0
            self.estado = 0
        else:
            self.velocidade = vel
            self.estado = 1

    def exibeEstado(self):
        if self.estado == 0:
            print("Nome: {0} Estado: Desligado".format(self.nome))
        else:
            if self.direcao == 0:
                print("Nome: {0} Estado: Ligado Direcao: Anti-Horário Velocidade: {1}".format(
                    self.nome, self.velocidade))
            else:
                print("Nome: {0} Estado: Ligado Direcao: Horário Velocidade: {1}".format(
                    self.nome, self.velocidade))


M1 = motor("Máquina do Prazer", 0)
L1 = LED("Lampada", 4)

L1.exibeEstado()
L1.desliga()
L1.exibeEstado()

M1.exibeEstado()
M1.atribuiVelocidade(100)
M1.atribuiDirecao(0)
M1.exibeEstado()
M1.atribuiVelocidade(300)
M1.exibeEstado()
