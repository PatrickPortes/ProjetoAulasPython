# Validação de Dados:

s = str(input('Qual o seu Sexo? [M/F] ')).strip().upper()[0]

while s not in 'MmFf':
    print('Dados Inválidos!!! Tente Novamente!!!')
    s = str(input('Qual o seu Sexo? [M/F] ')).strip().upper()[0]
print(f'Sexo {s} Registrado com Sucesso!!! ')
