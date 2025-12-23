# ================= LISTA DE TAREFAS =================
import json

CAMINHO_ARQUIVO = 'dados_salvos.json'

# --------------------------------------------------

def criar_lista_tarefas():
    return []

# --------------------------------------------------

def adicionar_tarefa(lista_tarefas, tarefa):
    lista_tarefas.append(tarefa)

# --------------------------------------------------

def verificar_lista_vazia(lista_tarefas):
    return len(lista_tarefas) == 0

# --------------------------------------------------

def remover_tarefa(lista_tarefas, tarefa=None, tarefa_removida=None):
    if verificar_lista_vazia(lista_tarefas):
        print('A lista está vazia!')
        return

    try:
        if tarefa_removida is not None:
            lista_tarefas.pop(tarefa_removida - 1)
        elif tarefa in lista_tarefas:
            lista_tarefas.remove(tarefa)
        else:
            print('Tarefa não encontrada.')
    except IndexError:
        print('Número de tarefa inválido.')

# --------------------------------------------------

def exibir_tarefas(lista_tarefas):
    if verificar_lista_vazia(lista_tarefas):
        print('A lista está vazia!')
        return

    print('Lista de tarefas:')
    for i, tarefa in enumerate(lista_tarefas, start=1):
        print(f'{i}. {tarefa}')

# --------------------------------------------------

def marcar_tarefa_concluida(lista_tarefas, tarefa_concluida=None, tarefa=None):
    if verificar_lista_vazia(lista_tarefas):
        print('A lista está vazia!')
        return

    try:
        if tarefa is not None:
            if '✅' not in lista_tarefas[tarefa - 1]:
                lista_tarefas[tarefa - 1] += ' - ✅'
        elif tarefa_concluida in lista_tarefas:
            i = lista_tarefas.index(tarefa_concluida)
            if '✅' not in lista_tarefas[i]:
                lista_tarefas[i] += ' - ✅'
        else:
            print('Tarefa não encontrada.')
    except IndexError:
        print('Número de tarefa inválido.')

# --------------------------------------------------

def limpar_lista(lista_tarefas):
    lista_tarefas.clear()

# --------------------------------------------------

def exibir_menu():
    print('''
MENU
1. Adicionar tarefa
2. Remover tarefa
3. Exibir tarefas
4. Marcar tarefa como concluída
5. Limpar lista de tarefas
6. Sair
''')

# --------------------------------------------------

def obter_opcao_usuario():
    try:
        return int(input('Escolha uma opção (1-6): '))
    except ValueError:
        return 0

# --------------------------------------------------

def confirmar_apagamento():
    confirmacao = input('Tem certeza que deseja limpar a lista? (s/n): ').lower()
    if confirmacao not in ('s', 'n'):
        print('Opção inválida.')
        return False
    return confirmacao == 's'

# --------------------------------------------------

def verificar_opcao_valida(opcao):
    if 1 <= opcao <= 6:
        return True
    print('Opção inválida.')
    return False

# --------------------------------------------------

def carregar_dados(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# --------------------------------------------------

def salvar_dados(lista_tarefas, caminho):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_tarefas, arquivo, indent=2, ensure_ascii=False)

# ================= PROGRAMA PRINCIPAL =================

lista_tarefas = carregar_dados(CAMINHO_ARQUIVO)

while True:
    exibir_menu()
    opcao = obter_opcao_usuario()

    if not verificar_opcao_valida(opcao):
        continue

    if opcao == 1:
        tarefa = input('Digite a tarefa que deseja adicionar: ')
        adicionar_tarefa(lista_tarefas, tarefa)
        salvar_dados(lista_tarefas, CAMINHO_ARQUIVO)

    elif opcao == 2:
        exibir_tarefas(lista_tarefas)
        tarefa = input('Digite o número ou o nome da tarefa a remover: ')
        if tarefa.isdigit():
            remover_tarefa(lista_tarefas, tarefa_removida=int(tarefa))
        else:
            remover_tarefa(lista_tarefas, tarefa=tarefa)
        salvar_dados(lista_tarefas, CAMINHO_ARQUIVO)

    elif opcao == 3:
        exibir_tarefas(lista_tarefas)

    elif opcao == 4:
        exibir_tarefas(lista_tarefas)
        tarefa = input('Digite o número ou o nome da tarefa a concluir: ')
        if tarefa.isdigit():
            marcar_tarefa_concluida(lista_tarefas, tarefa=int(tarefa))
        else:
            marcar_tarefa_concluida(lista_tarefas, tarefa_concluida=tarefa)
        salvar_dados(lista_tarefas, CAMINHO_ARQUIVO)

    elif opcao == 5:
        if confirmar_apagamento():
            limpar_lista(lista_tarefas)
            salvar_dados(lista_tarefas, CAMINHO_ARQUIVO)

    elif opcao == 6:
        print('Encerrando o programa.')
        break

        
    

        