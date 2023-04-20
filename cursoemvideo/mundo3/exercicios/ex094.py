# Unindo Dicionários e Listas

print('-='*40)
print(f'{"Unindo Dicionários e Listas:":^75}')
print('-='*40)
print('')

galera = list()
pessoa = dict()

soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO: Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO: Por favor, digite apenas S ou N.')

    if resp == 'N':
        break

print('-='*30)

print(f'A) Ao Todo Temos {len(galera)} Pessoas Cadastradas!!!')

media = soma / len(galera)

print(f'B) A Média de Idade é de {media:5.2f} Anos!!!')

print(f'C) As Mulheres Cadastradas Foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')

print()
print(f'D) A Lista de Pessoas que Estão Acima da Média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()

print('\nFIM')
