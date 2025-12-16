lista = [
    {'produto': 'banana', 'preco': 5.00},
    {'produto': 'maca', 'preco': 3.50},
    {'produto': 'uva', 'preco': 7.00},
    {'produto': 'abacaxi', 'preco': 10.00},
    {'produto': 'laranja', 'preco': 4.00},
    {'produto': 'pera', 'preco': 6.00}
]

def exibir(lista):
    for item in lista:
        print(item)
l1 = sorted(lista, key=lambda item: item['preco'])
l2 = sorted(lista, key=lambda item:item['produto'])

exibir(l1)
print('-'*50)
exibir(l2)