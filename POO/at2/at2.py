from pathlib import Path

BASE_DIR = Path(__file__).parent
LOG_FILE = BASE_DIR / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg}: ({self.__class__.__name__})'
        print('Salvando no log...')
        with open(LOG_FILE, 'a', encoding='utf-8') as arquivo:
            arquivo.write(msg_formatada + '\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg}: ({self.__class__.__name__})')


if __name__ == '__main__':
    log_arquivo = LogFileMixin()
    log_arquivo.log_error('Olá Mundo')
    log_arquivo.log_success('OI')

    log_tela = LogPrintMixin()
    log_tela.log_error('Erro na tela')
