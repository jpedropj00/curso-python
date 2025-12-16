import random
def primeiro_duplicado(lista):
    numeros_checados = set()
    primeiro_duplicado = -1
    for numero in lista:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        numeros_checados.add(numero)
    
    return primeiro_duplicado
tam = int(input('Digite o tamanho da lista: '))
lista = [random.randint(1,10) for _ in range(tam)]
print('Lista gerada: ', lista)
print(primeiro_duplicado(lista))
        
