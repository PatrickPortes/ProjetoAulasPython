# Matriz em Python v1.0

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = (int(input(f'Digite um Valor para a Posição [{l}],[{c}]: ')))

print('=-'*20)

for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()

print('\nFIM')
