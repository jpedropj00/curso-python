def criar_funcao(funcao, *args):
    def interna(*args):
        return funcao(*args)
    return interna
def multiplicar(a,b):
    return a * b
def somar(a,b):
    return a + b
def dividir(a,b):
    return a / b
def subtrair(a,b):
    return a - b

try:
    num1 = float(input('Digite o primeiro número:'))
    num2 = float(input('Digite o segundo número: '))
except (ValueError, TypeError):
    print('Por favor, digite apenas número válidos.')
    exit()
multiplicacao = criar_funcao(multiplicar, num1, num2)
soma = (criar_funcao(somar, num1, num2))
divisao = (criar_funcao(dividir, num1, num2))
subtracao = (criar_funcao(subtrair, num1, num2))
print(f'A multiplicação entre {num1} e {num2} é: {multiplicacao(num1, num2)}')
print(f'A soma entre {num1} e {num2} é: {soma(num1, num2)}')
print(f'A divisão entre {num1} e {num2} é: {divisao(num1, num2):.2f}')
print(f'A subtração entre {num1} e {num2} é: {subtracao(num1, num2)}')

