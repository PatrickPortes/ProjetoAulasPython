# Lista Composta e Análise de Dados

pessoas = list()
infos = list()

contador = 0
maior = menor = 0

while True:
    pessoas.append(str(input('Digite o seu Nome: ')))
    pessoas.append(float(input('Digite o seu Peso: ')))

    if len(infos) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    infos.append(pessoas[:])
    pessoas.clear()

    contador += 1

    continuar = str(input('Você Gostaria de Continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break

print(f'\nForam Cadastradas no Total {contador} Pessoas!!!')

print(f'O Maior Peso foi de {maior}Kg. Peso de ', end='')
for i in infos:
    if i[1] == maior:
        print(f'[{i[0]}] ', end='')

print(f'\nO Menor Peso foi de {menor}Kg. Peso de ', end='')
for i in infos:
    if i[1] == menor:
        print(f'[{i[0]}] ', end='')

print('\n\nFIM')