# Somas Ímpares Multiplos de Três

print('Números Ímpares Multiplos de Três no Intervalo de 1 até 500:')

s = 0
count = 0
for c in range(1,500): # Poderia tira o and do if e colocar range(1, 501, 2)
    if c % 3 == 0 and c % 2 != 0:
        print(c)
        count += 1
        s += c

print(f'\nO Somatório de Todos os {count} Números Multiplos de Três Ímpares foi: {s}')

print('\nFIM')