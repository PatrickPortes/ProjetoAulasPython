# Análise de Dados em uma Tupla

num = (int(input('Digite o Primeiro Número: ')), int(input('Digite o Segundo Número: ')),
       int(input('Digite o Terceiro Número: ')),int(input('Digite o Quarto Número: ')))

print(f'\nVocê Digitou os Valores: {num}')

print(f'\nO Número 9 Apereceu na Tupla {num.count(9)} Vezes!')

if 3 in num:
    print(f'\nO Número 3 Apereceu na {num.index(3)+1}ª Posição da Tupla!')
else:
    print('O Valor 3 Não foi Digitado!')

print('\nOs Valores Pares Digitados Foram: ', end='')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')