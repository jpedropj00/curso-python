def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'
num = int(input('Digite um número inteiro: '))
resultado = par_ou_impar(num)
print(f'O número {num} é {resultado}.')