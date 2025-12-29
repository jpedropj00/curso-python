class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    @classmethod
    def pessoa_com_50(cls, idade, nome):
        return cls(nome, 50)

        