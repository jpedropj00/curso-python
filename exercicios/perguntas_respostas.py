perguntas = [
    {
        'pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'resposta': '4'
    },
    {
        'pergunta': 'Quanto é 5 + 5?',
        'Opções': ['25', '55', '10', '51'],
        'resposta': '10'
    },
    {
        'pergunta': 'Quanto é 10/2 ?',
        'Opções': ['4', '5', '2', '1'],
        'resposta': '5'
    }
]
contAcertos = 0
for item in perguntas:
    print(item['pergunta'])
    for i, opcao in enumerate(item['Opções'], start=1):
        print(f'{i}) {opcao}')
    resposta_user = input('Digite o número da resposta correta:')
    if item['Opções'][int(resposta_user) - 1] == item['resposta']:
        print('Resposta correta')
        contAcertos += 1
    else:
        print('Resposta incorreta')

        