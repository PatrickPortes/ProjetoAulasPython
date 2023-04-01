# Quebrando um Número

from math import trunc, floor

real = float(input('Digite um número com vírgula: '))

inteiro = trunc(real)

print(f'O número {real} tem a parte inteira {inteiro}!')
print(f'O número {real} tem a parte inteira {int(inteiro)}!')
