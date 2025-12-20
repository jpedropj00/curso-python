caminho_arquivo = 'C:\\pasta-teste'
caminho_arquivo += '\\novo-arquivo-teste.txt'
# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Msg teste')
    arquivo.write('\nAtenção')
with open(caminho_arquivo, 'r') as arquivo:
    texto = arquivo.read()
    print(texto)
    