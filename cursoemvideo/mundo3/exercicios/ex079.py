# Valores Únicos em uma Lista

num = list()

continuar = 'S'

while continuar in 'Ss':
    valor = int(input(f'\nDigite um Número: '))
    if valor not in num:
        num.append(valor)
        print('Valor Adicionado com Sucesso!!!')
    else:
        print('Valor Duplicado, Tente Novamente!!!')

    continuar = str(input('Gostaria de Continuar? [S/N] ')).strip().upper()[0]

print(f'\nVocê Digitou os Valores: {num}')

num.sort()
print(f'\nLista dos Valores em Ordem Crescente = {num}')

num.sort(reverse=True)
print(f'\nLista dos Valores em Ordem Decrescente = {num}')

