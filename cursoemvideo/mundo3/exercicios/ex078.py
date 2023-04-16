# Maior e Menor Valores na Lista:

valores = list()

maior = menor = 0

for num in range(0, 5):
    valores.append(int(input(f'Digite um Valor para a Posição {num}: ')))

    if num == 0:
        maior = menor = valores[num]
    else:
        if valores[num] > maior:
            maior = valores[num]
        if valores[num] < menor:
            menor = valores[num]

print(f'\nOs Valores Digitados Foram: {valores}')

print(f'\nO Maior Valor Digitado foi O Número: {maior} e Estava nas Posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...')


print(f'\nO Menor Valor Digitado foi O Número: {menor} e Estava nas Posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...')

