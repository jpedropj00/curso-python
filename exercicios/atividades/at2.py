# def unir_lista(lista1, lista2):
#     lista3 = []
#     if len(lista1) > len(lista2):
#         maior_tamanho = len(lista1)
#     else:
#         maior_tamanho = len(lista2)
#     for i in range(maior_tamanho):
#         if i >= len(lista1):
#             continue
#         elif i >= len(lista2):
#             continue
#         tupla = (lista1[i], lista2[i])
#         lista3.append(tupla)
#     return lista3
# lista = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# lista2 = ['BA', 'SP', 'MG', 'RJ']

# lista3 = unir_lista(lista, lista2)
# print(*lista3, sep='\n')

#Minha resolução 
lista = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
# def zipper(lista1, lista2):
#     intervalo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i], lista2[i]) for i in range(intervalo)
#     ]
# print(zipper(lista, lista2))

#Resolução do curso
from itertools import zip_longest
#Resolução utilizando funcção já existente no python
print(list(zip_longest(lista, lista2)))
print(list(zip(lista, lista2)))
#AS DUAS MANEIRAS COM FUNÇÔES JÁ FEITAS

    