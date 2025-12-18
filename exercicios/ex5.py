from itertools import combinations, permutations, product
pessoas = ['João', 'Joana', 'Luiz', 'Leticia']
camisetas = [
    ['Preta', 'Branca'],
    ['P', 'M', 'G']
    ]

print(*list(combinations(pessoas,2)), sep='\n')
print()
print(*list(permutations(pessoas,2)), sep='\n')
print()
print(*list(product(*camisetas)), sep='\n')