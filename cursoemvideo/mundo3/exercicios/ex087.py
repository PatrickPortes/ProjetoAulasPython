# Matriz em Python v2.0

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

somaPar = somaImpar = maior = somaColuna = 0


for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = (int(input(f'Digite um Valor para a Posição [{l}],[{c}]: ')))

        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        else:
            somaImpar += matriz[l][c]

print('=-'*20)

for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()


for l in range(0,3):
    somaColuna += matriz[l][2]

for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print('=-'*20)

print(f'A Soma de Todos os Valores Pares Digitados é: {somaPar}')
print(f'A Soma de Todos os Valores Ímpares Digitados é: {somaImpar}')
print(f'A Soma dos Valores da Terceira Coluna é: {somaColuna} ')
print(f'O Maior Valor da Segunda Linha é: {maior}')

print('\nFIM')
