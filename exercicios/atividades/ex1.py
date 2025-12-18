import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 5.50},
    {'nome': 'Produto 2', 'preco': 105.99},
    {'nome': 'Produto 4', 'preco': 75.20},
]
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.10, 2)}
    for p in copy.deepcopy(produtos)
]
#Adiciona 10% ao preço de cada produto na nova lista

#Ordenando os novos produtos por nome decrescente
novos_produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p['nome'],
    reverse=True
)
#Ordenando produtos por preço
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key = lambda p:p['preco']
)
#Utilizando o deepcopy para copiar a lista
print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*novos_produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')






        
