from itertools import groupby
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rose', 'nota': 'C'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'Ana', 'nota': 'A'},
    {'nome': 'Carlos', 'nota': 'B'},
    
]
alunos_ordenados = sorted(alunos, key=lambda aluno: aluno['nota'])
grupos = groupby(alunos_ordenados, key=lambda aluno:aluno['nota'])
for chave, grupo in grupos:
    print(f'Grupo {chave}:')
    for aluno in grupo:
        print(f'\t{aluno["nome"]}')