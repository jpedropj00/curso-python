import random
def gerar_cpf():
    cpf = [random.randint(0,9) for _ in range(9)]
    
    soma = 0
    for i in range(9):
        soma += cpf[i] * (10 - i)
    digit1 = (soma * 10) % 11
    if digit1 > 9:
        digit1 = 0
    cpf.append(digit1)
    
    soma = 0
    for i in range(10):
        soma += cpf[i] * (11 - i)
    digit2 = (soma * 10) % 11
    if digit2 > 9:
        digit2 = 0
    cpf.append(digit2)
    
    cpf_formatado = formatar_cpf(cpf)
    return cpf_formatado

def formatar_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

print("CPF Gerado:", gerar_cpf())