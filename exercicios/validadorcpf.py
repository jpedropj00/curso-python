cpf = input('Informe o CPF: ')
def verificar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        print('CPF inválido (formato incorreto)')
        return False
    soma = 0
    for i in range(len(cpf) - 2):
        soma += int(cpf[i]) * (10 - i)
    digit1 = (soma * 10) % 11
    if digit1 > 9:
        digit1 = 0
    if digit1 != int(cpf[9]):
        print('CPF inválido')
        return False
    soma = 0
    for i in range(len(cpf) - 1):
        soma += int(cpf[i]) * (11 - i)
    digit2 = soma * 10 % 11
    if digit2 > 9:
        digit2 = 0
    if digit2 != int(cpf[10]):
        print('CPF inválido')
        return False
    print('CPF Válido')
    return True
verificar_cpf(cpf)
    
        