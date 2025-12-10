lista_compras = []
while True:
    print('''MENU:
          1 - Adicionar item
          2 - Remover Item
          3 - Listar Itens]
          4 - Sair''')
    escolha = int(input('Escolha uma opção:'))
    if escolha <= 0 or escolha > 4 or not escolha or escolha.is_integer() is False:
        print('Opção inválida, tente novamente.')
        continue
    if escolha == 1:
        produto = input('Digite o nome do produto a ser adicionado: ')
        lista_compras.append(produto)
        print(f'Produto {produto} adicionado com sucesso.')
    elif escolha == 2:
        for i, produto in enumerate(lista_compras, start=1):
            print(f'{i}° - {produto}')
        indice = int(input('Digite o número do produto a ser removido: '))
        if indice < 1 or indice > len(lista_compras):
            print('Indice invalido')
            continue
        produto_removido = lista_compras.pop(indice - 1)
        print(f'Produto {produto_removido} removido com sucesso.')
    elif escolha == 3:
        if not lista_compras:
            print('A lista de compras está vazia.')
        else:
            print('Itens:')
            for i, produto in enumerate(lista_compras, start=1):
                print(f'{i}° - {produto}')
    elif escolha == 4:
        print('Saindo...')
        break
        