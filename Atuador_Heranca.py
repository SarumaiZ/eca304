class Dispositivo():
    def __init__(self, nome):
        self.nome = nome

    def retornaID(self):
        return self.nome


class Sensor(Dispositivo):
    def __init__(self, nome, dado=None):
        super().__init__(nome)
        self.dado = dado

    def enviaDado(self):
        from random import randrange
        self.dado = randrange(1023)
        return self.dado


class Microcontrolador(Dispositivo):
    def __init__(self, nome):
        super().__init__(nome)
        self.dadosSensores = dict()
        self.dadosAtuadores = dict()

    def recebeDado(self, nomeSensor, valorSensor):
        self.dadosSensores[nomeSensor] = valorSensor

    def enviaDado(self, nomeAtuador, estado):
        self.dadosAtuadores[nomeAtuador] = estado
        return self.dadosAtuadores[nomeAtuador]

    def exibeInfo(self, tipo, nomeDispositivo):
        if tipo == "sensor":
            print("{0}: {1}".format(nomeDispositivo,
                  self.dadosSensores[nomeDispositivo]))
        if tipo == "atuador":
            print("{0}: {1}".format(nomeDispositivo,
                  self.dadosAtuadores[nomeDispositivo]))


sensor1 = Sensor("Ultrassom")
arduino = Microcontrolador("Arduino")
arduino.recebeDado(sensor1.retornaID(), sensor1.enviaDado())
arduino.exibeInfo("sensor", sensor1.retornaID())
sensor2 = Sensor("Sensor de Linha")
arduino.recebeDado(sensor2.retornaID(), sensor2.enviaDado())
arduino.exibeInfo("sensor", sensor2.retornaID())
