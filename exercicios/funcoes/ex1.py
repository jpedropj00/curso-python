def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado, args

qtNum = int(input('Quantos números deseja multiplicar? '))
tupla_numeros = ()
for i in range(qtNum):
    num = int(input(f'Digite o {i+1}° número: '))
    tupla_numeros += (num,)
print(f'O resultado da multiplicação é: {multiplicar(*tupla_numeros)}')

    