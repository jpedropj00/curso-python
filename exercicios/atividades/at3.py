lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1,2,3,4]
# def somar_listas(l1,l2):
#     intervalo = min(len(l1), len(l2))
#     return [
#         l1[i] + l2[i] for i in range(intervalo)
#     ]
# print(somar_listas(lista1, lista2))
lista_soma = []
# if len(lista1) > len(lista2):
#     intervalo = len(lista2)
# else:
#     intervalo = len(lista1)
# for i in range(intervalo):
#     lista_soma.append(lista1[i] + lista2[i])
from itertools import zip_longest
lista_soma = [x + y for x, y in zip_longest(lista1, lista2, fillvalue=0)]
print(lista_soma)