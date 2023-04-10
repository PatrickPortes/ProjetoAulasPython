# Ánalise de Dados do Grupo

contMaiorIdade = contHomem = contMulheres20 = 0

while True:
    idade = int(input('Digite sua Idade: '))

    sexo = continuar = ' '

    while sexo not in 'MF':
        sexo = str(input('Digite seu Sexo: [M/F] ')).strip().upper()[0]

    while continuar not in 'SN':
        continuar = str(input('\nVocê quer Continuar? [S/N] ')).strip().upper()[0]

    if idade >= 18:
        contMaiorIdade += 1

    if sexo in 'M':
        contHomem += 1

    if sexo in 'F' and idade <= 20:
        contMulheres20 += 1

    if continuar == 'N':
        break
print('\nFIM DO CADASTRO!!!\n')

print(f'{contMaiorIdade} ao todo são maior de idade!!!')
print(f'Foram cadastrados {contHomem} pessoas do sexo masculino!!!')
print(f'Foram cadastrados {contMulheres20} mulheres com menos de 20 anos!!!')

