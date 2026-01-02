from at2 import LogPrintMixin
class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False #Está ligado
    def ligar(self):
        if not self._ligado:
            self._ligado = True
            print('Ligando...')
        else:
            print('Já está ligado')
    def desligar(self):
        if self._ligado:
            self._ligado = False
            print('Desligando...')
        else:
            print('Já está desligado')
class Celular(Eletronico, LogPrintMixin):
    def ligar(self):
        if self._ligado:
            self.log_error(f'O celular {self._nome} já está ligado')
            return
        
        super().ligar()
        if self._ligado:
            self.log_success(f'O celular {self._nome} foi ligado com sucesso')
            msg = f'O celular {self._nome} já está ligado'
            self.log_success(msg)
        
    def desligar(self):
        if not self._ligado:
            self.log_success(f'O celular {self._nome} foi desligado com sucesso')
            return
        super().desligar()
        if not self._ligado:
            self.log_error(f'O celular {self._nome} já está desligado')
            msg = f'O celular {self._nome} já está desligado'
            self.log_error(msg)
    