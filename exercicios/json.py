import json
pessoa = {
    'nome': 'João',
    'sobrenome': 'Souza',
    'enderecos': [
        {'rua': 'Rua A', 'numero': 123},
        {'rua': 'Rua B', 'numero': 456}
    ],
    'altura': 1.8,
    'numeros_preferidos': [7, 13, 42],
    'dev': True,
    'nada': None
}
with open('pessoa.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(pessoa, arquivo_json,ensure_ascii=False, indent=2
)