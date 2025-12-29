from datetime import datetime
import json

CAMINHO_ARQUIVO = 'exercicios\\atividades\\at5.json'
class Pessoa:
    ano_atual = datetime.now().year
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_nascimento = self.get_ano_nascimento()
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
p1 = Pessoa(
    nome=input('Digite seu nome: '),
    idade=int(input('Digite sua idade: '))
)

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(vars(p1), arquivo, ensure_ascii=False, indent=2,)

        