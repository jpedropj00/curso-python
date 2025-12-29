class Carro:
    def __init__(self, nome):
        self._nome = nome
        self._motor = None
        self._fabricante = None
    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    @property
    def fabricante(self):
        return self._fabricante
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

c1 = Carro('HB20')
f1 = Fabricante('Volkswagen')
m1 = Motor('1.0')
c1.fabricante = f1
c1.motor = m1

        