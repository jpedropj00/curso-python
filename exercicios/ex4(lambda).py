def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def criar_multiplicador(multiplicador):
    def multiplicar(x):
        return x * multiplicador
    return multiplicar

#soma = lambda x,y : x + y, 2,3 -> 5
print(executa(soma,2,3)) # Saída: 5

dobrar = criar_multiplicador(2)
print(dobrar(5)) #Saída: 10

#duplica = executa(
#    lambda m : lambda n: n * m, 3)(4
# )