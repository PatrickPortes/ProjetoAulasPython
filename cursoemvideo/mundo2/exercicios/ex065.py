# Maior e Menor Valores

qtd = soma = media = meaior = menor = 0

again = 'S'

while again in 'Ss':
    num = int(input('Digite um Número: '))

    soma += num
    qtd += 1

    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    again = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]

media = soma / qtd

print(f'VOCÊ DIGITOU {qtd} NÚMEROS, E A SOMA ENTRE ELES FOI {soma}!!! E SUA MÉDIA É {media}!!!')

print(f'\nO MAIOR NÚMERO DIGITADO FOI {maior}, E O MENOR FOI {menor}!!!')
