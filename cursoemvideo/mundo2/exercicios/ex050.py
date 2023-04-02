# Soma dos Pares

s = 0
count = 0

for c in range(0, 6):
    n = int(input('Digite um Número: '))
    if n % 2 == 0:
        s += n
        count += 1

print(f'\nVocê Forneceu {count} Números Pares e o Resultado da Soma é: {s}')
print('\nFIM')
