# Números Primos

n = int(input('Digite um Número: '))

total = 0

for c in range(1,n + 1):
    if n % c == 0:
        print('\033[31m', end=' ')
        total +=1
    else:
        print('\033[m', end=' ')
    print(f'{c}', end=' ')

print(f'\n\033[mO Número {n} foi Divisível {total} Vezes!!!')

if total == 2:
    print('E Por Isso ele é um Número Primo!!!')
else:
    print('E Por Isso ele NÃO é um Número Primo!!!')