def criar_multiplicacao(n):
    def multiplicar(num):
        return num * n
    return multiplicar
duplicar = criar_multiplicacao(2)
triplicar = criar_multiplicacao(3)
quadruplicar = criar_multiplicacao(4)

num = int(input('Digite um número para ver suas multiplicações: '))
print(f'O dobro de {num} é {duplicar(num)}')
print(f'O triplo de {num} é {triplicar(num)}')
print(f'O quadruplo de {num} é {quadruplicar(num)}')